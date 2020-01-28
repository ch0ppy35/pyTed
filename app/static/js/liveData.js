var opts = {
    angle: 0.15, // The span of the gauge arc
    lineWidth: 0.49, // The line thickness
    radiusScale: 0.92, // Relative radius
    pointer: {
        length: 0.76, // // Relative to gauge radius
        strokeWidth: 0.035, // The thickness
        color: '#8A8A8A' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#96cfcc',   // Colors
    colorStop: '#55d459',    // just experiment with them
    strokeColor: '#a1a1a1',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support

};
var target = document.getElementById('gauge'); // your canvas element
var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
gauge.maxValue = 18; // set max gauge value
gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
gauge.animationSpeed = 32; // set animation speed (32 is default value)

$.get('/rtkw', function (data) {
    gauge.set(data);
});


setInterval(function () { // load the data from your endpoint into the div
    $.get('/rtkw', function (data) {
        $("#rtkw").replaceWith("<div id='rtkw'>" + data + " kW</div>")
        gauge.set(data); // set actual value
    });
}, 30000)