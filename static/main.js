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
      
        // Create an overlayMaps object to hold the stadiumMap layer
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
    
    // function createMarkers(data) {
        
    //     // Pull the event data
    //     var superbowlCities = data;
        

    //     // create markers
    //     // Initialize an array to hold quake markers
    //     var stadiumMarkers = [];

    //     for (var i = 0; i < superbowlCities.length; i++) {
    //         var superbowlCity = superbowlCities[i];
    //         var stadiumCity = superbowlCities.city_state; 

    //         console.log("stadiumCity: " + stadiumCity);

    //         // Adding circular markers + popups 
    //         stadiumMarker = L.marker([superbowlCity.lat, superbowlCity.long], {
    //         fillOpacity: 0.75,
    //         color: "white",
    //         fillcolor: "white",
    //         // fillColor: circleColor(timesHosted???),
    //         radius: 100
    //         });
    //         // }).bindPopup("<h1>Super Bowl" + superbowlCities.superbowl + "</h1>").addTo(map).addTo(map); 

    //         console.log(stadiumMarker);

    //         // Add the marker to the quakeMarkers array
    //         stadiumMarkers.push(stadiumMarker);

    //         console.log("stadiumMarkers:"+stadiumMarkers);
    //     };
    // };


    // Create a layer group made from the quake markers array, pass it into the createMap function
    createMap(L.layerGroup(stadiumMarkers));
    
});