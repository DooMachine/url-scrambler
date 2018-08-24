import itertools

class Scrambler():
    """
    Scramble string and return array of scrambled strings.
    """
    __info__ = {
        "name": "Python Word Scrambler",
        "description": "Scramble string and return array of scrambled strings.",
        "authors": (
            "Okan Aslankan <okn.aslnkn[at]gmail.com>",
        ),
    }   
            
    def Scramble_Word(self, word):
        if (type(word) is not str):            
            raise ValueError('Passed words should be type of string')            
        if (len(word)<=3):
            return [word]
        scrambled_words = self.InnerScramble_Word(word[1:-1])
        return [word[0] + e + word[-1:] for e in scrambled_words]

    def InnerScramble_Word(self, inner_word):
        word_lenght = len(inner_word)
        if (word_lenght <= 1):
            return [inner_word]
        if (word_lenght == 2):
            return inner_word[1] + inner_word[2]
        return ["".join(perm) for perm in itertools.permutations(inner_word)]
        
        



