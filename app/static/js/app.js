document.addEventListener('DOMContentLoaded', function () {
  const scrollToTopButton = document.getElementById('scrollToTop');
  window.addEventListener('scroll', function () {

      if (window.scrollY > 200) { 
          if (scrollToTopButton.style.display === 'none' || !scrollToTopButton.style.display) {
              scrollToTopButton.style.display = 'block';
          }
      } else {
          if (scrollToTopButton.style.display === 'block') {
              scrollToTopButton.style.display = 'none';
          }
      }
  });

  scrollToTopButton.addEventListener('click', function (event) {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});

//disparition du menu déroulant au clic
let navlinks = document.querySelectorAll(".nav-link");
let sousmenu = document.querySelector("#toggleMobileMenu");

navlinks.forEach((link) => {
  link.addEventListener("click", () => sousmenu.classList.remove("show"));
});

