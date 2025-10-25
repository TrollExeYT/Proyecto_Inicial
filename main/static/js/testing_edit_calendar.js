// Verifica si ya se selecciono un evento
let eventSelected = false

// Bloques de Eventos
const eventsBlocks = document.querySelectorAll('.event-block');
// Bloques en la agenda
const calendarBlocks = document.querySelectorAll('.calendar-block');

eventsBlocks.forEach((block) => block.addEventListener('dragstart', e => {
    SetEvent(block.dataset.id);
}))

calendarBlocks.forEach((block) => block.addEventListener('dragover', e => {
    e.preventDefault();
}))

calendarBlocks.forEach((block) => block.addEventListener('drop', e => {
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
    // Selecionar la posicion en la que se va a enviar el evento
    document.getElementById('id_day').value = day;
    document.getElementById('id_group').value = group;
    document.getElementById('id_division').value = division;
    // Tambien se va a enviar el formulario
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