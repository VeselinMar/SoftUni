function login(arrayPassword) {
    const User = arrayPassword.shift();
    const Password = User.split('').reverse().join('');
    let attemptsCounter = 0;

    for (const element of arrayPassword) {
        if (element === Password) {
            console.log(`User ${User} logged in.`);
            return;
        } else {
            attemptsCounter += 1;
            if (attemptsCounter === 4) {
                console.log(`User ${User} blocked!`);
                return;
            } else{
            console.log("Incorrect password. Try again.");
            }
        }
    }
}

login(['Acer','login','go','let me in','recA']);
login(['momo','omom']);
login(['sunny','rainy','cloudy','sunny','not sunny']);