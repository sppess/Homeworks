class WrongArtistError(Exception):
    pass


class Artist:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []

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

        if any(album.name == self.name for album in self.artist.albums):
            raise ValueError(f"Album '{self.name}' already in "
                             f"{self.artist.name} albums list")
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
        if len(self.songs) == 0:
            print('Songs list is empty')
            return 0

        for song in self.songs:
            if len(self.songs) == 1:
                return song.duration
            else:
                min_ = int(song.duration) * 60
                sec = (song.duration - int(song.duration)) * 100
                time = min_ + sec
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

        if any(song.name == self.name for song in self.artist.songs):
            raise ValueError(f"Song '{self.name}' already in "
                             f"{self.artist.name} albums list")
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
