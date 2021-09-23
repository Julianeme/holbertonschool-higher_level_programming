$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('.result').html(data);
  let i = 0;
  for (i in data.results) {
    $('#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
