document.addEventListener('DOMContentLoaded', function () {
  const helloDiv = document.getElementById('hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(function (response) {
      if (!response.ok) {
        throw new Error('Error en la petición: ' + response.status);
      }
      return response.json();
    })
    .then(function (data) {
      helloDiv.textContent = data.hello;
    })
    .catch(function (error) {
      console.error('Error al obtener el saludo:', error);
      helloDiv.textContent = 'Error al cargar saludo';
    });
});