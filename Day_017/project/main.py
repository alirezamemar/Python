from question_model import Question
from data import question_data

question_bank = [ Question(item["text"], item["answer"]) for item in question_data]
print(question_bank)