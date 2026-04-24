document.addEventListener('keydown', function(event){
    console.log(`Tecla Presionada: ${event.key}`);
    console.log(`Codigo tecla: ${event.code}`);
    fetch('/lectura', {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
        },
        body: JSON.stringify({
            tecla: event.key
        }),
    })
    .then(response => response.json())
    .then(data => console.log(data));
});