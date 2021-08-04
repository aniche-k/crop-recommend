function weatherBalloon(lat,lon) {
  var key = '2c87673cbe9d4eb88fe151f5de7acdc5';
  var url='https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid='+key
  fetch(url)  
  .then(function(resp) { return resp.json() }) // Convert data to json
  .then(function(data) {
    console.log(data);
	document.getElementById("city").value=(JSON.stringify(data.name)).replace(/\"/g, "");
  })
  .catch(()=> {
    console.log("error");
  });
  console.log("Statements after script");
}
function success(pos){
	var cord=pos.coords;
	weatherBalloon(cord.latitude,cord.longitude);
}
function err(pos){
	alert("Live Location Unavailable. Please Enter The Name Of Your City");
}