console.log("Loaded winners.js");

d3.json("/dictionary").then((importedData) => {

    var data = importedData;

    var winners = [...new Set(data.map(row => row.Winner))];
    var winamount = [4, 1, 1, 1, 5, 2, 6, 2, 5, 3, 1, 1, 4, 3, 1, 2, 6, 1, 1, 1, 1, 1];

    var losers = [...new Set(data.map(row => row.Loser))];
    var loseamount = [1, 2, 1, 4, 3, 3, 2, 5, 1, 2, 2, 5, 4, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1]; 
   
    var trace1 = {
        x: winners,
        y: winamount,
        text: data.map(row => row.winners),
        name: "Wins",
        type: "bar",
        
    };
    
    var trace2 = {
        x: losers,
        y: loseamount,
        text: data.map(row => row.losers),
        name: "Loses",
        type: "bar",
        
    }
    
    var Data = [trace1, trace2];
    
      
    var layout = {
        title: "Super Bowl win/lose",
        barmode: "group",
        xaxis: { title: "Teams"},
        yaxis: { title: "Wins/Loses"},
        
        
    };
    
      
    Plotly.newPlot("plot", Data, layout);
});

