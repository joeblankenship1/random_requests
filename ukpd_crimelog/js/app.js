(function() {
    // map options
    var options = {
        scrollWheelZoom: true,
        zoomSnap: .1,
        dragging: true,
        zoomControl: false,
        center: [38.030006, -84.498612],
        zoom: 14
    }
    // create the Leaflet map
    var map = L.map('map', options);
    // add tiles
    var tiles = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', {
        maxZoom: 22,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

})();