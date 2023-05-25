questions = [
    {"ques": " humans have 304 bones",
     "ans": "False"},
    {"ques": "a slug's body is green",
     "ans": "True"},
    {"ques": "the size of human heart is approximately the size of fist",
     "ans": "True"},
    {"ques": "The total surface area of human lung is the siz of a hockey pitch",
     "ans": "False"},
    {"ques": "Google was earlier called 'backrub'",
     "ans": "True"},
    {"ques": "You can lead a cow down stairs but not upstairs",
     "ans": "False"},
    {"ques": "Total surface area of square is 6*size_length",
     "ans": "True"}
]

class Question:
    def __init__(self, txt, answer):
        self.text = txt
        self.answer = answer


