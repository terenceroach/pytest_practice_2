# Single Class Program Challenge Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracks():
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   Creates an object of the class
        pass # No code here yet

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object (list)
        pass # No code here yet

    def view_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   A string showing the user the tracks they have listened to
        # Side-effects:
        #   Throws an exception if no tracks is set
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a track
# Add the track to the list of listened to tracks, and view them
"""
music_track = MusicTrack()
music_track.add_track("Welcome to the Jungle")
music_track.view_tracks() # => [1. Welcome to the Jungle]

"""
Given multiple tracks
# Add the tracks to the list of listened to tracks, and view them
"""
music_track = MusicTrack()
music_track.add_track("Welcome to the Jungle")
music_track.add_track("Like a Prayer")
music_track.add_track("Teenage Dirtbag")
music_track.view_tracks() # => [1. Welcome to the Jungle 2. Like a Prayer 3. Teenage Dirtbag]

"""
Given no track
# Raise an exception when user tries to view a list of listened to tracks
"""
music_track = MusicTrack()
music_track.view_tracks() # => [Excpetion: You have not yet listened to any tracks!]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

