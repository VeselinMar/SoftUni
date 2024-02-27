from song import Song


class Album:

    def __init__(self, name: str, *songs,):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        album_info = f"Album {self.name} \n"
        songs_info = "\n".join([f"== {song.get_info()}" for song in self.songs])
        return f"{album_info}{songs_info}"
