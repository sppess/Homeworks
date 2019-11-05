import unittest
from Artist_Album_Song_home_v import Album, Artist, Song, WrongArtistError


class TestAlbum(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.artist1 = Artist("Bring Me The Horizon", "England")
        cls.artist2 = Artist("Infected Rain", "Moldova")

        cls.album1 = Album("That’s the Spirit", 2015, "Rock",
                           cls.artist1)
        cls.album2 = Album("Amo", 2019, "Rock", cls.artist1)
        cls.album3 = Album("86", 2017, "Rock", cls.artist2)

        cls.song1 = Song("Throne", cls.artist1, [], 2015, 3.07, cls.album1)
        cls.song2 = Song("Freaky carnival", cls.artist2, [], 2017, 5.12,
                         cls.album3)
        cls.song3 = Song("Orphan Soul", cls.artist2, [], 2017, 4.51,
                         cls.album3)
        cls.song4_singl = Song("Mold", cls.artist2, [], 2017, 5.27)

        cls.same_song = Song("Throne", cls.artist1, [], 2015, 3.07, cls.album1)

    def test_song_isinstance_Song(self):
        self.assertIsInstance(self.song1, Song)

    def test_song_duration_is_float(self):
        self.assertIsInstance(self.song1.duration, float)

    def test_song_in_self_artist_songs_list(self):
        self.assertIn(self.song1, self.artist1.songs)
        self.assertIn(self.song2, self.artist2.songs)

    def test_song_is_unique_in_artist_song_list(self):
        self.assertEqual(len(self.artist1.songs), len(set(self.artist1.songs)))

    def test_singl_not_in_any_albums_song_list(self):
        self.assertIs(self.song4_singl.album, None)
        for album in self.artist2.albums:
            self.assertNotIn(self.song4_singl, album.songs)

    def test_rises_error_if_song_artist_and_song_album_artist_dont_match(self):
        with (self.assertRaises(WrongArtistError)):
            Song("Orphan Soul", self.artist1, [], 2017, 4.51, self.album3)
