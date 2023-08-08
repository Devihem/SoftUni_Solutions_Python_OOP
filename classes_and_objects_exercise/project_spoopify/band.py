# from project.album import Album, Song
from album import Album, Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album_search in self.albums:
            if album_name == album_search.name:
                if album_search.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(album_search)
                    return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        band_albums_print = '\n'.join([album_print.details() for album_print in self.albums])
        return f"Band {self.name}\n{band_albums_print}"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
