# test questions.py #
from scripts.questions import Questions

path = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"


def test_load_questions():
    test_question_obj = Questions()

    test_question_obj.load_questions(path)

    assert test_question_obj
