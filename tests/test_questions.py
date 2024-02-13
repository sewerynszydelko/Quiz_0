# test questions.py #
from scripts.questions import Questions

path = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"


def test_load_questions():
    test_question_obj = Questions(path)

    test_question_obj.load_questions()

    assert test_question_obj


def test_display_questions():
    test_question_obj = Questions(path)
    test_question_obj.load_questions()

    test_question_obj.display_question_and_answaers()

    assert True


def test_answear():
    test_obj_question = Questions(path)
    test_obj_question.load_questions()

    answears = test_obj_question.get_answears(0)

    assert answears == test_obj_question.data[0]["answears"]


def test_right_answear():
    test_obj_question = Questions(path)
    test_obj_question.load_questions()

    right_answears = test_obj_question.get_right_answer(0)

    assert right_answears == test_obj_question.data[0]["right_answaer"]


def test_question():
    test_obj_question = Questions(path)
    test_obj_question.load_questions()

    question = test_obj_question.get_question(0)

    assert question == test_obj_question.data[0]["question"]


def test_lenght_questions():
    test_obj_question = Questions(path)
    test_obj_question.load_questions()

    questions_len = test_obj_question.get_lenght_questions()

    assert questions_len == len(test_obj_question.data)


def test_question_data():
    test_obj_question = Questions(path)
    test_obj_question.load_questions()

    question_data = test_obj_question.get_question_data()

    assert question_data == test_obj_question.data
