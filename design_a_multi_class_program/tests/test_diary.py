from lib.diary import *

"""
Initially
Diary diary_entries is an empty list
"""
def test_entries_list_initialise_empty_list():
    diary = Diary()
    assert diary.entries_list == []

"""
Initially
when trying to read diary_entries from the empty list, the empty list is returned
"""
def test_read_entries_returns_empty_string_initially():
    diary = Diary()
    assert diary.read_entries() == ""

    """
Initially
When trying to select entries based on users reading speed and available time from the empty list, an empty string is returned
"""
def test_read_chunk_returns_empty_string_initially():
    diary = Diary()
    diary.read_chunk(2,2) == ""