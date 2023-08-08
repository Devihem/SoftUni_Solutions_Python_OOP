# from project.song import Song
from song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."

        elif song in self.songs:
            return "Song is already in the album."

        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        for song_search in self.songs:
            if song_name == song_search.name:
                self.songs.remove(song_search)
                return f"Removed song {song_search.name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        song_print_form = '\n'.join([f'== {song_print.get_info()}' for song_print in self.songs])
        return f"Album {self.name}\n{song_print_form}"
