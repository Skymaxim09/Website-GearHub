function hoverDropDown() {
    const dropdowns = document.querySelectorAll('.navbar .dropdown');

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('mouseenter', () => {
            if (window.innerWidth >= 992) {
                let menu = dropdown.querySelector('.dropdown-menu');
                menu.classList.add("show");
            }
        });

        dropdown.addEventListener('mouseleave', () => {
            if (window.innerWidth >= 992) {
                let menu = dropdown.querySelector('.dropdown-menu');
                setTimeout(() => {
                    menu.classList.remove("show");
                }, 200);
            }
        });
    });
}

function antiDoubleSubmit() {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const buttons = this.querySelectorAll('button[type="submit"]');
            buttons.forEach(button => {
                button.disabled = true;
            });
        });
    });
}

antiDoubleSubmit();
document.addEventListener('DOMContentLoaded', hoverDropDown);