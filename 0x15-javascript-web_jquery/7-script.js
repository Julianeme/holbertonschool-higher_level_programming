$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('.result').html(data);
  $('#character').text(data.name);
});
