from quiz import questions, Question
from quiz_brain import QuizBrain

question_bank = []
for question in questions:
    question_ask = question["ques"]
    answer = question["ans"]
    new_question = Question(question_ask, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.more_questions():
    quiz.next_ques()

print("You have completed the quiz")
print(f"Your final scare is :{quiz.score} / {quiz.question_number}")