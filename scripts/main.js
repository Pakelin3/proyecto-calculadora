function loadContent(distribution) {
    const url = `./${distribution}.html`;

    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('body_page').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('body_page').innerHTML = '<p>Ha ocurrido un error al cargar el contenido.</p>';
        });
}
