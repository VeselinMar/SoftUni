function solve(employeeList) {
    class Employee {
        constructor(employeeName) {
            this.employeeName = employeeName;
        }

        printEmployeeInfo() {
            console.log(`Name: ${this.employeeName} -- Personal Number: ${this.employeeName.length}`);
        }
    }

    for(person of employeeList) {
        let newEmployee = new Employee(person);
        newEmployee.printEmployeeInfo();
    }
}

solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]);

solve([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
    ]);