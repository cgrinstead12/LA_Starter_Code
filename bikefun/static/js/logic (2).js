// Creating map object
var map = L.map("map", {
  center: [34.048339,-118.235807],
  zoom: 8.5,
  
});

// Adding tile layer
var streetMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 10,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);

var darkMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 10,
  id: "mapbox.dark",
  accessToken: API_KEY
}).addTo(map);

var link = "http://s3-us-west-2.amazonaws.com/boundaries.latimes.com/archive/1.0/boundary-set/la-county-neighborhoods-current.geojson";



// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Style each feature (in this case a neighborhood)
    style: function(feature) {
      return {
        color: "white",
        // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
        fillColor: "blue",
        fillOpacity: 0.1,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function(feature, layer) {
      // Set mouse events to change map styling
      layer.on({
        // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.5
          });
        },
        // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
        mouseout: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.1
          });
        },
        // When a feature (neighborhood) is clicked, it is enlarged to fit the screen
        click: function(event) {
          map.fitBounds(event.target.getBounds());
        }
      });
      // Giving each feature a pop-up with information pertinent to it
      layer.bindPopup("<h1>" + feature.properties.name + "</h1> <hr> <h2>" + feature.properties.metadata.type + "</h2>");

    }
  }).addTo(map);
  d3.json('/top30', function(d) {
    var latLongs = [];
    
    for (i = 0; i < d.length; i++) {
      var startPoints = [+d[i].start_lat, +d[i].start_lon];
      var endPoints = [+d[i].end_lat, +d[i].end_lon];
      
      latLongs.push([startPoints,endPoints]);
      // latLongs.push(endPoints);
      L.marker(startPoints).bindPopup("<h1>" + startPoints[0] + "," + startPoints[1] + "</h1> <hr> <h1>" + d[i].start_to_end_name + "</h1>")
      .addTo(map);
      L.marker(endPoints).bindPopup("<h1>" + endPoints[0] + "," + endPoints[1] + "</h1> <hr> <h1>" + d[i].start_to_end_name + "</h1>")
      .addTo(map);
    };

    // console.log(latLongs);

    var bikeRoutes = new L.polyline(latLongs, {
        // onEachFeature: onEachFeature,
        color: 'red',
        weight: 3,
        opacity: 0.5}).addTo(map);
  
    
    var baseMaps = {
      "Street Map": streetMap,
      "Night Map": darkMap
    };
    
    // d3.csv("start_station.csv", function(d) {
    //   startStations = [];
      
    //   for (var i = 0; i<d.length; i++) {
    //   var Stations = [+d[i].start_lat, +d[i].start_lon]
    //   startStations.push(Stations);
    //   L.marker(startStations).bindPopup("<h1>" + 
    //   d.start_station_name + "</h1> ").addTo(map);
    //   };
    //   console.log(startStations);
    //   var bikeStations = new L.marker(startStations).addTo(map);
    // });


    var overlayMaps = {
      "Top 100 Routes": bikeRoutes
      
    };
  
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);
  });
  
});
