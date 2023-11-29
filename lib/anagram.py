# your code goes here!
class Anagram:
    def __init__(self, word):
        pass
        self.word = word.lower()

    def match(self, candidate_list):
        pass
        word_sorted = sorted(self.word)
        return [candidate for candidate in candidate_list if sorted(candidate.lower()) == word_sorted and candidate.lower() != self.word]
