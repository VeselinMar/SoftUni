function solve(arrayOfStrings) {
    let addressBook = {};

    for(element of arrayOfStrings) {
        let [name, address] = element.split(':');
        addressBook[name] = address;
    }
    
    Object.keys(addressBook)
        .sort()
        .forEach(key => {
            console.log(`${key} -> ${addressBook[key]}`);
        });
}

solve(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd']);

solve(['Bob:Huxley Rd',
'John:Milwaukee Crossing',
'Peter:Fordem Ave',
'Bob:Redwing Ave',
'George:Mesta Crossing',
'Ted:Gateway Way',
'Bill:Gateway Way',
'John:Grover Rd',
'Peter:Huxley Rd',
'Jeff:Gateway Way',
'Jeff:Huxley Rd']);