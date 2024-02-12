""" Quiz Game File """
from questions import Questions


class Quiz():

    def __init__(self) -> None:
        self.number_question = 0
        self.points = 0

    def next_question(self,question_obj):
        return question_obj.display_question_and_answaers(self.number_question)

    def get_user_input(self):
        return input("waht's your answear: ").lower()

    def about_quiz(self):
        print("Hello welcom in quiz game about python code !!\n")
        print("I have 10 question for you\nyou can answaer from a - d")
        print("In the end i will tell you how many points you get!\n")
        input("If you ready press any key... ")


PATH = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"

quiz_game = Quiz()
question_obj = Questions(PATH)
question_obj.load_questions()

while True:
    quiz_game.about_quiz()

    for i in range(len(question_obj.data)):

        quiz_game.next_question(question_obj)
        quiz_game.number_question += 1
        answear = quiz_game.get_user_input()

        if answear == question_obj.data[i]["right_answaer"]:
            quiz_game.points += 1
            print()

    print(f"You got points: {quiz_game.points} Congratulation!")

    break
