from quiz_brain import QuizBrain
from data import question_data
from question_model import Question



question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")




