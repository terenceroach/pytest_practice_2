from lib.track import *
"""
Given a title and artist
And a search keyword for the full title
Matches is true 
"""
def test_matches_on_full_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cat Title") == True

"""
Given a title and artist
And a search keyword for a partial title
Matches is true
"""
def test_matches_on_partial_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cat") == True

"""
Given a title and artist
And a search keyword for a full artist
Matches is true
""" 
def test_matches_on_full_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Dog Artist") == True

"""
Given a title and artist
And a search keyword for a partial artist
Matches is true
"""
def test_matches_on_partial_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Dog") == True

"""
Given a title and artist
And a search keyword that does not match either
Matches is false
"""
def test_does_not_match_on_non_matching_keyword():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Frog") == False