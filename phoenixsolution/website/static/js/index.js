const hamburger = document.querySelector('.header .nav-bar .nav-list .hamburger');
const mobile_menu = document.querySelector('.header .nav-bar .nav-list ul');
const menu_item = document.querySelectorAll('.header .nav-bar .nav-list ul li a');
const header = document.querySelector('.header');

// Función para actualizar el color de fondo del header según la posición de scroll
const updateHeaderBackground = () => {
    const scroll_position = window.scrollY;
    if (scroll_position > 100) {
        header.style.backgroundColor = 'rgba(23, 6, 0, 0.54)';
    } else {
        header.style.backgroundColor = 'transparent';
    }
};

// Agregar evento al botón de menú (hamburger)
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    mobile_menu.classList.toggle('active');
});

// Ejecutar la función al cargar la página y al hacer scroll
document.addEventListener('DOMContentLoaded', updateHeaderBackground);
document.addEventListener('scroll', updateHeaderBackground);

// Cerrar el menú móvil al hacer clic en cualquier elemento del menú
menu_item.forEach((item) => {
    item.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobile_menu.classList.toggle('active');
    });
});

//CARDS
function openModal(id) {
    const modal = document.getElementById(`modal-${id}`);
    modal.style.display = "flex";
}

function closeModal(id) {
    const modal = document.getElementById(`modal-${id}`);
    modal.style.display = "none";
}

// Cierra el modal al hacer clic fuera de él
window.onclick = function (event) {
    const modals = document.querySelectorAll(".modal");
    modals.forEach((modal) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};

let miembros = document.querySelectorAll('.miembro');
let currentIndex = 0;

function showNextMiembro() {
    miembros[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % miembros.length;
    miembros[currentIndex].classList.add('active');
}

if (miembros.length > 0) {
    miembros[currentIndex].classList.add('active');
}

setInterval(showNextMiembro, 5000);

document.querySelector('#contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    e.target.elements.name.value = '';
    e.target.elements.email.value = '';
    e.target.elements.message.value = '';
  });
