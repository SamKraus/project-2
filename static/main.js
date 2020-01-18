console.log("Loaded map.js");
d3.json("/map").then(function (data) {
    // ... and dump that JSON to the console for inspection
    console.log(data); 
}