// document.addEventListener('DOMContentLoaded', () => {
    
// })
async function getCats() {
    const response = await fetch('/cats'); 
    console.log(response); // Make sure the path corresponds to your FastAPI route
    const data = await response.json();
    console.log(data); // See full response in console

    // Access the list of cats using the correct key
    const catsList = data["Так вот же они, на пригорочке"];

    // Display cats in the HTML container
    const container = document.getElementById("cat-container");
    container.innerHTML = catsList.map(cat => `<p>${cat.name}</p>`).join('');
}