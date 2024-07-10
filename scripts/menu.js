const distributions = [
    "Binomial",
    "Normal",
    "Poisson",
    "Hipergeométrica"
];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function typeWriter() {
    const menu = document.getElementById('distribution-menu');
    const staticText = 'Calculadora de distribución - ';

    menu.textContent = '';
    for (let j = 0; j < staticText.length; j++) {
        menu.textContent += staticText.charAt(j);
        await sleep(175);
    }

    while (true) {
        for (let i = 0; i < distributions.length; i++) {
            const text = distributions[i];
            for (let j = 0; j < text.length; j++) {
                menu.textContent += text.charAt(j);
                await sleep(175);
            }
            await sleep(2000);
            for (let j = text.length; j > 0; j--) {
                menu.textContent = menu.textContent.slice(0, -1);
                await sleep(75);
            }
            await sleep(1000);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    typeWriter();
});
