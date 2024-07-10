$(document).ready(function () {
    function animateTypewriter(element) {
        const text = element.textContent.trim();
        element.textContent = '';
        let index = 0;
        const intervalId = setInterval(function () {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
            } else {
                clearInterval(intervalId);
            }
        }, 100);
    }
    const descriptionElements = document.querySelectorAll('#description');

    descriptionElements.forEach(function (element) {
        animateTypewriter(element);
    });
});