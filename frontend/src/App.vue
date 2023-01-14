<template>
  <div class="map">
    <l-map style="width:100%; height: 100%" :zoom="zoom" :center="center">
      <l-control-layers ref="layerCtrl" />
      <!-- <l-control-layers ref="layerCtrl"
        :position="layersPosition"
        :collapsed="false"
        :sort-layers="true"
      /> -->
      <!-- <l-tile-layer :url="url" ></l-tile-layer>  -->
      <l-tile-layer
        v-for="tileProvider in tileProviders"
        :key="tileProvider.name"
        :name="tileProvider.name"
        :visible="tileProvider.visible"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        :options="{ myCustomName: tileProvider.name }"
        layer-type="base"
      />
      <l-layer-group layer-type="overlay" name="DSM">
        <l-image-overlay :url="imageUrl1" :bounds="imageBounds"></l-image-overlay>
      </l-layer-group>
      <l-layer-group layer-type="overlay" name="DEM">
        <l-image-overlay :url="imageUrl2" :bounds="imageBounds"></l-image-overlay>
      </l-layer-group>
      <l-layer-group layer-type="overlay" name="Boundary">
        <l-polygon :lat-lngs="polygon.latlngs" :color="polygon.color"></l-polygon>
      </l-layer-group>
      <l-layer-group layer-type="overlay" name="TreeTag">
        <l-marker v-for="marker in markerLatLng" :lat-lng="marker" ></l-marker>
         <l-image-overlay :url="imageUrl3" :bounds="imageBounds"></l-image-overlay>
      </l-layer-group>
                        
    </l-map>
  </div>
</template>

<script>
import "leaflet";
import "leaflet/dist/leaflet.css";

import {
  LMap,
  LTileLayer,
  LMarker,
  LPolyline,
  LPolygon,
  LLayerGroup,
  LTooltip,
  LPopup,
  LControlZoom,
  LControlAttribution,
  LControlScale,
  LControlLayers,
  LImageOverlay,
} from "vue2-leaflet";

import image from "./assets/Picture1.png"
import image2 from "./assets/Picture2.png"
import image3 from "./assets/Picture3.png"

export default {
  name: "Map",
  components: {
    LImageOverlay,
    LMap,
    LTileLayer,
    LMarker,
    LPolyline,
    LPolygon,
    LLayerGroup,
    LTooltip,
    LPopup,
    LControlZoom,
    LControlAttribution,
    LControlScale,
    LControlLayers,
  },
  data: function() {
    return {
      zoom: 15,
      center: [2.782872, 101.71627],
      markerLatLng: [[2.782872, 101.71627], [2.783708,101.715358], [2.781881, 101.716726], [2.782304, 101.717257], [2.784077, 101.715889]],
      polygon: {
        latlngs: [[2.783708,101.715358], [2.781881, 101.716726], [2.782304, 101.717257], [2.784077, 101.715889], [2.783708, 101.715358]],
        color: 'green'
      },
      url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
      // url: "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      
      imageUrl1: image,
      imageUrl2: image2,
      imageUrl3: image3,
      imageBounds: [[2.7789,101.7151], [2.7858, 101.7218]],

      tileProviders: [
        {
          name: "OpenStreetMap",
          visible: true,
          attribution:
            '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        },
        {
          name: "GoogleEarth",
          visible: false,
          url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
          attribution:
            'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
        },
      ],

      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.map {
  height: 500px;
  width: 500px;
}
</style>