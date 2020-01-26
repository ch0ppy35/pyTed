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
    colorStart: '#0CCF3A',   // Colors
    colorStop: '#78DA16',    // just experiment with them
    strokeColor: '#E0E0E0',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support

};
var target = document.getElementById('gauge'); // your canvas element
var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
gauge.maxValue = 100; // set max gauge value
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