function populate_table(url) {
    google.charts.load('visualization', '1.0', {
        'packages': ['table']
    }).then(function() {
        $.ajax({
            url: url
        }).done(function(jsonData) {
            var data = new google.visualization.DataTable();

            columns = [];
            //Add Column Names
            for (var atr in jsonData[0]) {
                columns.push(atr)
                data.addColumn('string', atr)
            }

            // Add rows by volumn value
            $.each(jsonData, function(index, row) {
                newRow = [];
                for (var col in columns) {
                    newRow.push(String(row[columns[col]]))
                }
                data.addRow(newRow)
            });

            var options = {
                showRowNumber: true,
                width: '100%',
                height: '100%',
                page: 'enable',
                pageSize: 20
            };

            var chart = new google.visualization.Table(document.getElementById('data-table'));
            chart.draw(data, options);
        });
    });
}

// If all-values buttons are clicked
$("#song-btn").click(function() {
    populate_table("http://127.0.0.1:8080/song")
});

$("#artist-btn").click(function() {
    populate_table("http://127.0.0.1:8080/artist")
});

$("#feature-btn").click(function() {
    populate_table("http://127.0.0.1:8080/songfeature")
});



// If artist input changes disable song input and vice versa
$("#artist-input").on('input', function() {
    $("#song-input").prop("disabled", true);
    $("#genre-input").prop("disabled", true);

});
$("#song-input").on('input', function() {
    $("#artist-input").prop("disabled", true);
    $("#genre-input").prop("disabled", true);
    $("#artist-radio").prop('disabled', true);
    $("#search-btn").prop("disabled", true);
    $("#song-radio").toggle("highlight");
});
$("#genre-input").on('input', function() {
    $("#artist-input").prop("disabled", true);
    $("#song-input").prop("disabled", true);
});

$("#song-radio").click(function() {
    $("#search-btn").prop("disabled", false);
});




$("#search-btn").click(function() {

    filterVal = $('input[name=filter-radio]:checked').val();
    if ($("#artist-input").is(':enabled')) {
        //Run search on song input and generate table
        if (filterVal == "artist") {
            populate_table("http://127.0.0.1:8080/artist/filter?name=" + $("#artist-input").val())
        }
        if (filterVal == "song") {
            populate_table("http://127.0.0.1:8080/song/filter?artist=" + $("#artist-input").val())
        }
        if (filterVal == "songfeature") {
            populate_table("http://127.0.0.1:8080/songfeature/filter?artist=" + $("#artist-input").val())

        }

    }

    if ($("#song-input").is(':enabled')) {
        filterVal = $('input[name=filter-radio]:checked').val();
        if (filterVal == "song") {
            populate_table("http://127.0.0.1:8080/song/filter?name=" + $("#song-input").val())
        }
        if (filterVal == "songfeature") {
            populate_table("http://127.0.0.1:8080/songfeature/filter?name=" + $("#song-input").val())

        }
    }

    if ($("#genre-input").is(':enabled')) {
        filterVal = $('input[name=filter-radio]:checked').val();
        if (filterVal == "artist") {
            populate_table("http://127.0.0.1:8080/artist/filter?genre=" + $("#genre-input").val())
        }
        if (filterVal == "song") {
            populate_table("http://127.0.0.1:8080/song/filter?genre=" + $("#genre-input").val())
        }
        if (filterVal == "songfeature") {
            populate_table("http://127.0.0.1:8080/songfeature/filter?genre=" + $("#genre-input").val())

        }
    }

    $("#song-input").prop('disabled', false)
    $("#genre-input").prop('disabled', false)
    $("#artist-input").prop('disabled', false)

});
