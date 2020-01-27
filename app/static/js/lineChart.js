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

    $.get('/lastfive', function (setData) {
        return setData;
    });
    var json_data = $.get();
    var result = [];
    for (var i in json_data)
        result.push([i, json_data [i]]);

    var data = google.visualization.arrayToDataTable(result);

    var options = {
        title: 'Stats (Last 5 minutes)',
        curveType: 'function',
        legend: {position: 'bottom'}
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

    chart.draw(data, options);

}