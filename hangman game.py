import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "sql", "java","laptop"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")

    hint_letter = random.choice(word)
    guessed_letters.append(hint_letter)

    print("The word has",len(word),"letters.")
    while True:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)
        
        if display == word:
            print("Congratulations! You've guessed the word:", word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
        
        if attempts == 0:
            print("Sorry, you've run out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()
