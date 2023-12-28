class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_number +1 }. {self.question_list[self.question_number].text} (True/False):"
        ).lower()
        self.check_answer(user_answer)
        self.question_number += 1
        print(f"Your current score is: {self.score}/{self.question_number}")

    def check_answer(self, user_answer):
        if self.question_list[self.question_number].answer.lower() == user_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
