from lib.diary_entry import *

"""
Given 1 diary entry added
Return the to total number of words
"""
def test_adding_one_entry_returns_total_words():
    diary_entry = DiaryEntry("Title 1", "This is the first diary entry")
    assert diary_entry.count_words() == 6

"""
Given 1 diary entry initialised
Return the number of words in contents
"""
def test_ione_entry_the_word_count_in_contents():
    diary = DiaryEntry("Title 1", "This is the first diary entry")
    assert diary.count_words() == 6

"""
Given 1 diary entry initialised
Return the estimated time to read words in contents
"""
def test_one_entry_the_estimated_time_in_minutes_to_read_contents():
    diary = DiaryEntry("Title 1", "This is the first diary entry")
    assert diary.reading_time(2) == 3

"""
Given 1 entry added
Return a reading chunk that the user could read in the given minutes
"""
def test_add_one_entry_and_return_reading_chunk():
    diary = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    assert diary.reading_chunk(3,1) == "This is the"

"""
Given 1 entry added
Return muliple reading chunks that the user could read in the given minutes
"""
def test_add_one_entry_and_return_multiple_reading_chunk():
    diary = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    assert diary.reading_chunk(3,1) == "This is the"
    assert diary.reading_chunk(3,1) == "first diary entry"

"""
Given 1 entry added
Return muliple reading chunks over the length of the available conntenst that the user could read in the given minutes
Ensuring when the end of the contents is reached it goes back to the beginning
"""
def test_add_one_entry_and_return_multiple_reading_chunk_over_length_of_contents():
    diary = DiaryEntry("Title 1", "This is the first diary entry into the diary")
   
    assert diary.reading_chunk(3,1) == "This is the"
    assert diary.reading_chunk(3,1) == "first diary entry"
    assert diary.reading_chunk(2,2) == "into the diary"
    assert diary.reading_chunk(2,2) == "This is the first"

"""
Given 2 entris added
Return muliple reading chunks over the length of the available conntenst that the user could read in the given minutes
Ensuring when the end of the contents is reached it goes back to the beginning
"""
def test_add_multi_entries_and_return_multiple_reading_chunk_over_length_of_contents():
    diary_1 = DiaryEntry("Title 1", "This is the first diary entry into the diary")
    diary_2 = DiaryEntry("Title 2", "This is the second diary entry")
   
    assert diary_1.reading_chunk(3,1) == "This is the"
    assert diary_1.reading_chunk(3,1) == "first diary entry"
    assert diary_1.reading_chunk(2,2) == "into the diary"
    assert diary_1.reading_chunk(2,2) == "This is the first"
    assert diary_2.reading_chunk(5,5) == "This is the second diary entry"
    assert diary_2.reading_chunk(1,4) == "This is the second"