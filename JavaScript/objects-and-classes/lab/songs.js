function solve(array) {
    let songs = [];
    let NumberOfSongs = array.shift();
    let typeSong = array.pop();

    class Song {
        constructor(type, name, time) {
            this.type = type;
            this.name = name;
            this.time = time;
        }
    }

    for (let i = 0; i < NumberOfSongs; i++) {
        let [type, name, time] = array[i].split('_');
        let song = new Song(type, name, time);
        songs.push(song);
    }

    if (typeSong === 'all') {
        songs.forEach((i) => console.log(i.name));

    } else {
        let filtered = songs.filter((i) => i.type === typeSong);
        filtered.forEach((i) => console.log(i.name));
    }
}