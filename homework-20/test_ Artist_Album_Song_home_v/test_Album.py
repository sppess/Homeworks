import unittest
from Artist_Album_Song_home_v import Album, Artist, Song


class TestAlbum(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.artist1 = Artist("Bring Me The Horizon", "England")
        cls.artist2 = Artist("Infected Rain", "Moldova")

        cls.album1 = Album("That’s the Spirit", 2015, "Rock",
                           cls.artist1)
        cls.album2 = Album("Amo", 2019, "Rock", cls.artist1)
        cls.album3 = Album("86", 2017, "Rock", cls.artist2)
        cls.same_album = Album("86", 2017, "Rock", cls.artist2)

        cls.song1 = Song("Throne", cls.artist1, [], 2015, 3.07, cls.album1)
        cls.song2 = Song("Freaky carnival", cls.artist2, [], 2017, 5.12,
                         cls.album3)
        cls.song3 = Song("Orphan Soul", cls.artist2, [], 2017, 4.51,
                         cls.album3)
        cls.song4 = Song("Mold", cls.artist2, [], 2017, 5.27)

    def test_album_isinstance_Album(self):
        self.assertIsInstance(self.album1, Album)

    def test_album_have_songs_in_songs_list(self):
        if not self.album1.songs:
            print("Album songs list is empty")
        else:
            self.assertTrue(self.album1.songs)

    def test_songs_number_in_album_songs_list_is_correct(self):
        self.assertEqual(self.album1.songs_number, 1)
        self.assertEqual(self.album2.songs_number, 0)
        self.assertEqual(self.album3.songs_number, 2)

    def test_songs_duration_in_album_is_correct(self):
        self.assertEqual(self.album1.duration, 3.07)
        self.assertEqual(self.album2.duration, 0)
        self.assertAlmostEqual(self.album3.duration, 10, places=0)

    def test_album_is_unique_in_artist_album_list(self):
        self.assertEqual(len(self.artist2.albums),
                         len(set(self.artist2.albums)))
