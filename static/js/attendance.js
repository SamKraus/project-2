console.log("Loaded winners.js");

d3.json("/dictionary").then((importedData) => {

    var data = importedData;

    //var sorteddata = data.sort((a, b) => b.Attendance - a.Attendance);

    
    var trace1 = {
        x: data.map(row => row.Superbowl),
        y: data.map(row => row.Attendance),
        text: data.map(row => row.Stadium),
        name: "Attendance",
        type: "bar",
        
    };
    
      // data
    var Data = [trace1];
    
      
    var layout = {
        title: "Super Bowl Attendance",
        xaxis: { title: "Super Bowl #"},
        yaxis: { title: "Total Attendance"},
        
    };
    
      // Render the plot to the div tag with id "plot"
    Plotly.newPlot("plot", Data, layout);
    });