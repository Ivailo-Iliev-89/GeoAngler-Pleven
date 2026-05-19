document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const content = dropdown.querySelector('.dropdown-content');
        let timeout;

        dropdown.addEventListener('mouseenter', function() {
            if (window.innerWidth > 768) {
                clearTimeout(timeout);
                content.classList.add('show');
            }
        });
        
        dropdown.addEventListener('mouseleave', function() {
            if (window.innerWidth > 768) {
                timeout = setTimeout(() => {
                    content.classList.remove('show');
                }, 500); 
            }
        });
    });
});

/* -- Плавното показване на Формата за Излета -- */
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("toggleFormBtn");
    const cancelBtn = document.getElementById("cancelFormBtn");
    const formContainer = document.getElementById("collapsibleFormContainer");
    const formAnchor = document.getElementById("form-anchor-target");

    function toggleFishingForm() {
        if (!formContainer) return; 

        if (formContainer.style.display === "none" || formContainer.style.display === "") {
            formContainer.style.display = "block";
            formContainer.style.opacity = "0";
            
            setTimeout(() => { 
                formContainer.style.opacity = "1"; 
            }, 5);
            
            toggleBtn.innerHTML = " Скрий ";
            toggleBtn.classList.add("btn-cancel");
            
            setTimeout(() => {
                formAnchor.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 100);
            
        } else {
            formContainer.style.opacity = "0";
            
            setTimeout(() => { 
                formContainer.style.display = "none"; 
            }, 400);
            
            toggleBtn.innerHTML = " Сподели излет ";
            toggleBtn.classList.remove("btn-cancel");
        }
    }

    if (toggleBtn) toggleBtn.addEventListener("click", toggleFishingForm);
    if (cancelBtn) cancelBtn.addEventListener("click", toggleFishingForm);
});