document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', toggleMenu)
})


function toggleMenu(e) {
    const btn = document.querySelector('.dropdown-btn')
    const dropdown = document.querySelector('.dropdown')
    if (!e.target.matches('button.dropdown-btn') && !dropdown.classList.contains('hidden')) {
        dropdown.classList.toggle('hidden')
    }

    if (e.target.matches('button.dropdown-btn')) {
        dropdown.classList.toggle('hidden')
    }
}