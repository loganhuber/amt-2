document.addEventListener('DOMContentLoaded', () => {

    document.addEventListener('click', handleShowInfo)

})



function handleShowInfo(e) {
    const btn = e.target.closest('.info-btn')
    if (!btn) return

    const venue = document.getElementById('info-venue')
    venue.textContent = btn.dataset.venue

    const ticketLink = document.getElementById('info-ticket-link')
    const getTickets = document.getElementById('get-tickets')
    const ticketsAtDoor = document.getElementById('tickets-at-door')
    if (btn.dataset.link) {
        getTickets.style.display = ''
        ticketsAtDoor.style.display = 'none'
        ticketLink.href = btn.dataset.link
    } 
    if (btn.dataset.link == 'None') {
        ticketsAtDoor.style.display = ''
        getTickets.style.display = 'none'
    }

    const description = document.getElementById('info-description')
    description.textContent = btn.dataset.description

    const flyer = document.getElementById('show-flyer')
    flyer.src = btn.dataset.image

}