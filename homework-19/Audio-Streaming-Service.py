# Implement a simple Audio Streaming Service class architecture
# It'll include 3 classes - Song, Album and Artist
#
# Artist class:
#   - name: str
#   - country: str
#   - songs: list = []
#   - albums: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - albums_number: int - must be declared using property decorator as the
#   length of albums list
#
# Album class:
#   - name: str
#   - year: int
#   - genre: str
#   - artist: Artist
#   - songs: list = []
#   - songs_number: int - must be declared using property decorator as the
#   length of songs list
#   - duration: float - must be declared using property decorator. Album
#   duration is the sum of all songs' (from songs list) duration.
#
# Song class:
#   - name: str
#   - artist: Artist
#   - features: list[Author] = [] (can feature 1 or more Artists)
#   - year: int
#   - duration: float
#   - album: Album (can be None if it's a single)
#
#   when you specify an album, make sure add the song to album's [songs] list.
#   the same with Artist albums/songs lists
#
#   Also, you need implement a custom exception WrongArtistError which is
#   raised when you try to add a song to an album and artists don't match.


class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []
        self._songs_number = 0
        self._album_number = 0

    def __repr__(self):
        return f"{self.name}"

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def album_number(self):
        return len(self.albums)


class Album:
    def __init__(self, name: str, year: int, genre: str, artist: Artist):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        self._songs_number = 0
        self._duration = 0

        if any(album.name == self.name for album in self.artist.albums):
             print(f"Album '{self.name}' already in {self.artist.name} "
                   f"albums list")
        else:
            self.artist.albums.append(self)

    def __repr__(self):
        return f"{self.name}"

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        duration = 0
        for song in self.songs:
            min = int(song.duration) * 60
            sec = (song.duration - int(song.duration)) * 100
            time =  min + sec
            duration += time
        return duration / 60


class Song:
    def __init__(self, name: str, artist: Artist,
                 features: list, year: int,
                 duration: float, album=None):
        self.name = name
        self.artist = artist
        self.year = year
        self.duration = duration
        self.album = album
        self.features = features
        # self.features.append(self.artist.name)

        if any(song.name == self.name for song in self.artist.songs):
            print(f"Song '{self.name}' already in {self.artist.name} "
                  f"albums list")
        else:
            self.artist.songs.append(self)

        if self.album is None:
            print("Song cannot be added to album as this is a single")
        elif self.artist is not self.album.artist:
            raise WrongArtistError("Song's artist name don't match with "
                                   "album's artist name. Make sure the song's "
                                   "artist or album is correct")
        else:
            self.album.songs.append(self)

    def __repr__(self):
        return f"{self.name}"
