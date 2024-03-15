function solve(jsonStr) {
    let personInfo = JSON.parse(jsonStr);

    for(key in personInfo) {
        console.log(`${key}: ${personInfo[key]}`)
    }

}

solve('{"name": "George", "age": 40, "town": "Sofia"}')
solve('{"name": "Peter", "age": 35, "town": "Plovdiv"}')