class Vehicle {
    _parts = {};

    constructor(type, model, parts, fuel) {
        this.type = type;
        this.model = model;
        this.parts = parts;
        this.fuel = fuel;
    }
    
    set parts(value) {
        this._parts = {
            engine: value.engine,
            power: value.power,
            quality: value.engine * value.power,
        }
    }

    get parts() {
        return this._parts;
    }

    drive(fuelLost) {
        this.fuel -= fuelLost
    }
}

let parts = {engine: 9, power: 500};
let vehicle = new Vehicle('l', 'k', parts, 840);
vehicle.drive(20);
console.log(vehicle.fuel);