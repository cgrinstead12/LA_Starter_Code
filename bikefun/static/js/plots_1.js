//// Visualization: By Day of Week ////
d3.json("day_week", function(d) { 
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

  // console.log(Days);

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
  title: "LA Bike Trips By Day of Week",
  barmode: "stack"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot1", data, layout);

});

d3.json("/day_week_normalized", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  var Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
  var Areas = [];
  for (i = 0; i<d.length; i++) {

    if (d[i].Region == "Venice") {
      VeniceTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "DTLA") {
      dtlaTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "Port of LA") {
      plaTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "Pasadena") {
      pasTrips.push(+d[i].normalized_trip_count);
    };
    // Days.push(d[i].Day_Of_Week);
    Areas.push(d[i].Region);

  };

  // console.log(Days);

  var trace1 = {
    x: Days,
    y: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    type: "bar"
  };

  // Trace 2 for the Roman Data
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
  title: "LA Bike Trips By Day of Week (Normalized)",
  barmode: "stack"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot2", data, layout);

});

//// Visualization of Passholder Types ////


d3.json("/passholder", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  // var Passholder Type
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
    passTypes.push(d[i].passholder_type);

  };

  // console.log(Days);

  var trace1 = {
    x: passTypes,
    y: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    type: "bar",
    width: 0.35
  };

  // Trace 2 for the Roman Data
var trace2 = {
    x: passTypes,
    y: VeniceTrips,
    text: "Venice",
    name: "Venice",
    type: "bar",
    width: 0.35
  };
  var trace3 = {
    x: passTypes,
    y: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    type: "bar",
    width: 0.35
  };
  var trace4 = {
    x: passTypes,
    y: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    type: "bar",
    width: 0.35
  };

// Combining both traces
var data = [trace1, trace2, trace3, trace4];

// Apply the group barmode to the layout
var layout = {
  title: "LA Bike Trips By Passholder Types",
  barmode: "stack"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot3", data, layout);

});

d3.json("/passholder_normalized", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  // var Passholder Type
  var passTypes = ["Walk-up", "One Day Pass", "Monthly Pass", "Flex Pass", "Annual Pass"];
  for (i = 0; i<d.length; i++) {

    if (d[i].Region == "Venice") {
      VeniceTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "DTLA") {
      dtlaTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "Port of LA") {
      plaTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "Pasadena") {
      pasTrips.push(+d[i].normalized_trip_count);
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
    type: "bar",
    width: 0.35
  };

  // Trace 2 for the Roman Data
var trace2 = {
    x: passTypes,
    y: VeniceTrips,
    text: "Venice",
    name: "Venice",
    type: "bar",
    width: 0.35
  };
  var trace3 = {
    x: passTypes,
    y: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    type: "bar",
    width: 0.35
  };
  var trace4 = {
    x: passTypes,
    y: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    type: "bar",
    width: 0.35
  };

// Combining both traces
var data = [trace1, trace2, trace3, trace4];

// Apply the group barmode to the layout
var layout = {
  title: "LA Bike Trips By Passholder Types (Normalized)",
  barmode: "stack"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot4", data, layout);

});


// //// Visualization of Route Category ////


d3.json("/routes", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  // var Passholder Type
  var routeCategory = ["Round Trip", "One Way"];
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
    labels: routeCategory,
    values: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    indexLabel:"{labels}",
    type: "pie"
  };

  // Trace 2 for the Roman Data
  var trace2 = {
    labels: routeCategory,
    values: VeniceTrips,
    text: "Venice",
    name: "Venice",
    indexLabel:"{labels}",
    type: "pie"
  };

  var trace3 = {
    labels: routeCategory,
    values: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    indexLabel:"{labels}",
    type: "pie"
  };
  var trace4 = {
    labels: routeCategory,
    values: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    indexLabel:"{labels}",
    type: "pie"
  };

// Combining both traces
var data1 = [trace1];
var data2 = [trace2];
var data3 = [trace3];
var data4 = [trace4];

// Apply the group barmode to the layout
var layout1 = {
  title: "DTLA Trips By Route Category",
  height: 400,
  width: 500
};

var layout2 = {
  title: "Venice Trips By Route Category",
  height: 400,
  width: 500
};

var layout3 = {
  title: "Port of LA Trips By Route Category",
  height: 400,
  width: 500
};

var layout4 = {
  title: "Pasadena Trips By Route Category",
  height: 400,
  width: 500
};


// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot5-1", data1, layout1);
Plotly.newPlot("plot5-2", data2, layout2);
Plotly.newPlot("plot5-3", data3, layout3);
Plotly.newPlot("plot5-4", data4, layout4);
});

