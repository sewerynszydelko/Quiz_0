""" Main question file calss """
import json
from string import ascii_uppercase


class Questions:

    def __init__(self) -> None:
        self.data = []

    def load_questions(self, path):
        with open(path, "r") as file:
            data_json = json.load(file)
            self.data = data_json

        return self.data

    def display_question_and_answaers(self, question_number=0) -> str:
        print(self.data[question_number]["question"])
        for letter, answear in zip(ascii_uppercase, self.data[question_number]['answears']):
            print(letter+":", answear)


path = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"

if __name__ == "__main__":

    questions_1 = Questions()
    first_ques = questions_1.load_questions(path)

    questions_1.display_question_and_answaers()
