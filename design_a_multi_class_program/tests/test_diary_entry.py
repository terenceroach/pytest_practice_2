from lib.diary_entry import *

"""
Given a diary entry with a title and contents
We see the title reflected in the title property
"""
def test_add_one_entry_sets_title_correct():
    diary_entry = DiaryEntry("Title 1", "First Entry")
    assert diary_entry.title == "Title 1"

"""
Given a diary entry with a title and contents
We see the contents reflected in the contents property
"""
def test_add_one_entry_sets_contents_correct():
    diary_entry = DiaryEntry("Title 1", "First Entry")
    assert diary_entry.contents == "First Entry"
