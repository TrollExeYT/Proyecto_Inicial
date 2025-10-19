let eventSelected = false

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