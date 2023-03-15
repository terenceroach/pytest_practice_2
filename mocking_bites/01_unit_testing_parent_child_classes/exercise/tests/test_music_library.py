from unittest.mock import Mock
from lib.music_library import *

"""
When I add multiple tracks
And I search for a keyword
I get tracks that match that keyword
"""
def test_searches_by_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("hello") == [fake_matching]

"""
Initially, tracks is empty
"""
def test_tracks_empty_initially():
    library = MusicLibrary()
    assert library.tracks == []

"""
When I add some tracks
They show up in the tracks list
"""
def test_tracks_get_added_and_list_out():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.tracks == [track_1, track_2, track_3]