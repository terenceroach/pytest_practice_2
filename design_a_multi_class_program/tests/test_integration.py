from lib.diary import *
from lib.diary_entry import *
from lib.tasklist import *
from lib.contact_list import *

"""
Given one DiaryEntry which is added to Diary
We see this entry in the diary_entries list
"""
def test_one_diary_entry_added_to_entries_list():
    diary = Diary()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
    diary.add(entry_1)
    assert diary.entries_list == [entry_1] # => [entry_1]

"""
Given one DiaryEntry which is added to the TaskList
We see this entry in the todo_list list
"""
def test_one_todo_entry_added_to_todo_list():
    task_list = TaskList()
    todo_1 = DiaryEntry("Todo", "Complete the challenges")
    task_list.add(todo_1)
    assert task_list.todo_list == [todo_1]

"""
Given one DiaryEntry which is added to the ContactList
We see this entry in the contact_list list
"""
def test_one_contact_entry_added_to_contact_list():
    contact_list = ContactList()
    contact_1 = DiaryEntry("Contact 1", "07870000000")
    contact_list.add(contact_1)
    assert contact_list.contact_list == [contact_1]

"""
Given two DiaryEntry which are added to Diary and TaskList
We see these entries in the relevant lists
"""
def test_one_entry_for_diary_and_one_for_tasklist_show_in_lists():
    diary = Diary()
    task_list = TaskList()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
    todo_1 = DiaryEntry("First Todo", "Wash the dishes")
    diary.add(entry_1)
    task_list.add(todo_1)
    assert diary.entries_list == [entry_1]
    assert task_list.todo_list == [todo_1]

"""
Given two DiaryEntry which is added to TaskList and ContactList
We see these entries in the relevant lists
"""
def test_one_entry_for_tasklist_and_one_for_contactlist_show_in_lists():
    task_list = TaskList()
    contact_list = ContactList()
    todo_1 = DiaryEntry("First Todo", "Wash the dishes")
    contact_1 = DiaryEntry("First Contact", "07870000000")
    contact_list.add(contact_1)
    task_list.add(todo_1)
    assert contact_list.contact_list == [contact_1]
    assert task_list.todo_list == [todo_1]

"""
Given two DiaryEntry which is added to Diary and ContactList
We see these entries in the relevant lists
"""
def test_one_entry_for_diary_and_one_for_contactlist_show_in_lists():
    diary = Diary()
    contact_list = ContactList()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
    contact_1 = DiaryEntry("First Contact", "07870000000")
    contact_list.add(contact_1)
    diary.add(entry_1)
    assert contact_list.contact_list == [contact_1]
    assert diary.entries_list == [entry_1]

"""
Given three DiaryEntry which are added to Diary, TaskList and ContactList
We see these entries in the relevant lists
"""
def test_one_entry_for_diary_one_entry_for_tasklist_and_one_for_contactlist_show_in_lists():
    diary = Diary()
    todos = TaskList()
    contact_list = ContactList()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
    todo_1 = DiaryEntry("First Todo", "Walk the dog")
    contact_1 = DiaryEntry("First Contact", "07870000000")
    contact_list.add(contact_1)
    diary.add(entry_1)
    todos.add(todo_1)
    assert contact_list.contact_list == [contact_1]
    assert diary.entries_list == [entry_1]
    assert todos.todo_list == [todo_1]

"""
Given one DiaryEntry which is added to the Diary
We can read the entry
"""
def test_read_one_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
    diary.add(entry_1)
    assert diary.read_entries() == "This is the first diary entry"

"""
Given two DiaryEntry which are added to the Diary
We can read the entries
"""
def test_read_two_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
    diary.add(entry_1)
    entry_2 = DiaryEntry("Second Entry", "This is the second diary entry")
    diary.add(entry_2)
    assert diary.read_entries() == "This is the first diary entry, This is the second diary entry"

"""
Given multiple DiaryEntry which are added to the Diary
We can read a entry based on the users reading speed and available time
"""
def test_read_entry_based_on_user_speed_and_available_time():
    diary = Diary()
    entry_1 = DiaryEntry("First Entry", "This is the first diary entry you see")
    entry_2 = DiaryEntry("Second Entry", "This is the second diary entry and is longer than the other entries")
    entry_3 = DiaryEntry("Third Entry", "This is third diary entry")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.read_chunk(2,3) == "This is third diary entry"
    assert diary.read_chunk(5,5) == "This is the second diary entry and is longer than the other entries"
    assert diary.read_chunk(2,6) == "This is the first diary entry you see"

"""
Given muliple contact numbers are added
We can see a list of all the numbers in the contact_list
"""
def test_multi_contacts_added_returned_in_a_list():
    contact_list = ContactList()
    contact_1 = DiaryEntry("Contact 1", "07870000000")
    contact_2 = DiaryEntry("Contact 2", "07870000005")
    contact_3 = DiaryEntry("Contact 3", "07870000003")
    contact_list.add(contact_1)
    contact_list.add(contact_2)
    contact_list.add(contact_3)
    assert contact_list.view_contacts() == ["07870000000", "07870000005", "07870000003"]