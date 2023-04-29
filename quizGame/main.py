from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    new_Question = Question(text, answer)
    question_bank.append(new_Question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your total score was: {quiz.score}/{quiz.question_number}")