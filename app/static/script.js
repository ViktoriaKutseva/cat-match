document.addEventListener('DOMContentLoaded', () => {
    // Вызываем getCats при загрузке страницы
    getCats();
});
async function getCats() {
    try {
        const response = await fetch('/api/cats');
        const data = await response.json();
        console.log(data); // Проверка структуры данных

        const catsList = data["Так вот же они, на пригорочке"];
        
        if (Array.isArray(catsList)) {
            const container = document.getElementById("cat-container");
            container.innerHTML = catsList.map(cat => `
                <p><strong>Имя:</strong> ${cat.name}</p>
                <p><strong>Возраст:</strong> ${cat.age}</p>
                <p><strong>Порода:</strong> ${cat.breed}</p>
                <p><strong>Описание:</strong> ${cat.description}</p>
                <hr>
            `).join('');
        } else if (data["Гиде кисоньки???"]) {
            console.warn("No cats found:", data["Гиде кисоньки???"]);
            const container = document.getElementById("cat-container");
            container.innerHTML = `<p>${data["Гиде кисоньки???"]}</p>`;
        } else {
            console.error("Unexpected response format:", data);
        }
    } catch (error) {
        console.error("Error fetching cats:", error);
    }
}
