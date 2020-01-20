console.log("Loaded map.js");
d3.json("/map").then(function(data) {
    
    // ... and dump that JSON to the console for inspection
    console.log(data); 

    // send to createMarkers function
    createMarkers(data);

    function createMap(stadiumMap) {

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
          "Stadium Cities": stadiumMap
        };
      
        // Create the map object with options
        var map = L.map("map", {
            center: [39.828175,-98.579500],
            zoom: 5,
            layers: [lightmap, stadiumMap]
        });
      
        // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
        L.control.layers(baseMaps, overlayMaps, {
          collapsed: false
        }).addTo(map);
    }
    
    function createMarkers(sbdata) {
    
        // Pull the "stations" property off of response.data
        var superbowlCities = data.map(d => d.city_state);


        console.log("superbowlCities:"+superbowlCities);
        
        // Initialize an array to hold bike markers
        var stadiumMarkers = [];
       
        stadiumCity = data.map(d => d.superbowl);
        superbowlGame = data.map(d => d.city_state);
        stadiumLat = data.map(d => d.lat);
        stadiumLong = data.map(d => d.long);

        console.log("City: "+stadiumCity);
        console.log("Superbowl: "+superbowlGame);
        console.log("Lat: "+stadiumLat);
        console.log("Long: "+stadiumLong);
    
        // test markers for trial map
        var testMarker= ([34.1139, -118.4868],[33.2525,-110.2558])

        // // Loop through the stations array
        // for (var index = 0; index < superbowlCities.length; index++) {

        //     var stadiumList = superbowlCities[index];

        //     console.log("stadiumList: "+stadiumList);
        
        //     // For each station, create a marker and bind a popup with the station's name
        //     var stadiumMarker = L.marker([stadiumList.lat, stadiumList.long])
        //     // .bindPopup("<h3>Super Bowl" + stadiumList.superbowl + "<h3>");
        
        //     // Add the marker to the bikeMarkers array
        //     stadiumMarkers.push(stadiumMarker);
        // }
      
        // Create a layer group made from the bike markers array, pass it into the createMap function
        createMap(L.layerGroup(testMarker));
        
        // createMap(L.layerGroup(stadiumMarkers));
    }
      

});