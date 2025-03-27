document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".slide");
    let currentIndex = 0;

    // Function to show a specific slide
    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.opacity = i === index ? "1" : "0"; // Fade effect
            slide.style.transition = "opacity 0.8s ease-in-out";
        });
    }

    // Function to go to the next slide
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    // Function to go to the previous slide
    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }

    // Auto-slide every 3 seconds
    let autoSlide = setInterval(nextSlide, 3000);

    // Add left & right navigation buttons
    const slider = document.querySelector(".slider");
    const prevButton = document.createElement("button");
    const nextButton = document.createElement("button");

    prevButton.innerHTML = "◀";
    nextButton.innerHTML = "▶";
    
    prevButton.classList.add("slider-button", "prev");
    nextButton.classList.add("slider-button", "next");

    slider.appendChild(prevButton);
    slider.appendChild(nextButton);

    // Click event for navigation
    prevButton.addEventListener("click", function () {
        clearInterval(autoSlide);
        prevSlide();
        autoSlide = setInterval(nextSlide, 3000); // Restart auto-slide
    });

    nextButton.addEventListener("click", function () {
        clearInterval(autoSlide);
        nextSlide();
        autoSlide = setInterval(nextSlide, 3000); // Restart auto-slide
    });

    // Show the first slide initially
    showSlide(currentIndex);
});
