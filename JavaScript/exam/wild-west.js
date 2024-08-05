function solve(input) {
    function executeCommand(command, posse) {
        const parts = command.split(' - ');

        switch (parts[0]) {
            case 'FireShot':
                const shooter = posse[parts[1]];
                const target = parts[2];
                if (shooter.bullets > 0) {
                    shooter.bullets--;
                    console.log(`${parts[1]} has successfully hit ${target} and now has ${shooter.bullets} bullets!`);
                } else {
                    console.log(`${parts[1]} doesn't have enough bullets to shoot at ${target}!`);
                }
                break;

            case 'TakeHit':
                const character = posse[parts[1]];
                const damage = parseInt(parts[2]);
                const attacker = parts[3];
                character.hp -= damage;
                if (character.hp > 0) {
                    console.log(`${parts[1]} took a hit for ${damage} HP from ${attacker} and now has ${character.hp} HP!`);
                } else {
                    delete posse[parts[1]];
                    console.log(`${parts[1]} was gunned down by ${attacker}!`);
                }
                break;

            case 'Reload':
                const reloadCharacter = posse[parts[1]];
                const maxBullets = 6;
                if (reloadCharacter.bullets === maxBullets) {
                    console.log(`${parts[1]}'s pistol is fully loaded!`);
                } else {
                    const numBulletsReloaded = maxBullets - reloadCharacter.bullets;
                    reloadCharacter.bullets = maxBullets;
                    console.log(`${parts[1]} reloaded ${numBulletsReloaded} bullets!`);
                }
                break;

            case 'PatchUp':
                const patchCharacter = posse[parts[1]];
                const maxHp = 100;
                const amount = parseInt(parts[2]);
                if (patchCharacter.hp === maxHp) {
                    console.log(`${parts[1]} is in full health!`);
                } else if (patchCharacter.hp + amount > maxHp) {
                    const amountRecovered = maxHp - patchCharacter.hp;
                    patchCharacter.hp = maxHp;
                    console.log(`${parts[1]} patched up and recovered ${amountRecovered} HP!`);
                } else {
                    patchCharacter.hp += amount;
                    console.log(`${parts[1]} patched up and recovered ${amount} HP!`);
                }
                break;

            case 'Ride Off Into Sunset':
                break;

            default:
                console.log("Invalid command");
        }
    }

    function parseInput(input) {
        const posseSize = parseInt(input[0]);
        const posse = {};

        for (let i = 1; i <= posseSize; i++) {
            const [name, hp, bullets] = input[i].split(' ');
            posse[name] = {
                hp: parseInt(hp),
                bullets: parseInt(bullets)
            };
        }

        const commands = input.slice(posseSize + 1);
        
        return { posse, commands };
    }

    const { posse, commands } = parseInput(input);

    // Execute each command
    commands.forEach(command => {
        executeCommand(command, posse);
    });

    // Print characters in posse
    for (const character in posse) {
        console.log(`${character}\n HP: ${posse[character].hp}\n Bullets: ${posse[character].bullets}`);
    }
}

// Example input
const input = (["2",
"Jesse 100 4",
"Walt 100 5",
"FireShot - Jesse - Bandit",
 "TakeHit - Walt - 30 - Bandit",
 "PatchUp - Walt - 20" ,
 "Reload - Jesse",
 "Ride Off Into Sunset"]);

solve(input);
