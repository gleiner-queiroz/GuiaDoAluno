const quotes = [
    "Acredite em si mesmo e tudo será possível.",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
    "Seja a mudança que você deseja ver no mundo.",
    "Nunca desista de um sonho só por causa do tempo que levará para realizá-lo. O tempo vai passar de qualquer forma."
];

function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}

window.onload = function() {
    const quoteElement = document.querySelector('.motivation-quote p');
    if (quoteElement) {
        quoteElement.textContent = getRandomQuote();
    }
};