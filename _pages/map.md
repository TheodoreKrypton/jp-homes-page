---
layout: default
title: Map
permalink: /map
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
     integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
     crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
     integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
     crossorigin=""></script>

<style>
#map { height: 500px}
</style>

<div id="map"></div>

<script>
var map = L.map('map').setView([36.5551, 139.8826], 5);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var req = new XMLHttpRequest();

req.onload = (e) => {
  var data = JSON.parse(req.responseText);
  L.geoJSON(data, {
    onEachFeature: function (feature, layer) {
      layer.on('click', function (e) {
        window.open(feature.properties.URL);
      });
    }
  }).addTo(map);
};
req.open("GET", 'https://raw.githubusercontent.com/TheodoreKrypton/jp-homes-page/map/map.json');
req.send();

</script>