//// Visualization of Year-Month ////


d3.json("/year_month", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  // var Passholder Type

  var yearMonth = [
    "2016-07-01",
"2016-08-01",
"2016-09-01",
"2016-10-01",
"2016-11-01",
"2016-12-01",
"2017-01-01",
"2017-02-01",
"2017-03-01",
"2017-04-01",
"2017-05-01",
"2017-06-01",
"2017-07-01",
"2017-08-01",
"2017-09-01",
"2017-10-01",
"2017-11-01",
"2017-12-01",
"2018-01-01",
"2018-02-01",
"2018-03-01",
"2018-04-01",
"2018-05-01",
"2018-06-01",
"2018-07-01",
"2018-08-01",
"2018-09-01"];
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
    x: yearMonth,
    y: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    mode: 'lines+markers'  
  };

  // Trace 2 for the Roman Data
var trace2 = {
    x: yearMonth,
    y: VeniceTrips,
    text: "Venice",
    name: "Venice",
    mode: 'lines+markers'  
  };
  var trace3 = {
    x: yearMonth,
    y: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    mode: 'lines+markers'  
  };
  var trace4 = {
    x: yearMonth,
    y: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    mode: 'lines+markers'  
  };

// Combining both traces
var data = [trace1, trace2, trace3, trace4];

// Apply the group barmode to the layout
var layout = {
  title: "LA Bike Trips By Year-Month",
  barmode: "line"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot7", data, layout);

});


d3.json("/year_month_normalized", function(d) { 
  var VeniceTrips = [];
  var dtlaTrips = [];
  var plaTrips = [];
  var pasTrips = [];

  // var Passholder Type

  var yearMonth = [
    "2016-07-01",
"2016-08-01",
"2016-09-01",
"2016-10-01",
"2016-11-01",
"2016-12-01",
"2017-01-01",
"2017-02-01",
"2017-03-01",
"2017-04-01",
"2017-05-01",
"2017-06-01",
"2017-07-01",
"2017-08-01",
"2017-09-01",
"2017-10-01",
"2017-11-01",
"2017-12-01",
"2018-01-01",
"2018-02-01",
"2018-03-01",
"2018-04-01",
"2018-05-01",
"2018-06-01",
"2018-07-01",
"2018-08-01",
"2018-09-01"];
  for (i = 0; i<d.length; i++) {

    if (d[i].Region == "Venice") {
      VeniceTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "DTLA") {
      dtlaTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "Port of LA") {
      plaTrips.push(+d[i].normalized_trip_count);
    }
    else if (d[i].Region == "Pasadena") {
      pasTrips.push(+d[i].normalized_trip_count);
    };
    // Days.push(d[i].Day_Of_Week);
    // passTypes.push(d[i].passholder_type);

  };

  // console.log(Days);

  var trace1 = {
    x: yearMonth,
    y: dtlaTrips,
    text: "DTLA",
    name: "DTLA",
    mode: 'lines+markers'  
  };

  // Trace 2 for the Roman Data
var trace2 = {
    x: yearMonth,
    y: VeniceTrips,
    text: "Venice",
    name: "Venice",
    mode: 'lines+markers'  
  };
  var trace3 = {
    x: yearMonth,
    y: plaTrips,
    text: "Port of LA",
    name: "Port of LA",
    mode: 'lines+markers'  
  };
  var trace4 = {
    x: yearMonth,
    y: pasTrips,
    text: "Pasadena",
    name: "Pasadena",
    mode: 'lines+markers'  
  };

// Combining both traces
var data = [trace1, trace2, trace3, trace4];

// Apply the group barmode to the layout
var layout = {
  title: "LA Bike Trips By Year-Month (Normalized)",
  barmode: "line"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot8", data, layout);

});