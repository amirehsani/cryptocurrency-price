document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/coin_prices')
        .then(response => response.json())
        .then(data => {
            displayCoinPrices(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

function displayCoinPrices(coinPrices) {
    const coinList = document.getElementById('coin-list');
    coinList.innerHTML = '';

    for (const coin in coinPrices) {
        const listItem = document.createElement('li');
        listItem.textContent = `${coin}: ${coinPrices[coin]} USD`;
        coinList.appendChild(listItem);
    }
}
