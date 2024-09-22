// This line waits for the DOM (Document Object Model) to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Select the header element
    const header = document.querySelector('.header');
    
    // Get the original offset position of the navbar
    const sticky = header.offsetTop;

    // Define the function that adds/removes the "sticky" class
    function stickyNavbar() {
        if (window.pageYOffset > sticky) {
            header.classList.add("sticky");
        } else {
            header.classList.remove("sticky");
        }
    }

    // Run the stickyNavbar function every time the user scrolls
    window.onscroll = function() {
        stickyNavbar();
    };
});