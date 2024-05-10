import random

# edit this list - get more from Chat GPT
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of/from"},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "más", "english": "more"},
    {"spanish": "con", "english": "with"},
    {"spanish": "sus", "english": "his/her/your/their (plural)"},
    {"spanish": "es", "english": "is"},
    {"spanish": "al", "english": "to the"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "o", "english": "or"},
    {"spanish": "fue", "english": "was"},
    {"spanish": "ha", "english": "has"},
    {"spanish": "le", "english": "to him/her"},
    {"spanish": "sobre", "english": "about/on"},
    {"spanish": "si", "english": "if"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "sus", "english": "his/her/your/their (plural)"},
    {"spanish": "esta", "english": "this"},
    {"spanish": "entre", "english": "between/among"},
    {"spanish": "también", "english": "also/too"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "era", "english": "was (imperfect tense)"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "me", "english": "me"},
    {"spanish": "da", "english": "gives"},
    {"spanish": "te", "english": "you (singular)"},
    {"spanish": "puede", "english": "can/may"},
    {"spanish": "han", "english": "have (plural)"},
    {"spanish": "del", "english": "of the"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "sobre", "english": "on/over"},
    {"spanish": "nos", "english": "us"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "ni", "english": "neither/nor"},
    {"spanish": "contra", "english": "against"},
    {"spanish": "qué", "english": "what"},
    {"spanish": "unos", "english": "some"},
    {"spanish": "otro", "english": "other"},
    {"spanish": "ella", "english": "she"},
    {"spanish": "siempre", "english": "always"},
    {"spanish": "cuanto", "english": "how much"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "tan", "english": "so"},
    {"spanish": "solo", "english": "alone/only"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "donde", "english": "where"},
    {"spanish": "cada", "english": "each"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "vida", "english": "life"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "hora", "english": "hour"},
    {"spanish": "sabe", "english": "knows"},
    {"spanish": "días", "english": "days"},
    {"spanish": "año", "english": "year"},
    {"spanish": "tan", "english": "so"},
    {"spanish": "solo", "english": "alone/only"},
    {"spanish": "año", "english": "year"},
    {"spanish": "cada", "english": "each"},
    {"spanish": "día", "english": "day"},
    {"spanish": "vida", "english": "life"},
    {"spanish": "años", "english": "years"},
    {"spanish": "tiene", "english": "has"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "tanto", "english": "so much"},
    {"spanish": "saber", "english": "to know"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "mundo", "english": "world"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "puede", "english": "can/may"},
    {"spanish": "lugar", "english": "place"},
    {"spanish": "país", "english": "country"},
    {"spanish": "aún", "english": "still/even"},
    {"spanish": "entre", "english": "between"},
    {"spanish": "este", "english": "this"},
    {"spanish": "quiero", "english": "I want"},
]

def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()