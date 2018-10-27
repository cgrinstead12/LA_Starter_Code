d3.json("/day_week", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  var Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
  var Areas = [];
  for (i = 0; i<d.length; i++) {

    if (d[i].Region == "Venice") {
      VeniceTrips.push(+d[i].trip_count);
    }
    else if (d[i].Region == "DTLA") {
      dtlaTrips.push(+d[i].trip_count);
    }
    else if (d[i].Region == "Port of LA") {
      plaTrips.push(+d[i].trip_count);
    }
    else if (d[i].Region == "Pasadena") {
      pasTrips.push(+d[i].trip_count);
    };
    // Days.push(d[i].Day_Of_Week);
    Areas.push(d[i].Region);

  };

  console.log(Days);

  var trace1 = {
    x: Days,
    y: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    type: "bar"
  };


var trace2 = {
    x: Days,
    y: VeniceTrips,
    text: "Venice",
    name: "Venice",
    type: "bar"
  };
  var trace3 = {
    x: Days,
    y: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    type: "bar"
  };
  var trace4 = {
    x: Days,
    y: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    type: "bar"
  };

// Combining both traces
var data = [trace1, trace2, trace3, trace4];

// Apply the group barmode to the layout
var layout = {
  title: "Bike Trips by Area and Day of the Week",
  barmode: "stack"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot1", data, layout);

});

// d3.csv("day_of_week_normalized.csv", function(d) { 
//   var VeniceTrips = [];
//   var dtlaTrips = [];
//   var plaTrips = [];
//   var pasTrips = [];

//   var Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
//   var Areas = [];
//   for (i = 0; i<d.length; i++) {

//     if (d[i].Region == "Venice") {
//       VeniceTrips.push(+d[i].normalized_trip_count);
//     }
//     else if (d[i].Region == "DTLA") {
//       dtlaTrips.push(+d[i].normalized_trip_count);
//     }
//     else if (d[i].Region == "Port of LA") {
//       plaTrips.push(+d[i].normalized_trip_count);
//     }
//     else if (d[i].Region == "Pasadena") {
//       pasTrips.push(+d[i].normalized_trip_count);
//     };
//     // Days.push(d[i].Day_Of_Week);
//     Areas.push(d[i].Region);

//   };

//   console.log(Days);

//   var trace1 = {
//     x: Days,
//     y: dtlaTrips,
//     text: "DTLA",
//     name: "DTLA",
//     type: "bar"
//   };

//   // Trace 2 for the Roman Data
// var trace2 = {
//     x: Days,
//     y: VeniceTrips,
//     text: "Venice",
//     name: "Venice",
//     type: "bar"
//   };
//   var trace3 = {
//     x: Days,
//     y: plaTrips,
//     text: "Port of LA",
//     name: "Port of LA",
//     type: "bar"
//   };
//   var trace4 = {
//     x: Days,
//     y: pasTrips,
//     text: "Pasadena",
//     name: "Pasadena",
//     type: "bar"
//   };

// // Combining both traces
// var data = [trace1, trace2, trace3, trace4];

// // Apply the group barmode to the layout
// var layout = {
//   title: "Normalized Bike Trips by Area and Day of the Week",
//   barmode: "stack"
// };

// // Render the plot to the div tag with id "plot"
// Plotly.newPlot("plot2", data, layout);

// });



d3.json("/passholder", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  // var Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
  var passTypes = ["Walk-up", "One Day Pass", "Monthly Pass", "Flex Pass", "Annual Pass"];
  for (i = 0; i<d.length; i++) {

    if (d[i].Region == "Venice") {
      VeniceTrips.push(+d[i].trip_count);
    }
    else if (d[i].Region == "DTLA") {
      dtlaTrips.push(+d[i].trip_count);
    }
    else if (d[i].Region == "Port of LA") {
      plaTrips.push(+d[i].trip_count);
    }
    else if (d[i].Region == "Pasadena") {
      pasTrips.push(+d[i].trip_count);
    };
    // Days.push(d[i].Day_Of_Week);
    // passTypes.push(d[i].passholder_type);

  };

  // console.log(Days);

  var trace1 = {
    x: passTypes,
    y: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    type: "bar"
  };

  // Trace 2 for the Roman Data
var trace2 = {
    x: passTypes,
    y: VeniceTrips,
    text: "Venice",
    name: "Venice",
    type: "bar"
  };
  var trace3 = {
    x: passTypes,
    y: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    type: "bar"
  };
  var trace4 = {
    x: passTypes,
    y: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    type: "bar"
  };

// Combining both traces
var data = [trace1, trace2, trace3, trace4];

// Apply the group barmode to the layout
var layout = {
  title: "Passholder Types",
  barmode: "stack"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot3", data, layout);

});

// d3.csv("passholder_type_normalized.csv", function(d) { 
//   var VeniceTrips = [];
//   var dtlaTrips = [];
//   var plaTrips = [];
//   var pasTrips = [];

//   // var Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
//   var passTypes = ["Walk-up", "One Day Pass", "Monthly Pass", "Flex Pass", "Annual Pass"];
//   for (i = 0; i<d.length; i++) {

//     if (d[i].Region == "Venice") {
//       VeniceTrips.push(+d[i].normalized_trip_count);
//     }
//     else if (d[i].Region == "DTLA") {
//       dtlaTrips.push(+d[i].normalized_trip_count);
//     }
//     else if (d[i].Region == "Port of LA") {
//       plaTrips.push(+d[i].normalized_trip_count);
//     }
//     else if (d[i].Region == "Pasadena") {
//       pasTrips.push(+d[i].normalized_trip_count);
//     };
//     // Days.push(d[i].Day_Of_Week);
//     // passTypes.push(d[i].passholder_type);

//   };

//   // console.log(Days);

//   var trace1 = {
//     x: passTypes,
//     y: dtlaTrips,
//     text: "DTLA",
//     name: "DTLA",
//     type: "bar"
//   };

//   // Trace 2 for the Roman Data
// var trace2 = {
//     x: passTypes,
//     y: VeniceTrips,
//     text: "Venice",
//     name: "Venice",
//     type: "bar"
//   };
//   var trace3 = {
//     x: passTypes,
//     y: plaTrips,
//     text: "Port of LA",
//     name: "Port of LA",
//     type: "bar"
//   };
//   var trace4 = {
//     x: passTypes,
//     y: pasTrips,
//     text: "Pasadena",
//     name: "Pasadena",
//     type: "bar"
//   };

// // Combining both traces
// var data = [trace1, trace2, trace3, trace4];

// // Apply the group barmode to the layout
// var layout = {
//   title: "Normalized Passholder Types",
//   barmode: "stack"
// };

// // Render the plot to the div tag with id "plot"
// Plotly.newPlot("plot4", data, layout);

// });


  