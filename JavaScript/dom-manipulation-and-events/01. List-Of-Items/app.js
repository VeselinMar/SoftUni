function addItem() {
    const listToAddTo = document.getElementById('items');

    const newItemText = document.getElementById('newItemText').value;

    const newItem = document.createElement('li');

    newItem.textContent = newItemText;

    listToAddTo.appendChild(newItem);

    document.getElementById('newItemText').value = '';
}