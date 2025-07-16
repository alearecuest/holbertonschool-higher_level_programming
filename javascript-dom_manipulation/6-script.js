const characterDiv = document.getElementById('character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(function (response) {
    if (!response.ok) {
      throw new Error('Error en la petición: ' + response.status);
    }
    return response.json();
  })
  .then(function (data) {
    characterDiv.textContent = data.name;
  })
  .catch(function (error) {
    console.error('Hubo un problema con fetch:', error.message);
  });
