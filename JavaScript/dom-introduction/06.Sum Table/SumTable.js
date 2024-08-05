function sumTable() {
    let table = document.querySelectorAll("table tr");
    let result = document.querySelector("#sum")
    let total = 0;
    for (let i = 1; i < table.length; i++) {
        let cols = table[i].children;
        let cost = cols[cols.length - 1].textContent;
        total += Number(cost);
    }
    result.textContent = total
}