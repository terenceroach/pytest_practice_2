from lib.diary import *

"""
Initially
There are no entries
"""
def test_initally_there_are_no_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially word count is 0
"""
def test_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0



