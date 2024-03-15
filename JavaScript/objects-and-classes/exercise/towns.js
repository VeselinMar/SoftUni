function solve(cityArray) {
    let capitalInfo = {};

    for (city of cityArray) {
        let [cityName, cityLatitude, cityLongitude] = city.split(" | ");
        capitalInfo = {
            town: cityName,
            latitude: Number(cityLatitude).toFixed(2),
            longitude: Number(cityLongitude).toFixed(2),
        };
        console.log(capitalInfo);
    }
}

solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625'])

solve(['Plovdiv | 136.45 | 812.575'])