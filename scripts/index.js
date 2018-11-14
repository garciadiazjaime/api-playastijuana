const KEY_API = 'AIzaSyBb0NHFvyZSBHgcA49cEx3JakM79osLr1M';
const API_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?';
const data = ['key=' + KEY_API,
  'location=32.5170938,-117.1202092',
  'radius=3000',
  'rankby=prominence'];
const params = data.join('&');
const URL = [API_URL, params].join('');
console.log('URL', URL);
https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&name=cruise&key=YOUR_API_KEY


const request = require('request');
request(URL, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body) // Show the HTML for the Google homepage.
  }
})

// function initialize() {
//   var pyrmont = new google.maps.LatLng(-33.8665, 151.1956);
//
//   var map = new google.maps.Map(document.getElementById('map'), {
//     center: pyrmont,
//     zoom: 15,
//     scrollwheel: false
//   });
//
//   // Specify location, radius and place types for your Places API search.
//   var request = {
//     location: pyrmont,
//     radius: '500',
//     types: ['store']
//   };
//
//   // Create the PlaceService and send the request.
//   // Handle the callback with an anonymous function.
//   var service = new google.maps.places.PlacesService(map);
//   service.nearbySearch(request, function(results, status) {
//     if (status == google.maps.places.PlacesServiceStatus.OK) {
//       for (var i = 0; i < results.length; i++) {
//         var place = results[i];
//         // If the request succeeds, draw the place location on
//         // the map as a marker, and register an event to handle a
//         // click on the marker.
//         var marker = new google.maps.Marker({
//           map: map,
//           position: place.geometry.location
//         });
//       }
//     }
//   });
// }
//
// // Run the initialize function when the window has finished loading.
// google.maps.event.addDomListener(window, 'load', initialize);
