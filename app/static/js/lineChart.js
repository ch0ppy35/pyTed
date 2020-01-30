google.charts.load('current', {'packages': ['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    /*    var data = google.visualization.arrayToDataTable([
            ['Year', 'Sales', 'Expenses'],
            ['2004', 1000, 400],
            ['2005', 1170, 460],
            ['2006', 660, 1120],
            ['2007', 1030, 540]
        ]);*/


    $.getJSON('/lastfive', function (dataq) {
        // var columns = ['ts', 'Voltage', 'killawatts'];
        // var result = JSON.parse(dataq).map(function (obj) {
        //     return columns.map(function (key) {
        //         return obj[key];
        //     });
        // });
        // result.unshift(columns);
        console.log(dataq);
        var arr = $.map(dataq, function(el) { return el });
        console.log(arr)

        var data = google.visualization.arrayToDataTable(arr);

        var options = {
            title: 'Stats (Last 5 minutes)',
            curveType: 'function',
            legend: {position: 'bottom'}
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
    });


}