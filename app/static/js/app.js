//apparition de l'icone pour remonter en haut de la page
const UpBtn = document.querySelector("#goTopPage");

window.addEventListener("scroll", () => {
  if (window.scrollY > 700) {
    UpBtn.classList.remove("invisible");
  } else {
    UpBtn.classList.add("invisible");
  }
});

//disparition du menu déroulant au clic
let navlinks = document.querySelectorAll(".nav-link");
let sousmenu = document.querySelector("#toggleMobileMenu");

navlinks.forEach((link) => {
  link.addEventListener("click", () => sousmenu.classList.remove("show"));
});

const titre = document.querySelector(".moreInfos");
if (window.innerWidth >= 768) {
  titre.classList.add("hidden");
}
