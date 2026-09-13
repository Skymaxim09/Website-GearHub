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

// Change category slug (product list)
document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('categorySelect');
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            const slug = this.value;
            if (slug) {
                const pathOrigin = window.location.origin;
                const pathUrl = '/product-list--slug_placeholder'.replace('slug_placeholder', slug)

                window.location.replace(pathOrigin + pathUrl);
            }
        });
    }
});
