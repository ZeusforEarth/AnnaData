document.addEventListener("DOMContentLoaded", function () {
    const image = document.querySelector(".image-container img");
    const title = document.querySelector(".title");
    const description = document.querySelector(".description");
    const body = document.body;

    // Add tooltip on hover
    image.setAttribute("title", "Click to enlarge");

    // Image click effect: enlarge on click, reset after 1s
    image.addEventListener("click", function () {
        this.style.transform = "scale(1.2)";
        this.style.transition = "transform 0.5s ease-in-out";
        setTimeout(() => {
            this.style.transform = "scale(1)";
        }, 1000);
    });

    // Fade-in animation
    title.style.opacity = "0";
    description.style.opacity = "0";
    image.style.opacity = "0";

    setTimeout(() => {
        title.style.transition = "opacity 1s ease-in-out";
        description.style.transition = "opacity 1s ease-in-out";
        image.style.transition = "opacity 1s ease-in-out";
        title.style.opacity = "1";
        description.style.opacity = "1";
        image.style.opacity = "1";
    }, 500);

    
    // Sample Searchable Data (You can expand this dynamically)
    const pages = [
        { url: "index.html", content: "Home Page, Agriculture, Farming" },
        { url: "imagereco.html", content: "Image Recognition, AI, Crop Detection" },
        { url: "plantpartnerint.html", content: "Inter Cropping, Plant Partner, Companion Planting" },
        { url: "crop1.html", content: "Crop, Growth, Soil, Farming Techniques" },
        { url: "about.html", content: "About Us, Team, Contact, Agriculture Information" }
    ];

    // Function to Search Across Pages
    function performGlobalSearch() {
        const query = searchInput.value.trim().toLowerCase();
        searchResults.innerHTML = ""; // Clear previous results

        if (query === "") {
            alert("Please enter a search term.");
            return;
        }

        let resultsFound = false;

        pages.forEach(page => {
            if (page.content.toLowerCase().includes(query)) {
                resultsFound = true;
                const resultItem = document.createElement("div");
                resultItem.innerHTML = `<a href="${page.url}" target="_blank">${page.url}</a>`;
                searchResults.appendChild(resultItem);
            }
        });

        if (!resultsFound) {
            searchResults.innerHTML = "<p>No results found.</p>";
        }
    }

    // Search Button Click Event
    searchButton.addEventListener("click", performGlobalSearch);

    // Enable "Enter" Key Search
    searchInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            performGlobalSearch();
        }
    });
});
