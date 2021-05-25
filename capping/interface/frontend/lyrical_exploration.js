$("#search-btn").on('click', function(){
  songName = "song="+ $("#song-input").val() + "&"
  artistName = "artist=" + $("#artist-input").val()
  url = "http://127.0.0.1:8080/predict/lyrics/input?" + songName + artistName
  console.log(url)
  $.ajax({
      url: url
  }).done(function(jsonData) {
    console.log(jsonData)
    $("#predicted-genre").html("Predicted Genre: " + jsonData);
  });
});
