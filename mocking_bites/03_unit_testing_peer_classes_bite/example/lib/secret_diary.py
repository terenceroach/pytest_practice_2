class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.is_locked = True
        print(self.diary)

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        # call self.diary.read() if unlocked otherwise return Go away!
        if self.is_locked is False:
            return self.diary.read()
        else:
            return "Go away!"

    def lock(self):
        # Locks the diary
        # Returns nothing
        self.is_locked = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.is_locked = False