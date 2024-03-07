function matrix(num) {
    function printRow() {
        for (let i = 0; i < num; i++) {
            process.stdout.write(`${num} `);
        }
    }

    for (let i = 0; i < num; i++) {
        printRow();
        console.log();
    }
}

matrix(3);