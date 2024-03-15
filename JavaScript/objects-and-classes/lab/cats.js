function solve(arrayOfStrings) {

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        makeMeow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for(element of arrayOfStrings) {
        let [catName, catAge] = element.split(' ');
        let cat = new Cat(catName, catAge);
        cat.makeMeow();
    }
}

solve(['Mellow 2', 'Tom 5']);
solve(['Candy 1', 'Poppy 3', 'Nyx 2']);