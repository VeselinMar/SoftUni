function cafeteria(inputArray) {
    // Extracting number of workers
    const n = parseInt(inputArray[0]);
    
    // Initializing workers object
    const workers = {};
    
    // Parsing information for each worker
    for (let i = 1; i <= n; i++) {
      const workerInfo = inputArray[i].split(' ');
      const name = workerInfo[0];
      const shift = workerInfo[1];
      const coffees = workerInfo.slice(2)[0].split(',');
      workers[name] = { name, shift, coffees };
    }
    
    // Processing commands until "Closed" command is given
    let commandIndex = n + 1;
    while (inputArray[commandIndex] !== 'Closed') {
      const command = inputArray[commandIndex].split(' / ');
      const action = command[0];
      const barista = command[1];
      
      // Handling different command types
      if (action === 'Prepare') {
        const shift = command[2];
        const coffeeType = command[3];
        
        if (workers[barista] && workers[barista].shift === shift && workers[barista].coffees.includes(coffeeType)) {
          console.log(`${barista} has prepared a ${coffeeType} for you!`);
        } else {
          console.log(`${barista} is not available to prepare a ${coffeeType}.`);
        }
      } else if (action === 'Change Shift') {
        const shift = command[2];
        
        if (workers[barista]) {
          workers[barista].shift = shift;
          console.log(`${barista} has updated his shift to: ${shift}`);
        }
      } else if (action === 'Learn') {
        const coffeeType = command[2];
        
        if (workers[barista]) {
          if (workers[barista].coffees.includes(coffeeType)) {
            console.log(`${barista} knows how to make ${coffeeType}.`);
          } else {
            workers[barista].coffees.push(coffeeType);
            console.log(`${barista} has learned a new coffee type: ${coffeeType}.`);
          }
        }
      }
      
      commandIndex++;
    }
  
    // Outputting the information of each worker
    for (const barista in workers) {
      console.log(`Barista: ${barista}, Shift: ${workers[barista].shift}, Drinks: ${workers[barista].coffees.join(', ')}`);
    }
  }
  
  // Example input:
  const inputArray = [
    '4',

'Alice day Espresso,Cappuccino',

'Bob night Latte,Mocha',

'Carol day Americano,Mocha',

'David night Espresso',

'Prepare / Alice / day / Espresso',

'Change Shift / Bob / day',

'Learn / Carol / Latte',

'Prepare / Bob / night / Latte',

'Learn / David / Cappuccino',

'Prepare / Carol / day / Cappuccino', 
'Change Shift / Alice / night', 
'Learn / Bob / Mocha', 
'Prepare / David / night / Espresso', 
'Closed'];
  
  cafeteria(inputArray);
  