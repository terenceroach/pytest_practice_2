class MusicTrack():

    def __init__(self):
        self.music_track_list = []

    def add_track(self, track):
        self.music_track_list.append(track)

    def view_tracks(self):
        if self.music_track_list == []:
            raise Exception("You have not yet listened to any tracks!")
        else:
            counter = 1
            list_string = ""
            for i in self.music_track_list:
                list_string = list_string + f"{counter}. {i} "
                counter += 1
        return list_string.strip()