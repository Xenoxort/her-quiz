import random

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_bank

    def still_has_questions(self):
        return len(self.questions_list) != 0

    def next_question(self):
        self.question_number += 1
        current_question = random.choice(self.questions_list)
        current_text = current_question.text
        current_answer = current_question.answer
        self.questions_list.remove(current_question)

        player_input = input(f"Q.{self.question_number}: {current_text} (True/False)?: ")

        self.check_answer(current_answer, player_input)

    def check_answer(self, answer, input):
        if answer.lower() == input.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

