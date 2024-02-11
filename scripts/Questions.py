""" Main question file calss """
import json
from string import ascii_uppercase


class Questions:

    def __init__(self,path) -> None:
        self.path = path
        self.data = []

    def load_questions(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)

        return self.data

    def display_question_and_answaers(self, question_number=0) -> str:
        print(self.data[question_number]["question"])
        for letter, answear in zip(ascii_uppercase, self.data[question_number]['answears']):
            print(letter+":", answear)


path = "C:\\Users\\5792\\Desktop\\Quiz_0\\scripts\\Questions_Answears.json"

if __name__ == "__main__":

    questions_1 = Questions(path)
    first_ques = questions_1.load_questions()

    questions_1.display_question_and_answaers()
