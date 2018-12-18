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

    drawLegend();
    drawSlider();

    function drawLegend() {
        // generate legend via leaflet
        var legendControl = L.control({
            position: 'topright'
        });
        // add to Map
        legendControl.onAdd = function(map) {
            // create new DOM element for id=legend
            var legend = L.DomUtil.create('div', 'legend');
            return legend;
        };
        // add legent element to map
        legendControl.addTo(map);

        // add legend title
        var legend = $('.legend').html('<h3><span>2018</span> Crime Types</h3><ul>');

    };

    function drawSlider() {
        // create Leaflet control for slider
        var sliderControl = L.control({
            position: 'bottomleft'
        });
        // define the ui-control within the DOM
        sliderControl.onAdd = function(map) {
            // use the defined ui-control element
            var slider = L.DomUtil.get("ui-controls");
            // disable scrolling
            L.DomEvent.disableScrollPropagation(slider);
            // diable click events
            L.DomEvent.disableClickPropagation(slider);
            return slider;
        };
        // add control to map
        sliderControl.addTo(map);

    };
})();