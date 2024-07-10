// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function () {
    // Función para crear una estrella y añadirla al contenedor
    function createStar(container) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.width = `${randomInRange(1, 4)}px`;
        star.style.height = star.style.width;
        star.style.top = `${randomInRange(0, 100)}%`;
        star.style.left = `${randomInRange(0, 100)}%`;
        container.appendChild(star);

        // Animación de movimiento hacia arriba
        const duration = randomInRange(20, 3); // Duración aleatoria en segundos
        star.style.animation = `moveStar ${duration}s linear infinite`;

        return star;
    }

    // Función para inicializar el fondo de estrellas
    function initStarsBackground() {
        const container = document.getElementById('stars-container');
        if (!container) {
            console.error('Container not found.');
            return;
        }

        // Crear el número especificado de estrellas
        for (let i = 0; i < 300; i++) { // Cambia el número de estrellas aquí si es necesario
            createStar(container);
        }
    }

    // Inicializar el fondo de estrellas
    initStarsBackground();
});

// Función para generar un número aleatorio dentro de un rango
function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
}
