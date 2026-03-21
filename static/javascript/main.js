window.onload = () => {
    checkForSubmits()
    loadImgs()
}
document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', toggleMenu)
    document.addEventListener('click', toggleTabs)
})

// toggles more buttons on navbar in base.html
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

// for switching tabs on video.html
function toggleTabs(e) {
    if (!e.target.matches('button.tab-btn')) return

    const btns = document.querySelectorAll('.tab-btn')
    if (e.target.matches('button.tab-btn.active')) return

    const selectedBtn = e.target.closest('.tab-btn')
    const id = selectedBtn.dataset.target
    const tabs = document.querySelectorAll('.tab-content')
    tabs.forEach((tab) => {
        if (!tab.classList.contains('hidden')) {
            tab.classList.add('hidden')
        }
    })

    btns.forEach((btn) => {
        if (btn.classList.contains('active')) {
            btn.classList.remove('active')
        }
    })
    selectedBtn.classList.add('active')

    const selectedContent = document.querySelector(id)
    selectedContent.classList.remove('hidden')

}


// function handleLoader() {
//     const loader = document.querySelector('.loader-overlay')
//     const content = document.querySelector('.content')
//     loader.style.display = 'none'
//     content.classList.remove('hidden')
//     content.classList.add('flex-column')
// }

function loadImgs() {
    const body = document.querySelector('body')
    body.classList.add('loaded')
}

function checkForSubmits() {
const params = new URLSearchParams(window.location.search);
if (params.get("submitted") === "true") {
  showThanxMsg()
}
}

function showThanxMsg() {
    console.log("Hi mom")
    const form = document.querySelector('.contact-container')
    const msg = document.querySelector('.thanx-msg')

    form.classList.remove('flex-column')
    form.classList.add("hidden")
    msg.classList.add('flex-column')
    msg.classList.remove('hidden')
}




// Logs elements that are too wide. 
// [...document.querySelectorAll("*")].forEach(el => {
//   if (el.scrollWidth > document.documentElement.clientWidth) {
//     console.log(el);
//   }
// });