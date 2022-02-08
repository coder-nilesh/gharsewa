const hamburger = document.querySelector('.hamburger-btn');
const nav = document.querySelector('.nav-bar');

hamburger.addEventListener("click", ()=>{
    nav.classList.toggle("open");
    hamburger.classList.toggle("rotate");
})


const searchBtn = document.querySelector(".service-search-btn");
searchBtn.addEventListener("click",()=>{
    var input, filter, cards, cardContainer, title, i;
    input = document.getElementById("search-input");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("service-list");
    cards = cardContainer.getElementsByClassName("service-list-card");
    for (i = 0; i < cards.length; i++) {
      title = cards[i].querySelector(".service-name");
      if (title.innerText.toUpperCase().indexOf(filter) > -1) {
        cards[i].style.display = "";
      } else {
        cards[i].style.display = "none";
      }
    }
})


