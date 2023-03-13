class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.words_read_so_far = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        total_words = len(self.contents.split())
        estimated_reding_time = total_words / wpm
        return int(estimated_reding_time)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.

        words_can_read = wpm * minutes
        if self.words_read_so_far >= len(self.contents.split()):
            self.words_read_so_far = 0
        chunk_to_read = " ".join(self.contents.split()[self.words_read_so_far:self.words_read_so_far + words_can_read])
        self.words_read_so_far += words_can_read
        return chunk_to_read