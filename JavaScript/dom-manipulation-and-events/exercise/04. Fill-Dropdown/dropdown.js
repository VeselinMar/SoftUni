function addItem() {
        const text = document.getElementById("newItemText").value;
        const value = document.getElementById("newItemValue").value;
        const menuDiv = document.getElementById("menu");

        const newOption = document.createElement("option");
        newOption.textContent = text;
        newOption.value = value;

        menuDiv.appendChild(newOption);

        document.getElementById("newItemText").value = '';
        document.getElementById("newItemValue").value = '';
}
