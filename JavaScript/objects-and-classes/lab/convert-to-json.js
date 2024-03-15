function solve(firstName, lastName, hairColor) {
    let personalInfo = {
        name: firstName,
        lastName,
        hairColor,
    };

    jsonfied = JSON.stringify(personalInfo);
    
    console.log(jsonfied);

}

solve('George', 'Jones', 'Brown')
solve('Peter', 'Smith', 'Blond')