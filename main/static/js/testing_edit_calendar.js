// Verifica si ya se selecciono un evento
let eventSelected = false

// Bloques de Eventos
const eventsBlocks = document.querySelectorAll('.event-block');
// Bloques en la agenda
const calendarBlocks = document.querySelectorAll('.calendar-block');

eventsBlocks.forEach((block) => block.addEventListener('dragstart', () => {
    SetEvent(block.dataset.id);
}))

eventsBlocks.forEach((block) => block.addEventListener('click', () => {
    SetEvent(block.dataset.id);
}))
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

calendarBlocks.forEach((block) => block.addEventListener('drop', () => {
    let day = block.dataset.day;
    let group = block.dataset.group;
    let division = block.dataset.division;
    SetLocation(day, group, division);
}))

calendarBlocks.forEach((block) => block.addEventListener('click', () => {
    let day = block.dataset.day;
    let group = block.dataset.group;
    let division = block.dataset.division;
    SetLocation(day, group, division);
}))

function SetEvent(id_event){
    // Para seleccionar un evento
    let event = document.getElementById('id_event');
    event.setAttribute('value', String(id_event));
    eventSelected = true;
}

function SetLocation(day, group, division){
    // Seleccionar la posición en la que se va a enviar el evento
    document.getElementById('id_day').value = day;
    document.getElementById('id_group').value = group;
    document.getElementById('id_division').value = division;
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