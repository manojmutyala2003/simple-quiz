

questions = ("How many rings are on the Olympic flag?: ",
             "Which of these animals does NOT appear in the Chinese zodiac?: ",
             "How many holes are on a standard bowling ball?: ",
             "In the nursery rhyme, how many blackbirds were baked in a pie?: ",
             "What are the main colors on the flag of Spain?: ")

options = (("A. None", "B. 4 ", "C. 5", "D. 7"),
          ("A. Bear", "B. Dog", "C. Dragon", "D. Rabbit"),
          ("A. 2", "B. 3", "C. 5", "D. 10"),
          ("A. 4", "B. 11", "C. 24", "D. 99"),
          ("A. Black and yellow", "B. Blue and white", "C. Green and white", "D. Red and yellow"))

answers = ("C", "A", "B", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("!!!!! QUESTION !!!!!")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT !")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("**********************")
print("   ~~~~~RESULTS~~~~~  ")
print("**********************")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")