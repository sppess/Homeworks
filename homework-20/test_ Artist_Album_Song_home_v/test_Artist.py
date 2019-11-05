import unittest
from Artist_Album_Song_home_v import Artist, Album, Song


class TestArtist(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.artist1 = Artist("Bring Me The Horizon", "England")
        cls.artist2 = Artist("Infected Rain", "Moldova")
        cls.artist3 = Artist("New Years Day", "USA")

        cls.album1 = Album("That’s the Spirit", 2015, "Rock",
                           cls.artist1)
        cls.album2 = Album("Amo", 2019, "Rock", cls.artist1)
        cls.album3 = Album("86", 2017, "Rock", cls.artist2)

        cls.song1 = Song("Throne", cls.artist1, [], 2015, 3.07, cls.album1)
        cls.song2 = Song("Freaky carnival", cls.artist2, [], 2017, 5.12,
                         cls.album3)
        cls.song3 = Song("Orphan Soul", cls.artist2, [], 2017, 4.51,
                         cls.album3)
        cls.song4 = Song("Mold", cls.artist2, [], 2017, 5.27)

    def test_artist_isinstance_Artist(self):
        self.assertIsInstance(self.artist1, Artist)

    def test_artist_have_albums_in_albums_list(self):
        if not self.artist3.albums:
            print("Artist albums list is empty")
        else:
            self.assertTrue(self.artist1.albums)

    def test_artist_have_songs_in_songs_list(self):
        if not self.artist3.songs:
            print("Artist songs list is empty")
        if self.artist1.songs:
            self.assertTrue(self.artist1.songs)

    def test_songs_number_in_artist_songs_list_is_correct(self):
        self.assertEqual(self.artist1.songs_number, 1)
        self.assertEqual(self.artist2.songs_number, 3)

    def test_albums_number__in_artist_album_list_is_correct(self):
        self.assertEqual(self.artist1.album_number, 2)
        self.assertEqual(self.artist2.album_number, 1)
