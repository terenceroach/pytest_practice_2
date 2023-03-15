from unittest.mock import Mock
from lib.secret_diary import SecretDiary
"""
Given a diary entry
If diary entry unlocked, read() will return it
"""
def test_unlocked_diary_is_returned():
    fake_diary= Mock()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    fake_diary.read.return_value = "A new diary entry"
    assert secret_diary.read() == "A new diary entry"

"""
Given a diary entry
If diary entry locked, read() will return go away message
"""
def test_locked_diary_is_not_returned_and_go_away_message_received():
    fake_diary= Mock()
    secret_diary = SecretDiary(fake_diary)
    fake_diary.read.return_value = "A new diary entry"
    assert secret_diary.read() == "Go away!"

"""
Given a diary entry
If diary entry locked, is_locked returns True
"""
def test_locked_diary_is_locked_equals_true():
    fake_diary= Mock()
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary.is_locked == True

"""
Given a diary entry
Diary entry can be unlocked and is_locked returns False
"""
def test_unlock_diary_and_is_locked_equals_false():
    fake_diary= Mock()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.is_locked == False

"""
Given a diary entry
Diary entry can be unlocked adn locked again and is_locked returns True
"""
def test_unlock_and_lock_again_diary_and_is_locked_equals_true():
    fake_diary= Mock()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.is_locked == True

def test_content_property():
    fake_diary = Mock()
    fake_diary.contents = "A new diary entry"
    secret_diary = SecretDiary(fake_diary)
 
    assert secret_diary.diary.contents == "A new diary entry"