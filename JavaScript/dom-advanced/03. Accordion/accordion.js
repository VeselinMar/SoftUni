function toggle() {
    const toggleButton = document.querySelector('.head span.button');
    const extraInformationElement = document.getElementById('extra');
    
    if (toggleButton.textContent === 'More') {
        extraInformationElement.style.display = 'block';
        toggleButton.textContent = 'Less';
    }
    else {
        extraInformationElement.style.display = 'none';
        toggleButton.textContent = 'More';
    }
}
