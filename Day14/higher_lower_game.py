# Import random module
# use random module to get the Data for questions A and B
# implement a function to convert data into printable strings
# ask user to check for the followers count
# if user is right, raise the score, else finish the game.
# if game is continue Question B becomes A and new question is being generated for B
# Process is repeated until user guess is wrong.

from random import randint
from Day14 import art, game_data


def random_question():
    # get the random data
    DataIndex = randint(0, (len(game_data.data) - 1))
    QuestionData = game_data.data[DataIndex]
    # question will be "Compare A: Priyanka Chopra Jonas, a Actress and musician, from India."
    QuestionString = f"{QuestionData['name']}, {QuestionData['description']}, from {QuestionData['country']}."
    return QuestionString, QuestionData['follower_count']


def question():
    question_a = random_question()
    question_b = random_question()
    return [question_a, question_b]


def game():
    score = 0
    continue_game = True
    while continue_game:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
            allquestions = [allquestions[1], random_question()]
        else:
            allquestions = question()

        if allquestions[0][1] > allquestions[1][1]:
            correct_answer = "A"
        else:
            correct_answer = "B"

        print(f"Compare A : {allquestions[0][0]}")
        print(art.vs)
        print(f"Against B : {allquestions[1][0]}")
        print(f"psst, correct answer is {correct_answer}")
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer != correct_answer:
            continue_game = False
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            continue
        else:
            score += 1


game()
