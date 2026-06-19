// Shared site behavior: footer year + mobile nav toggle.
(function () {
  var yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();

  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
  }
})();
