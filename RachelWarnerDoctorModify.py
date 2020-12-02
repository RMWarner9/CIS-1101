"""
Name: Rachel Warner
Program Name: Doctor Modify
Program Purpose: Acts as a therapist for the user using generated responses from input from the user
               Corrected the flaw where user said "you are a bad therapist"
Inputs:
    User inputs a sentence
Output: a response to the users
"""

import random

# Asks the user for their name
name = input("What is your name? ")

# hedges are used randomly to encourage conversation
hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")
# qualifiers are used to put at the beginning of the responses
qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")
# 1st and second person replacements. Added you: I , am: are
replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "mine": "yours", "you": "I", "am": "are", "are":
                "am", "i": "you"}


def reply(sentence):
    # Builds and returns a reply to the sentence
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + change_person(sentence)


def change_person(sentence):
    # Replaces first person nouns with second person nouns
    words = sentence.split()
    reply_words = []
    for word in words:
        reply_words.append(replacements.get(word, word))
    return " ".join(reply_words)


def main():
    # Handles the interaction between patient and doctor
    print(f"Good morning {name}, I hope you are well today. \n" +
          f"What can I do for you?\n" +
          f"To quit at any time type: QUIT")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))


# Entry point for program execution

if __name__ == "__main__":
    main()