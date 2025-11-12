// Verifica si ya se selecciono un evento
let eventSelected = false

// Bloques de Eventos
const eventsBlocks = document.querySelectorAll('.event-block');
// Bloques en la agenda
const calendarBlocks = document.querySelectorAll('.calendar-block');
/*
const deleteBlock = document.getElementById('delete-block');

deleteBlock.addEventListener('click', (e) => {
    let event = document.getElementById('id_event');
    event.setAttribute('value', String(deleteBlock.dataset.id));
    eventSelected = true;
})
*/
eventsBlocks.forEach((block) => {
    block.addEventListener('click', () => SetEvent(block));
    block.addEventListener('dragstart', () => SetEvent(block));
})
/*
// SE INTENTO AÑADIR DRAG AND DROP PARA MÓVILES (No se pudo)
eventsBlocks.forEach((block) => block.addEventListener('touchstart', e => {
    block.classList.add('in-movement');

    let touchLocation = e.changedTouches[0];

    block.style.left = `${touchLocation.pageX}px`;
    block.style.top = `${touchLocation.pageY}px`;
}))

eventsBlocks.forEach((block) => block.addEventListener('touchmove', e => {
    let touchLocation = e.changedTouches[0];

    block.style.left = `${touchLocation.pageX}px`;
    block.style.top = `${touchLocation.pageY}px`;
}))

eventsBlocks.forEach((block) => block.addEventListener('touchend', () => {
    block.classList.remove('in-movement');
}))
*/
calendarBlocks.forEach((block) => block.addEventListener('dragover', e => {
    e.preventDefault();
}))

calendarBlocks.forEach((block) => {
    block.addEventListener('drop', () => SetLocation(block));
    block.addEventListener('click', () => SetLocation(block));
})


function SetEvent(block) {
    // Para seleccionar un evento
    let event = document.getElementById('id_event');
    event.setAttribute('value', String(block.dataset.id));

    let info = document.querySelectorAll('.selected');

    info.forEach(item => {
        item.classList.remove('border');
        item.classList.remove('border-4');
        item.classList.remove('border-light');
        item.classList.remove('selected')
    })


    let img = block.getElementsByTagName('img')[0];
    img.classList.add('border');
    img.classList.add('border-4');
    img.classList.add('border-light');
    img.classList.add('selected')
    eventSelected = true;
}

function SetLocation(block) {
    // Seleccionar la posición en la que se va a enviar el evento
    document.getElementById('id_day').value = block.dataset.day;
    document.getElementById('id_group').value = block.dataset.group;
    document.getElementById('id_division').value = block.dataset.division;
    // También se va a enviar el formulario
    SendForm();
}

function SendForm() {
    // Checkeamos que se haya seleccionado un evento
    if (!eventSelected) {
        return;
    }

    // Se envia el formulario
    let form = document.getElementById('form-event_connector');
    form.submit();
}

let searchInput = document.getElementById('form-search')

searchInput.addEventListener('input', e => {
    Search();
})

function Search() {
    let input = document.getElementById('form-search')
    let filter = input.value.toUpperCase();
    eventsBlocks.forEach(block => {
        let txtValue = block.dataset.name.toUpperCase();
        console.log(txtValue.indexOf(filter));
        if ((txtValue.indexOf(filter) !== -1 || filter.trim() === "") || (block.id === "delete-block")) {
            block.classList.remove('hidden');
        } else {
            block.classList.add('hidden')
        }
    })
}


