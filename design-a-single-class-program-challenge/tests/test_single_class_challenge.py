import pytest
from lib.single_class_challenge import *

def test_add_single_track():
    music_track = MusicTrack()
    music_track.add_track("Welcome to the Jungle")
    assert music_track.view_tracks() == "1. Welcome to the Jungle"

def test_add_single_other_track():
    music_track = MusicTrack()
    music_track.add_track("Like a Prayer")
    assert music_track.view_tracks() == "1. Like a Prayer"

def test_add_multiple_tracks():
    music_track = MusicTrack()
    music_track.add_track("Welcome to the Jungle")
    music_track.add_track("Like a Prayer")
    music_track.add_track("Teenage Dirtbag")
    assert music_track.view_tracks() == "1. Welcome to the Jungle 2. Like a Prayer 3. Teenage Dirtbag"

def test_no_tracks_to_view_exception():
    music_track = MusicTrack()
    with pytest.raises(Exception) as e:
        music_track.view_tracks()
    error_message = str(e.value)
    assert error_message == "You have not yet listened to any tracks!"