from lib.diary import Diary

"""
Given a diary entry
contents property is set
"""
def test_contents_property_set():
    diary = Diary("A new diary entry")
    assert diary.contents == "A new diary entry"

"""
Given a diary entry
the read method return contents
"""
def test_read_method_returns_contents():
    diary = Diary("My diary entry")
    assert diary.read() == "My diary entry"
