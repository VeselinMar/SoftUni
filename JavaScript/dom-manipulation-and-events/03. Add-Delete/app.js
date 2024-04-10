function addItem() {
    let itemToBeAdded = document.getElementById("newItemText").value;
    let list = document.getElementById("items");

    if (itemToBeAdded.length === 0) return;

    let newItem = document.createElement("li");
    newItem.textContent = itemToBeAdded;
    
    let remove = document.createElement("a");
    let linkText = document.createTextNode("[Delete]");
    remove.appendChild(linkText);
    remove.href = "#";
    remove.addEventListener("click", deleteItem);

    newItem.appendChild(remove);
    list.appendChild(newItem);

    document.getElementById("newItemText").value = '';

    function deleteItem() {
        newItem.remove();
    }
}