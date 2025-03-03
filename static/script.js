document.addEventListener("DOMContentLoaded", function () {
    // Clear prediction result when page reloads
    if (performance.navigation.type === 1) {
        let resultDiv = document.querySelector(".result");
        if (resultDiv) {
            resultDiv.style.display = "none";
        }
    }
});
