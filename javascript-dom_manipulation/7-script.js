const listMovies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    if (!response.ok) {
      throw new Error('Error en la petición: ' + response.status);
    }
    return response.json();
  })
  .then(function (data) {
    const films = data.results;

    films.forEach(function (film) {
      const li = document.createElement('li');
      li.textContent = film.title;
      listMovies.appendChild(li);
    });
  })
  .catch(function (error) {
    console.error('Error al cargar películas:', error);
  });
