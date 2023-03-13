# Diary, Tasks and Contacts Multi-Class Planned Design Recipe

## 1. Describe the Problem

_
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
_

## 2. Design the Class System

_
Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com
_

```

┌─────────────────────────   ┐
│ DiaryEntry(title, contents)│
│                            │
│ - title                    │
│ - contents                 │
└─────────────────────────   ┘
             │
             │ creates lists in the following 3 classes
             ▼
┌────────────────────────────┐
│ Diary - a list created     |
|   from DiaryEntries        │
│                            │
│ - entries                  │
│ - add(entry)               │
│ - read_entries()           │
│   => [entries...]          │
| - read_chunk(wpm, time)    |
|   => "text"                |
└───────────┬────────────────┘

┌────────────────────────────┐
│ TaskList - a list created  |
|    from DiaryEntries       │
│                            │
│ - tasks                    │
│ - add(task)                │ 
└───────────┬────────────────┘

┌────────────────────────────┐
│ ContactList - a list       |
|   created from DiaryEntries│
│                            │
│ - contacts                 │
│ - add(contact)             |
| - view_contacts()          |
|  => [contacts]             │ 
└───────────┬────────────────┘

```

_Also design the interface of each class in more detail._

```python
class DiaryEntry():
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents)
        # Parameters:
        #   title: string
        #   contents: string
        # Side-effects:
        #   Sets the title and contents properties
        pass # No code here yet

class Diary():
    # User-facing properties:
    #   diary_entries: list of instances of DiaryEntry

    def __init__(self):
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the diary_entries property of the self object
        pass # No code here yet

    def read_entries(self):
        # Returns:
        #   A string of the Diary Entries that are in the diary_entries property of the self object
        pass # No code here yet

    def read_chunk(self, wpm, time):
        # Returns:
        #   A string up to the length that the user can read in the time they have available
        pass # No code here yet

class TaskList():
    # User-facing properties:
    #   todo_list: list of instances of DiaryEntry

    def __init__(self):
        pass # No code here yet

    def add(self, todo):
        # Parameters:
        #   todo: an instance of DiaryEntry
        # Side-effects:
        #   Adds the todo to the todo_list property of the self object
        pass # No code here yet

class ContactList():
    # User-facing properties:
    # contact_list: list of instances of DiaryEntry

    def __init__(self):
        pass # No code here yet

    def add(self, contact):
        # Parameters:
        #   contact: an instance of DiaryEntry
        # Side-effects:
        #   Adds the contact to the contact_list property of the self object
        pass # No code here yet

    def view_contacts(self):
        # Returns:
        #   A list of the contact_list number objects that are in the contact_list property of the self object
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given one DiaryEntry which is added to Diary
We see this entry in the diary_entries list
"""
diary = Diary()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
diary.add(entry_1)
diary.entries_list # => [entry_1]

"""
Given one DiaryEntry which is added to the TaskList
We see this entry in the todo_list list
"""
task_list = TaskList()
todo_1 = DiaryEntry("Todo", "Complete the challenges")
task_list.add(todo_1)
task_list.todo_list # => [todo_1]

"""
Given one DiaryEntry which is added to the ContactList
We see this entry in the contact_list list
"""
contact_list = ContactList()
contact_1 = DiaryEntry("Contact 1", "07870000000")
contact_list.add(contact_1)
contact_list.contact_list # => [contact_1]

"""
Given two DiaryEntry which is added to Diary and TaskList
We see these entries in the relevant lists
"""
diary = Diary()
task_list = TaskList()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
todo_1 = DiaryEntry("First Todo", "Wash the dishes")
diary.add(entry_1)
task_list.add(todo_1)
diary.entries_list # => [entry_1]
task_list.todo_list # => [todo_1]

"""
Given two DiaryEntry which is added to TaskList and ContactList
We see these entries in the relevant lists
"""
task_list = TaskList()
contact_list = ContactList()
todo_1 = DiaryEntry("First Todo", "Wash the dishes")
contact_1 = DiaryEntry("First Contact", "07870000000")
contact_list.add(contact_1)
task_list.add(todo_1)
contact_list.contact_list # => [contact_1]
task_list.todo_list # => [todo_1]

"""
Given two DiaryEntry which is added to Diary and ContactList
We see these entries in the relevant lists
"""
diary = Diary()
contact_list = ContactList()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
contact_1 = DiaryEntry("First Contact", "07870000000")
contact_list.add(contact_1)
diary.add(entry_1)
contact_list.contact_list # => [contact_1]
diary.entries_list # => [entry_1]

"""
Given three DiaryEntry which are added to Diary, TaskList and ContactList
We see these entries in the relevant lists
"""
diary = Diary()
todos = TaskList()
contact_list = ContactList()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
todo_1 = DiaryEntry("First Todo", "Walk the dog")
contact_1 = DiaryEntry("First Contact", "07870000000")
contact_list.add(contact_1)
diary.add(entry_1)
todos.add(todo_1)
contact_list.contact_list # => [contact_1]
diary.entries_list # => [entry_1]
todos.todo_list # => [todo_1]

"""
Given one DiaryEntry which is added to the Diary
We can read the entry
"""
diary = Diary()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
diary.add(entry_1)
diary.read_entries() # => ["This is the first diary entry"]

"""
Given two DiaryEntry which are added to the Diary
We can read the entries
"""
diary = Diary()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry")
diary.add(entry_1)
entry_2 = DiaryEntry("Second Entry", "This is the second diary entry")
diary.add(entry_2)
diary.read_entries() # => "This is the first diary entry, This is the second diary entry"

"""
Given multiple DiaryEntry which are added to the Diary
We can read a entry based on the users reading speed and available time
"""
diary = Diary()
entry_1 = DiaryEntry("First Entry", "This is the first diary entry you see")
entry_2 = DiaryEntry("Second Entry", "This is the second diary entry and is longer than the other entries")
entry_3 = DiaryEntry("Third Entry", "This is third diary entry")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.read_chunk(2,3) # => "This is third diary entry"
diary.read_chunk(5,5) # => "This is the second diary entry and is longer than the other entries"
diary.read_chunk(2,6) # => "This is the first diary entry you see"

"""
Given muliple contact numbers are added
We can see a list of all the numbers in the contact_list
"""
contact_list = ContactList()
contact_1 = DiaryEntry("Contact 1", "07870000000")
contact_2 = DiaryEntry("Contact 2", "07870000005")
contact_3 = DiaryEntry("Contact 3", "07870000003")
contact_list.add(contact_1)
contact_list.add(contact_2)
contact_list.add(contact_3)
contact_list.view_contacts() # => ["07870000000", "07870000005", "07870000003"]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a diary entry with a title and contents
We see the title reflected in the title property
"""
diary_entry = DiaryEntry("Title 1", "First Entry")
diary_entry.title # => "Title 1"

"""
Given a diary entry with a title and contents
We see the contents reflected in the contents property
"""
diary_entry = DiaryEntry("Title 1", "First Entry")
diary_entry.contents # => "First Entry"

"""
Initially
Diary diary_entries is an empty list
"""
diary = Diary()
diary.entries_list #  => []

"""
Initially
when trying to read diary_entries from the empty list, an em-ty string is returned
"""
diary = Diary()
diary.read_entries() # => []

"""
Initially
When trying to select entries based on users reading speed and available time from the empty list, an empty string is returned
"""
diary = Diary()
diary.read_chunk(2,2) # => ""

"""
Initially
TaskList todo_list is an empty list
"""
tasks = TaskList()
tasks.todo_list #  => []

"""
Initially
ContactList contact_list is an empty list
"""
contacts = ContactList()
contact.contact_list #  => []

"""
Initially
When trying to view a list of contacts, an empty list is returned
"""
contacts = ContactList()
contacts.view_contacts() #  => []
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
