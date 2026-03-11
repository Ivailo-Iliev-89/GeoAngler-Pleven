document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const content = dropdown.querySelector('.dropdown-content');
        let timeout;

        dropdown.addEventListener('mouseenter', function() {
            clearTimeout(timeout);
            content.classList.add('show');
        });

        dropdown.addEventListener('mouseleave', function() {
            timeout = setTimeout(() => {
                content.classList.remove('show');
            }, 500); 
        });
    });
});