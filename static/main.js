// Show that we've loaded the JavaScript file
console.log("Loaded main.js");

// Query the endpoint that returns a JSON ...
d3.json("/map").then(function (data) {

    // ... and dump that JSON to the console for inspection
    console.log(data); 
    console.log("lat"+data.lat)
 
    function createMap(superBowls) {

        // Create the tile layer that will be the background of our map
        var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
            attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
            maxZoom: 18,
            id: "mapbox.light",
            accessToken: API_KEY
        });

        // Create a baseMaps object to hold the lightmap layer
        var baseMaps = {
            "Light Map": lightmap
        };

        // Create an overlayMaps object to hold the bikeStations layer
        var overlayMaps = {
            "Super Bowls": superBowls
        };

        // Create the map object with options
        var map = L.map("plot", {
            center: [39.828175,-98.579500],
            zoom: 5,
            layers: [lightmap, superBowls]
        });

        // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
        L.control.layers(baseMaps, overlayMaps, {
            collapsed: false
        }).addTo(map);
    }
    
    function createMarkers(response) {
    
        // Pull the "stations" property off of response.data
        var locations = response.city_state;
    
        // Initialize an array to hold bike markers
        var cityMarkers = [];
    
        // Loop through the stations array
        for (var index = 0; index < locations.length; index++) {
        var locationList = locations[index];
    
        // For each station, create a marker and bind a popup with the station's name
        var cityMarker = L.marker([location.lat, location.long])
            .bindPopup("<h3>Super Bowl" + location.superbowl + "<h3>");
    
        // Add the marker to the bikeMarkers array
        cityMarkers.push(cityMarker);
        }
    
        // Create a layer group made from the bike markers array, pass it into the createMap function
        createMap(L.layerGroup(cityMarkers));
    }
  
});