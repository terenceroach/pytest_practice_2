from lib.music_library import *
from lib.track import *

"""
When add multiple tracks
They are reflected in the tracks list
"""
def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

"""
When I add multiple tracks
And I search for a partial track title
Then I get the matching track back
"""

def test_searched_for_track_by_partial_title():
    library = MusicLibrary()
    track_1 = Track("Dog", "Cat")
    track_2 = Track("Frog", "Toad")
    library.add(track_1)
    library.add(track_2)
    assert library.search('Do') == [track_1]

