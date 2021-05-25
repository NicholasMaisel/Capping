function populate_hist(column, div, genre = null, color = null) {
    google.charts.load('visualization', '1.0', {
        'packages': ['corechart']
    }).then(function() {
        url = 'http://127.0.0.1:8080/songfeature';
        if(genre !== null){
          url = url + '/filter?genre=' + genre
          genre = " " + genre
        } else {
          genre = ""
        }
        $.ajax({
            url: url
        }).done(function(jsonData) {
            var data = new google.visualization.DataTable();
            data.addColumn('number', column)
            // Add rows by volumn value
            $.each(jsonData, function(index, row) {
                newRow = [];
                newRow.push(row[column])
                data.addRow(newRow)
            });


            var options = {
                title: 'Distribution of ' + column + genre,
                legend: { position: 'none' },
                numBucketsRule: 'sturges',
                colors: [color],
            },
            hAxis= {
              title: "helo"
            }

            var chart = new google.visualization.Histogram(document.getElementById(div));
            chart.draw(data, options);
        });
    });
}


$('#feature-combo').on('change', function() {
  var feature_selected = $('#feature-combo').find(":selected").text();
  populate_hist(feature_selected,'data-hist',null,'blue');
  populate_hist(feature_selected,'rock-hist', 'Rock', 'red');
  populate_hist(feature_selected,'pop-hist', 'Pop','orange');
  populate_hist(feature_selected,'edm-hist', 'EDM','green');
  populate_hist(feature_selected,'hop-hist', 'Hop','purple');
  populate_hist(feature_selected,'country-hist', 'Country','brown');
  populate_hist(feature_selected,'jazz-hist', 'Jazz','lightblue');
  populate_hist(feature_selected,'classical-hist', 'Classical','black');

});
