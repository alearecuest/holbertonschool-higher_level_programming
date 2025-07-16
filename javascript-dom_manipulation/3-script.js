const header = document.querySelector('header');

const toggleButton = document.getElementById('toggle_header');

toggleButton.addEventListener('click', function () {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else {
    header.classList.remove('red');
    header.classList.add('green');
  }
});
