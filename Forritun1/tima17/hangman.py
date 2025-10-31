class Hangman:
    
    def __init__(self, word: str):
        self.word = word
        self.letter_guess = []
        self.count = 0

    def guess_letter(self, letter: str) -> bool:
        

        if letter.lower() not in self.word.lower():
            self.count += 1
            return False
        
        elif letter.lower() in self.word.lower():
            self.letter_guess.append(letter.upper())
            return True 


    def __str__(self) -> str:

        hangman_loc = []
        for value in self.word:
            if value.upper() in self.letter_guess:
                hangman_loc.append(value.upper())
            else:
                hangman_loc.append("_")

        return f'{" ".join(hangman_loc)}\nNumber of incorrect guesses: {self.count}'   
     

hangword = Hangman("Testing")
print(hangword)
print(hangword.guess_letter("i"))
print(hangword.guess_letter("I"))
print(hangword.guess_letter("a"))
hangword.guess_letter("t")
print(hangword)
hangword.guess_letter("E")
hangword.guess_letter("s")
print(hangword)
hangword.guess_letter("i")
hangword.guess_letter("N")
hangword.guess_letter("g")
print(hangword)