class QuizBrain:
    def __init__(this, list):
        this.question_number = 0
        this.question_list = list
        this.score = 0
    
    def still_has_questions(this):
        return this.question_number < len(this.question_list)
    
    def next_question(this):
        current_question = this.question_list[this.question_number]
        this.question_number += 1
        user_answer = input(f"Q.{this.question_number}: {current_question.text} (True/False): ")
        this.check_answer(user_answer, current_question.answer)

    def check_answer(this, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            this.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {this.score}/{this.question_number}")