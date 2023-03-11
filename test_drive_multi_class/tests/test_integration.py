from lib.diary import *
from lib.diary_entry import *

"""
Given 2 diary entries are added
We get the diary entries back in the entries list
"""
def test_add_multiple_entries_and_lists_them():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    entry_2 = DiaryEntry("Title 2", "This is the second diary entry into the diary")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given 1 diary entry is added
We get the diary entries back in the entries list
"""
def test_add_one_entry_and_lists_it():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    diary.add(entry_1)
    assert diary.all() == [entry_1]

"""
Given 2 diary entries added
Return the number of words
"""
def test_add_multiple_entreis_and_return_number_of_words():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    entry_2 = DiaryEntry("Title 2", "This is the second diary entry")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 15

"""
Given 3 diary entries are added
Return as estimate of the number of minutes required to read all entries based on the provided words per minute
"""
def test_add_multiple_entries_and_return_estimated_minutes_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    entry_2 = DiaryEntry("Title 2", "This is the second diary entry")
    entry_3 = DiaryEntry("Title 3", "This is the third diary entry and contains a bit of rambling")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.reading_time(3) == 9

    """
    Given 4 diary entries added
    Return the diary entry that matches closest the time the user as available but not over 
    """
def test_add_multiple_entries_and_return_diary_entry_most_suitable_to_users_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    entry_2 = DiaryEntry("Title 2", "This is the second diary entry")
    entry_3 = DiaryEntry("Title 3", "This is the third diary entry and contains a bit of rambling")
    entry_4 = DiaryEntry("Title 4", "This is the fourth diary entry and contains another load of complete and utter rambling")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    assert diary.find_best_entry_for_reading_time(2,7) == entry_3

def test_add_multiple_entries_and_return_diary_entry_most_suitable_to_users_time_2():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    entry_2 = DiaryEntry("Title 2", "This is the second diary entry")
    entry_3 = DiaryEntry("Title 3", "This is the third diary entry and contains a bit of rambling")
    entry_4 = DiaryEntry("Title 4", "This is the fourth diary entry and contains another load of complete and utter rambling")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    assert diary.find_best_entry_for_reading_time(2,3) == entry_2

"""
Given 1 entry added
Return a reading chunk that the user could read in the given minutes
"""
def test_add_one_entry_and_return_reading_chunk():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    diary.add(entry_1)
    assert entry_1.reading_chunk(3,1) == "This is the"