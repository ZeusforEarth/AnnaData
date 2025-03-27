document.addEventListener("DOMContentLoaded", function () {
    const mainSearchButton = document.getElementById("search-btn");
    const mainSearchInput = document.getElementById("search");
    
    if (mainSearchButton && mainSearchInput) {
        function performSearch() {
            let searchText = mainSearchInput.value.trim();
            if (searchText !== "") {
                // Redirect to search page with query parameter
                window.location.href = `/MixedFarming/intercropping/?search=${encodeURIComponent(searchText)}`;
            } else {
                alert("Please enter a search term.");
            }
        }

        mainSearchButton.addEventListener("click", performSearch);

        // "Enter" Key Press for Searching
        mainSearchInput.addEventListener("keyup", function (event) {
            if (event.key === "Enter") {
                performSearch();
            }
        });
    }
});