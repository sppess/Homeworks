import datetime
# datetime.timedelta - разница между двумя моментами времени,
# с точностью до микросекунд.
from typing import List  # Для указания типов


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []

    def __repr__(self):
        return self.name

    @property
    def song_numbers(self):
        return len(self.songs)

    @property
    def albums_numbers(self):
        return len(self.albums)


class Album:
    def __init__(self, name, year: int, genre: str, artist: Artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.artist.albums.append(self)  # !

        self.songs = []

    def __repr__(self):
        return f"{self.name} by {self.artist.name}"

    @property
    def song_numbers(self):
        return len(self.songs)

    @property
    def duration(self):
        return datetime.timedelta(sum(song.duration.seconds for
                                      song in self.songs))


class Song:
    def __init__(self, name: str, artist: Artist,
                 year: int, duration: int,
                 album: Album = None,
                 features: List[Artist] = None):
        if album and (album.artist != artist):
            raise WrongArtistError(f"{album.artist} is not {artist}")

        self.name = name
        self.artist = artist
        self.duration = datetime.timedelta(seconds=duration)
        self.year = year
        self.album = album
        self.features = features or []

        if self.album:
            if self.album.artist != artist:
                raise WrongArtistError(f"{album.artist} is not {artist}")
            self.album.songs.append(self)

    def __repr__(self):
        return f"{self.name} by {self.artist.name}"


if __name__ == '__main__':
    a1 = Artist('Nick', 'USA')
    a2 = Artist('Stiven', 'Germany')
    alb = Album('Best Hits', 1993, 'Pop', a1)

    s1 = Song('She', a1, 2003, 150, alb)
    s2 = Song('She', a1, 2003, 150, alb)
    s3 = Song('She', a1, 2003, 150, alb)
    s4 = Song('She', a1, 2003, 150, alb)
