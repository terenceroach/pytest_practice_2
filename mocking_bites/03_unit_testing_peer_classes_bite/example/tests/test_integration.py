from lib.diary import Diary
from lib.secret_diary import SecretDiary
"""
Given 1 diary entry
Go away message is received when the diary's content is locked
"""
def test_cannot_read_one_diary_content_when_it_is_locked():
    diary = Diary("I am some diary content that can't be viewed")
    secret_diary = SecretDiary(diary)

    assert secret_diary.read() == "Go away!"

"""
Given 1 diary entry
Contents is received when the diary's content is unlocked
"""
def test_can_read_one_diary_content_when_it_is_unlocked():
    diary = Diary("I am some diary content that can be viewed")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()

    assert secret_diary.read() == "I am some diary content that can be viewed"

"""
Given 1 diary entry
Go away message is received when the diary's content is locked after being unlocked
"""
def test_cannot_read_one_diary_content_when_it_is_unlocked_and_locked_again():
    diary = Diary("I am some diary content that cannot be viewed")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()

    assert secret_diary.read() == "Go away!"
