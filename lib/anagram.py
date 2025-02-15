class Anagram:
    def __init__(self, word):
        '''Initializes with a single word.'''
        self.word = word.lower()

    def match(self, word_list):
        '''Returns a list of words that are anagrams of the initialized word.'''
        sorted_word = sorted(self.word)
        anagrams = []

        for candidate in word_list:
            if sorted_word == sorted(candidate.lower()):
                anagrams.append(candidate)

        return anagrams
