<template>
    <div id="container">
        <div id="mapContainer"></div>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import { ref, onMounted } from 'vue'
import axios from 'axios'

// import image from "./assets/plantation1.png";
// import image2 from "./assets/plantation2.png";
// import image3 from "./assets/plantation3.png";
// import image4 from "./assets/plantation4.png";
// import image5 from "./assets/plantation5.png";

export default {
    name: "Map",
    setup() {
        const center = [5.4152603, 102.2170545]
        // const markerLatLng = [[2.782872, 101.71627], [2.783708, 101.715358], [2.781881, 101.716726], [2.782304, 101.717257], [2.784077, 101.715889]]
        // const polygon = {
        //     latlngs: [[5.415570145398239, 102.2165935006721], [5.415725019100209, 102.21675445500246],
        //     [5.415751721458614, 102.21701198193097], [5.415564804925056, 102.21713538025091],
        //     [5.415244376447327, 102.21719976198304], [5.4149079263628686, 102.21725877857085],
        //     [5.414806457253019, 102.21707099851878], [5.414934628757367, 102.21687785332237],
        //     [5.415329824058001, 102.21669543841463]],
        //     color: 'green'
        // }
        

        // const imageUrl1 = image
        // const imageUrl2 = image2
        // const imageUrl3 = image3
        // const imageUrl4 = image4
        // const imageUrl5 = image5
        // const imageBounds = [[5.416072150215122, 102.21765534421183], [5.4144485555928235, 102.21645355107528]]
        const tree_data = []
        onMounted(async () => {
                const fetchtreetag = await axios.get('http://127.0.0.1:8000/api/v1/treehealth/')
                const tree_data = fetchtreetag.data

                const fetchplantation = await axios.get('http://127.0.0.1:8000/api/v1/plantationGIS/')
                const plantation_data = fetchplantation.data

                const polygon = []
                const fetchplot = await axios.get('http://127.0.0.1:8000/api/v1/plot/')
                const plot = fetchplot.data

                plot[0].Boudary.coordinates[0].forEach((item)=>{
                    polygon.push(item.reverse())
                }

                )
                
                console.log(plantation_data[0])
                
                const imageBounds = [plantation_data[0].IMG_bound_1.coordinates.reverse(),plantation_data[0].IMG_bound_2.coordinates.reverse()]
                
                
                const mapDiv = L.map("mapContainer", { zoomSnap: 0.15 }).setView(center, 18);
                const drone = L.icon({
                    iconUrl: 'https://cdn-icons-png.flaticon.com/512/1812/1812587.png',
                    iconSize: [40, 40],
                });
                const redDot = L.icon({
                    iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Basic_red_dot.png',
                    iconSize: [10, 10],
                });

                const greenDot = L.icon({
                    iconUrl: 'https://www.pngkey.com/png/full/417-4174990_how-to-set-use-small-green-dot-icon.png',
                    iconSize: [10, 10],
                });
                const yellowDot = L.icon({
                    iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/7/7c/GAudit_YellowDot.png',
                    iconSize: [10, 10],
                });
                const blueDot = L.icon({
                    iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Location_dot_blue.svg/2048px-Location_dot_blue.svg.png',
                    iconSize: [10, 10],
                });

                const deleteMarker = (marker) => {
                    marker.remove()
                }

                mapDiv.on('click', (e) => {
                    const latlng = e.latlng
                    const marker = L.marker([latlng.lat, latlng.lng]).addTo(mapDiv)
                    marker.bindPopup(`<p>Latitude: ${latlng.lat},${latlng.lng}</p>
                    <button id="delete-marker">Delete</button>`)
                    marker.on('click', () => {
                        marker.openPopup()
                        document.getElementById('delete-marker').addEventListener('click', () => {
                            deleteMarker(marker)
                        })
                    })

                })


                L.marker([5.416072150215122, 102.21765534421183]).addTo(mapDiv)
                L.marker([5.4144485555928235, 102.21645355107528]).addTo(mapDiv)
                L.marker([5.415388569283324,102.21694760019885], { icon: drone }).bindPopup("Weeding is progress").addTo(mapDiv)




                // OSM Layer
                var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                    maxNativeZoom: 19,
                    maxZoom: 25
                });

                // Satelite Layer
                var satelite = L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", {
                    attribution: 'Satelite',
                    maxNativeZoom: 19,
                    maxZoom: 25
                }).addTo(mapDiv);

                var raster = L.imageOverlay(`http://127.0.0.1:8000/${plantation_data[0].Raster}`, imageBounds)
                var tag = []
                for (let i = 0; i < tree_data.length; i++) {
                    // console.log(tree_data[i].Gps.coordinates[1]);
                    tag.push(L.marker([tree_data[i].Gps.coordinates[1], tree_data[i].Gps.coordinates[0]], { icon: blueDot }).bindPopup(
                        `<p>Latitude: ${tree_data[i].Gps.coordinates[1]},${tree_data[i].Gps.coordinates[0]}</p>`))
                }
                // console.log(tag);
                tag.push(raster)


                var health = []
                for (let i = 0; i < tree_data.length; i++) {
                    var icontype
                    if(tree_data[i].Health_class=="Healthy"){
                        icontype=greenDot
                    }
                    else if(tree_data[i].Health_class=="Moderate health"){
                        icontype=yellowDot
                    }
                    else if(tree_data[i].Health_class=="Unhealthy"){
                        icontype=redDot
                    }
                    health.push(L.marker([tree_data[i].Gps.coordinates[1], tree_data[i].Gps.coordinates[0]], { icon: icontype}).bindPopup(
                        `<p>Status: ${tree_data[i].Health_class}</p>`))
                }
                health.push(raster)

                var boundary = L.polygon(polygon, { color: 'green' })
                var baseMaps = {
                    "Satelite": satelite,
                    "OpenStreetMap": osm,
                };

                var treetag = L.layerGroup(tag);
                var treehealth = L.layerGroup(health);

                var overlayMaps = {
                    "Raster": raster,
                    "Boundary": boundary,
                    "DSM": L.imageOverlay(`http://127.0.0.1:8000/${plantation_data[0].DSM}`, imageBounds),
                    "DTM": L.imageOverlay(`http://127.0.0.1:8000/${plantation_data[0].DTM}`, imageBounds),
                    "Flow": L.imageOverlay(`http://127.0.0.1:8000/${plantation_data[0].Flow}`, imageBounds),
                    "TreeTag": treetag,
                    "TreeHealth": treehealth

                };
                var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(mapDiv);
    
        })
        // return {
        //     center,
        //     markerLatLng,
        //     polygon,
        //     imageUrl1,
        //     imageUrl2,
        //     imageUrl3,
        //     imageBounds,
        // }
    },

    // methods: {
    //     setupLeafletMap: function () {
    //         const mapDiv = L.map("mapContainer").setView(this.center, 18);

    //         // OSM Layer
    //         var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    //             attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    //         });

    //         // Satelite Layer
    //         var satelite = L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", {
    //             attribution: 'Satelite'
    //         }).addTo(mapDiv);

    //         var raster = L.imageOverlay(this.imageUrl3, this.imageBounds)
    //         var tag = []
    //         console.log(this.todos)
    //         for (let i = 0; i < this.markerLatLng.length; i++) {
    //             // console.log(this.markerLatLng[i]);
    //             // L.marker(this.markerLatLng[i]).addTo(mapDiv)
    //             tag.push(L.marker(this.markerLatLng[i]).bindPopup('This tag ' + i))
    //         }
    //         console.log(tag);
    //         tag.push(raster)

    //         var polygon = L.polygon(this.polygon.latlngs, { color: this.polygon.color })
    //         var baseMaps = {
    //             "Satelite": satelite,
    //             "OpenStreetMap": osm,
    //         };

    //         var treetag = L.layerGroup(tag);

    //         var overlayMaps = {
    //             "Boundary": polygon,
    //             "DSM": L.imageOverlay(this.imageUrl1, this.imageBounds),
    //             "DTM": L.imageOverlay(this.imageUrl2, this.imageBounds),
    //             "TreeTag": treetag
    //         };
    //         var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(mapDiv);

    //     },

    // },
    // mounted() {
    //     this.setupLeafletMap();
    // },
};
</script>


<style scoped>
#mapContainer {
    width: 80vw;
    height: 100vh;
}
</style>