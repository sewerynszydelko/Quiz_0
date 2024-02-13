""" Quiz Game File """
from questions import Questions


class Quiz():

    def __init__(self) -> None:
        self.number_question = 0
        self.points = 0

    def next_question(self, question_obj: object) -> None:
        return question_obj.display_question_and_answaers(self.number_question)

    def get_user_input(self):
        return input("waht's your answear: ").lower()

    def check_answear(self, user_input: str, question_obj: object, question_number: int) -> bool:
        return user_input == question_obj.get_right_answer(question_number)

    def add_point(self):
        self.points += 1

    def show_points(self):
        return self.points

    def play(self, quiz, question_obj):
        for i in range(len(question_obj.get_question_data())):

            quiz.next_question(question_obj)
            self.number_question = i + 1
            answear = quiz.get_user_input()

            if quiz.check_answear(answear, question_obj, i):
                quiz.add_point()

        return print(f"You got points: {quiz_game.show_points()} Congratulation!")

    def about_quiz(self):
        print("Hello welcom in quiz game about python code !!\n")
        print("I have 10 question for you\nyou can answaer from a - d")
        print("In the end i will tell you how many points you get!\n")
        input("If you ready press any key... ")


PATH = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"

quiz_game = Quiz()
question_obj = Questions(PATH)
question_obj.load_questions()

"""
while True:
    quiz_game.about_quiz()

    for i in range(len(question_obj.data)):

        quiz_game.next_question(question_obj)
        quiz_game.number_question = i
        answear = quiz_game.get_user_input()

        if quiz_game.check_answear(answear, question_obj, i):
            quiz_game.add_point()
            print()

    print(f"You got points: {quiz_game.show_points()} Congratulation!")

    break
"""
quiz_game.play(quiz_game, question_obj)
