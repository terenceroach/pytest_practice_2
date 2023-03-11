class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = len(self.text)
        while i > 0:
            if self.text[i-1].lower() in self.vowels:
                self.text = self.text[i:] + self.text[:i-1]
            i -= 1
        return self.text