class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def more_questions(self):
        length = len(self.question_list)
        return self.question_number < length

    def check_answer(self, ans, answer):
        if ans.lower() == answer.lower():
            print(" ")
            print("You got it right!")
            self.score += 1
        else:
            print(" ")
            print("That's wrong!")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/ {self.question_number}")
        print(" ")




    def next_ques(self):
        current_ques = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_ques.text} (True/False): ")
        self.check_answer(user_answer, current_ques.answer)