function solve(inputString) {
    const heroes = [];

    class Hero {
        constructor(name, level, items) {
            this.name = name;
            this.level = level;
            this.items = items
        }
    }
    for (const heroData of inputString) {
        const [heroName, heroLevel, items] = heroData.split(' / ');
        const hero = new Hero(heroName, Number(heroLevel), items.split(', '));
        heroes.push(hero);
    }
    function sortByLevel(hero1, hero2) {
        return hero1.level - hero2.level;
    }
    heroes.sort(sortByLevel);
    
    heroes.forEach(hero => console.log(`Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items.join(', ')}`))
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ]);
solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ]);
