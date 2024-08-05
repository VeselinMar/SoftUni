function solve() {
    const textareaInputElement = document.querySelector('#exercise textarea:first-of-type');
    const textareaOutputElement = document.querySelector('#exercise textarea:last-of-type');
    const generateButtonElement = document.querySelector('#exercise button:first-of-type');
    const buyButtonElement = document.querySelector('#exercise button:last-of-type');
    const furnitureTbodyElement = document.querySelector('.table tbody')

    //parse input
    generateButtonElement.addEventListener('click', (e) => {
        const furnitures = JSON.parse(textareaInputElement.value);

        for (const furniture of furnitures) {
            const imgElement = document.createElement('img');
            imgElement.src = furniture.img;
            const imageTdElement = document.createElement('td');
            imageTdElement.appendChild(imgElement)

            const namePElement = document.createElement('p');
            namePElement.textContent = furniture.name;
            const nameTdElement = document.createElement('td');
            nameTdElement.appendChild(namePElement)

            const pricePElement = document.createElement('p');
            pricePElement.textContent = furniture.price;
            const priceTdElement = document.createElement('td');
            priceTdElement.appendChild(pricePElement)

            const decPElement = document.createElement('p');
            decPElement.textContent = furniture.decFactor;
            const decTdElement = document.createElement('td');
            decTdElement.appendChild(decPElement)

            const markElement = document.createElement('input');
            markElement.setAttribute('type', 'checkbox');
            const markTdElement = document.createElement('td');
            markTdElement.appendChild(markElement);

            const furnitureTrElement = document.createElement('tr');
            furnitureTrElement.appendChild(imageTdElement);
            furnitureTrElement.appendChild(nameTdElement);
            furnitureTrElement.appendChild(priceTdElement);
            furnitureTrElement.appendChild(decTdElement);
            furnitureTrElement.appendChild(markTdElement);

            furnitureTbodyElement.appendChild(furnitureTrElement);

        }
    })
    buyButtonElement.addEventListener('click', () => {
        let checkedFurnitureItems = [];
        let totalPrice = 0;
        let totalDecFactor = 0;
        let averageDecFactor = 0;
    
        const rows = furnitureTbodyElement.children;
    

        for (let i = 0; i < rows.length; i++) {
            const row = rows[i];
            const checkbox = row.querySelector('input[type="checkbox"]');
    

            if (checkbox.checked) {

                const name = row.children[1].querySelector('p').textContent;
                const price = parseFloat(row.children[2].querySelector('p').textContent);
                const decFactor = parseFloat(row.children[3].querySelector('p').textContent);
    
                checkedFurnitureItems.push(name);

                totalPrice += price;
                totalDecFactor += decFactor;
            }
        }

        if (checkedFurnitureItems.length > 0) {
            averageDecFactor = totalDecFactor / checkedFurnitureItems.length;
        }

        textareaOutputElement.textContent = `Bought furniture: ${checkedFurnitureItems.join(', ')}`;
        textareaOutputElement.textContent += `\nTotal price: ${totalPrice.toFixed(2)}`;
        textareaOutputElement.textContent += `\nAverage decoration factor: ${averageDecFactor}`;
    });
    
}
