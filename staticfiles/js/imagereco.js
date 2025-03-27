document.addEventListener("DOMContentLoaded", function () {
    // Search functionality
    const searchInput = document.querySelector(".search-input");
    const searchButtons = document.querySelectorAll(".search-button");
    const tableRows = document.querySelectorAll("tbody tr");
    
    searchButtons.forEach(button => {
        button.addEventListener("click", function () {
            const query = searchInput.value.toLowerCase();
            tableRows.forEach(row => {
                row.style.display = row.innerText.toLowerCase().includes(query) ? "" : "none";
            });
        });
    });

    // Image slider functionality
    let currentIndex = 0;
    const images = document.querySelectorAll("#sliderImage");
    const nextButton = document.createElement("button");
    nextButton.innerText = "▶";
    nextButton.classList.add("next-button");
    document.body.appendChild(nextButton);
    
    function showImage(index) {
        images.forEach((img, i) => {
            img.style.display = i === index ? "block" : "none";
        });
    }
    
    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }
    
    nextButton.addEventListener("click", nextImage);
    setInterval(nextImage, 3000); // Change image every 3 seconds
    showImage(currentIndex);

    // File upload functionality
    const fileInput = document.getElementById("fileInput");
    const uploadBtn = document.querySelector(".upload-btn");
    const cancelBtn = document.querySelector(".cancel-btn");
    const uploadArea = document.querySelector(".upload-area");
    
    fileInput.addEventListener("change", function () {
        const file = fileInput.files[0];
        if (file) {
            uploadArea.innerHTML = `<p>Selected file: ${file.name}</p>`;
        }
    });
    
    uploadBtn.addEventListener("click", function () {
        if (fileInput.files.length > 0) {
            alert("File uploaded successfully!");
        } else {
            alert("Please select a file first.");
        }
    });
    
    cancelBtn.addEventListener("click", function () {
        fileInput.value = "";
        uploadArea.innerHTML = `<span class="upload-icon">📤</span><p>Select a file or drag and drop here</p>`;
    });
});
