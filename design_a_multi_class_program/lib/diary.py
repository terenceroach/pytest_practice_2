class Diary():
    def __init__(self):
        self.entries_list = []
    
    def add(self, entry):
        self.entries_list.append(entry)

    def read_entries(self):
        string_to_read = ""
        for i in self.entries_list:
            print(i.contents)
            string_to_read += i.contents + ", "
        print(string_to_read[:-2])
        return string_to_read[:-2]
    
    def read_chunk(self, wpm, time):
        words_can_read_in_time = wpm * time
        longest_chunk = ""
        for i in self.entries_list:
            if len(i.contents.split()) <= words_can_read_in_time:
                if len(i.contents.split()) > len(longest_chunk.split()):
                    longest_chunk = i.contents
        return longest_chunk