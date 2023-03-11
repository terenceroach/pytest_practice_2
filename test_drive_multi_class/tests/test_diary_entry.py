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