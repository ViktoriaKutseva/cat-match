document.addEventListener('DOMContentLoaded', () => {
    // Вызываем getCats при загрузке страницы
    getCats();
});

async function getCats() {
    try {
        const response = await fetch('/api/cats');
        const data = await response.json();
        const cats = data["Так вот же они, на пригорочке"]; // Убедитесь, что ключ соответствует вашему JSON

        const container = document.getElementById("cat-container");
        container.innerHTML = '';

        cats.forEach(cat => {
            const catDiv = document.createElement("div");
            catDiv.className = "cat";
            catDiv.innerHTML = `
                <p>Имя: ${cat.name}</p>
                <p>Возраст: ${cat.age}</p>
                <p>Порода: ${cat.breed}</p>
                <p>Описание: ${cat.description}</p>
            `;
        const updateButton = document.createElement("button");
        updateButton.innerText = "Изменить кись";
        updateButton.onclick = () => updateCat(cat.id);

        const deleteButton = document.createElement("button");
        deleteButton.innerText = "Забрать котика";
        deleteButton.onclick = () => deleteCat(cat.id);

        catDiv.appendChild(updateButton);
        catDiv.appendChild(deleteButton);

        container.appendChild(catDiv);
        });
    } catch (error) {
        console.error("Ошибка при получении котов:", error);
    }
}

async function updateCat(catId) {
    const newName = prompt("Введите новое имя котика:");
    const newAge = prompt("Введите новый возраст котика:");
    const newBreed = prompt("Введите новую породу котика:");
    const newDescription = prompt("Введите новое описание котика:");

    try {
        const response = await fetch(`/api/cats/${catId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: newName,
                age: newAge,
                breed: newBreed,
                description: newDescription,
            }),
        });
        const data = await response.json();
        alert("Котик обновлен!");
        getCats(); // Обновляем список
    } catch (error) {
        console.error("Ошибка при обновлении котика:", error);
    }
}

async function deleteCat(catId) {
    const confirmDelete = confirm("Точно нашелся?");
    if (!confirmDelete) return;

    try {
        const response = await fetch(`/api/cats/${catId}`, {
            method: 'DELETE', 
        });
        const data = await response.json();
        alert("Котик взят");
        getCats();
    } catch (error) {
        console.error("Ошибка при пристроении котика", error);
    }
}
// document.addEventListener('DOMContentLoaded', () => {
//     // Вызываем getCats при загрузке страницы
//     getCats();
// });
// async function getCats() {
//     try {
//         const response = await fetch('/api/cats');
//         const data = await response.json();
//         console.log(data); // Проверка структуры данных

//         const catsList = data["Так вот же они, на пригорочке"];
        
//         if (Array.isArray(catsList)) {
//             const container = document.getElementById("cat-container");
//             container.innerHTML = catsList.map(cat => `
//                 <p><strong>Имя:</strong> ${cat.name}</p>
//                 <p><strong>Возраст:</strong> ${cat.age}</p>
//                 <p><strong>Порода:</strong> ${cat.breed}</p>
//                 <p><strong>Описание:</strong> ${cat.description}</p>
//                 <hr>
//             `).join('');
//         } else if (data["Гиде кисоньки???"]) {
//             console.warn("No cats found:", data["Гиде кисоньки???"]);
//             const container = document.getElementById("cat-container");
//             container.innerHTML = `<p>${data["Гиде кисоньки???"]}</p>`;
//         } else {
//             console.error("Unexpected response format:", data);
//         }
//     } catch (error) {
//         console.error("Error fetching cats:", error);
//     }
// }
