displayLoadMsg()

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(handleLoader, 2000)
    
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



function displayLoadMsg() {
    const msgs = ['loading...', "I'm working on it...", "Dude, just wait a sec..", "gimme a sec pls..."]
    const index = Math.floor(Math.random() * msgs.length)
    const el = document.getElementById('loader-msg')
    el.textContent = msgs[index]
}


function handleLoader() {
    const loader = document.querySelector('.loader-overlay')
    const content = document.querySelector('.content')
    loader.style.display = 'none'
    content.classList.remove('hidden')
    content.classList.add('flex-column')
}