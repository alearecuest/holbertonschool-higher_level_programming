const updateButton = document.getElementById('update_header');
const header = document.querySelector('header');

updateButton.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});