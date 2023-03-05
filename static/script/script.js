function updateTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    var timeString = hours + ":" + minutes + ":" + seconds;
    document.getElementById("clock").innerHTML = timeString;
}
setInterval(updateTime, 1000);

fetch('https://api.openweathermap.org/data/2.5/weather?q=ubon ratchathani&appid=0bddcc3609d450dc7d5264d45b10ab09')
.then(respon => respon.json())
.then(data => {
  var des = data['weather'][0]['description']
  var tem = data['main']['temp'] - 273.15
  var data_tem = `${tem.toFixed(2)}°C / ${des}`
  document.getElementById('data_tem').innerHTML = data_tem
})

$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        var name = $('#nameInput').val();
        $.ajax({
            type: 'POST',
            url: '/process',
            data: {name: name},
            success: function(data) {
                $('#my-image').attr('src', data.image_url);
                $('#successAlert').text(data.name).show();
            }
        });
    });
});
