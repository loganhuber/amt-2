// checks if url contains ?submitted=true
function formSubmitted() {
    const params = new URLSearchParams(window.location.search);
    return params.get("submitted") === "true"
}

// hides form, shows msg
function showThanxMsg() {
    console.log("Hi mom")
    const form = document.querySelector('.contact-container')
    const msg = document.querySelector('.thanx-msg')

    form.classList.remove('flex-column')
    form.classList.add("hidden")
    msg.classList.add('flex-column')
    msg.classList.remove('hidden')
}

function main() {
    if (formSubmitted()) {
        showThanxMsg()
    }
}

main()