from scripts.quiz import Quiz, Questions

PATH = "Path_to_Questions_Answears.json"

quiz_game = Quiz()
question_obj = Questions(PATH)


def test_next_question():
    assert quiz_game.next_question(question_obj)


def test_get_user_input():
    assert quiz_game.get_user_input() == "a"

def test_check_answear():
    user_input = "d"
    question_number = 1

    assert quiz_game.check_answear(user_input,question_obj,question_number) == True

def test_add_point():
    quiz_game.add_point()
    assert quiz_game.points == 1

def test_show_points():
    assert quiz_game.show_points() == 1
    quiz_game.add_point()
    assert quiz_game.show_points() == 2
