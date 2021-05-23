
$(document).ready(function(){
  const apiPath = "http://127.0.0.1:8080/NicholasMaisel/MusicCapping/1.0.0/songfeature";
  $.get(apiPath, function(data) {
    console.log(data)
    create_radar(JSON.parse(data))
  });
});
function create_radar(data){
  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
  type: 'radar',
  data: {
    labels: Object.keys(data[0]),
    datasets: [{
      label: 'My First Dataset',
      data: Object.values(data[0]),
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }]
  }
});

}
