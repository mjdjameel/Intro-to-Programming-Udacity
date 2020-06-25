// Select color input
// Select size input
const color = document.getElementById('colorPicker');
const pixelCanvas = document.getElementById('pixelCanvas');
const sizePicker = document.getElementById('sizePicker');

// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', function(event){
    pixelCanvas.innerHTML = '';
    event.preventDefault();
    makeGrid();
});

function makeGrid() {
    const Height = document.getElementById('inputHeight').value;
    const Width = document.getElementById('inputWidth').value;

    for (let i = 0 ; i < Height; i++){
        let row = pixelCanvas.insertRow(i);
        for (let j = 0; j < Width; j++){
            let cell = row.insertCell(j);
        } 
    }
}

pixelCanvas.addEventListener('click', function(event){
    if (event.target.nodeName === 'TD'){
        event.target.style.backgroundColor = color.value;
    }
});



