# your code goes here!
class Anagram:
    def __init__(self, word):
        '''Initializes with a single argument, a word.'''
        self.word = word

    def match(self, words):
        '''Returns a list of words that are anagrams of the initialized word.'''
        # Convert the initialized word to a sorted tuple of characters
        sorted_word = tuple(sorted(self.word))
        # Initialize an empty list to store matching anagrams
        matched_words = []
        for w in words:
            # Convert the current word to a sorted tuple of characters
            if tuple(sorted(w)) == sorted_word:
                matched_words.append(w)
        return matched_words
