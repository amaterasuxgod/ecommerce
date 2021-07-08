const btn2 = document.getElementById("mobile-nav-close");
const btn1 = document.getElementById("mobile-nav");
const nav1 = document.getElementById("container-mob");


btn1.addEventListener("click", () => {
    nav1.classList.add("mobile-nav-content-show");
    nav1.style.transition = 'all 1s ease-in-out 1s';
    btn1.style.display = 'none';
    btn2.style.display = 'block';
});

btn2.addEventListener("click", () => {
    nav1.classList.remove("mobile-nav-content-show");
    btn1.style.display = 'block';
    btn2.style.display = 'none';
});




