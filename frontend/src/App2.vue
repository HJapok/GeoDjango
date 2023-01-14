<template>
  <div id="container">
    <div id="mapContainer"></div>
  </div>
 </template>
  
  <script>
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";

  import image from "./assets/Picture1.png";
  import image2 from "./assets/Picture2.png";
  import image3 from "./assets/Picture3.png";  
  export default {
   name: "Map",
   data() {
     return{
       center: [2.782872, 101.71627],
       markerLatLng: [[2.782872, 101.71627], [2.783708,101.715358], [2.781881, 101.716726], [2.782304, 101.717257], [2.784077, 101.715889]],
       polygon: {
        latlngs: [[2.783708,101.715358], [2.781881, 101.716726], [2.782304, 101.717257], [2.784077, 101.715889], [2.783708, 101.715358]],
        color: 'green'
      },
      imageUrl1: image,
      imageUrl2: image2,
      imageUrl3: image3,
      imageBounds: [[2.7789,101.7151], [2.7858, 101.7218]],
     }},
   
     methods: {
     setupLeafletMap: function () {
        const mapDiv = L.map("mapContainer").setView(this.center, 18);
        
        // OSM Layer
        var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        });
        
        // Satelite Layer
        var satelite = L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", {
        attribution: 'Satelite'
        }).addTo(mapDiv);

        var raster = L.imageOverlay(this.imageUrl3, this.imageBounds)

        // var littleton = L.marker([2.782872, 101.71627]).bindPopup('This is Littleton, CO.'),
        //     denver    = L.marker([2.783708,101.715358]).bindPopup('This is Denver, CO.'),
        //     aurora    = L.marker([2.781881, 101.716726]).bindPopup('This is Aurora, CO.'),
        //     golden    = L.marker([2.782304, 101.717257]).bindPopup('This is Golden, CO.'),
        //     golden1    = L.marker([2.784077, 101.715889]).bindPopup('This is Golden1, CO.');
        
        var tag = []
        for (let i = 0; i < this.markerLatLng.length; i++) {
            // console.log(this.markerLatLng[i]);
            // L.marker(this.markerLatLng[i]).addTo(mapDiv)
            tag.push(L.marker(this.markerLatLng[i]).bindPopup('This tag '+i))
          }
          console.log(tag);
          tag.push(raster)

          var polygon = L.polygon(this.polygon.latlngs, {color: this.polygon.color})
          var baseMaps = {
              "Satelite": satelite,
              "OpenStreetMap": osm,
          };

          var treetag = L.layerGroup(tag);

          var overlayMaps = {
              "Boundary": polygon,
              "DSM": L.imageOverlay(this.imageUrl1, this.imageBounds),
              "DTM": L.imageOverlay(this.imageUrl2, this.imageBounds),
              "TreeTag": treetag
          };
          var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(mapDiv);

          // L.imageOverlay(this.imageUrl1, this.imageBounds).addTo(mapDiv);


     },

   },
   mounted() {
     this.setupLeafletMap();
   },
  };
  </script>
  
  
  <style scoped>
  #mapContainer {
   width: 80vw;
   height: 100vh;
  }
  </style>