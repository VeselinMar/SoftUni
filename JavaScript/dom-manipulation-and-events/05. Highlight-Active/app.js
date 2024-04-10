// function focused() {
//     let focused = document.querySelectorAll('div > div');
    
//     for (div of focused) {
//     div.addEventListener('mouseenter', highlightOn);
//     div.addEventListener('mouseleave', highlightOff);
//     }

//     function highlightOn(event) {
//         let div = event.currentTarget;
//         div.classList.add('focused');


//     }

//     function highlightOff(event) {
//         let div = event.currentTarget;
//         div.classList.remove('focused');
//     }
// }

function focused() {
    let inputElements = document.querySelectorAll('input[type=text]');

    Array.from(inputElements).forEach(inputElement => inputElement.addEventListener('focus', (event) => {
        event.target.parentElement.classList.add('focused');
    }));

    Array.from(inputElements).forEach(inputElement => inputElement.addEventListener('blur', (event) => {
        event.target.parentElement.classList.remove('focused');
    }));
}
