function solve(arrayOfStrings) {
    let phonebook = {};

    for(person of arrayOfStrings) {
        let [firstName, phoneNumber] = person.split(' ');
        phonebook[firstName] = phoneNumber;
    }

    for(person in phonebook) {
        console.log(`${person} -> ${phonebook[person]}`);
    }

}

solve(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344'])

solve(['George 0552554',
'Peter 087587',
'George 0453112',
'Bill 0845344'])
