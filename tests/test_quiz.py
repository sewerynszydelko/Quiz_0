from scripts.quiz import Quiz
from scripts.questions import Questions

PATH = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"

quiz_game = Quiz()
question_obj = Questions(PATH)


def test_next_question():
    assert quiz_game.next_question(question_obj)


def test_get_user_input():
    assert quiz_game.get_user_input() == "a"

def test_check_answear():
    user_input = "d"
    question_number = 0

    assert quiz_game.check_answear() == True

def test_add_point():
    quiz_game.add_point()
    assert quiz_game.points == 1

def test_show_points():
    assert quiz_game.show_points() == 0
    quiz_game.add_point()
    assert quiz_game.show_points() == 1
