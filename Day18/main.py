from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    question_bank.append(Questions(question_text, question_answer))
quiz_game = QuizBrain(question_bank)
while quiz_game.still_has_questions():
    quiz_game.next_question()
print(f"You have completed the quiz\nYour final score is {quiz_game.score}/{quiz_game.question_number}")

