""" Main question file calss """
import json
from string import ascii_uppercase

PATH = "Path_to_Questions_Answears.json"


class Questions:
    """Takes path to file with questions, iterate ,display ,
    and get any uestion in file
    """

    def __init__(self, path) -> None:
        "Initilaze path and data in list"
        self.path = path
        self.data = []

    def load_questions(self):
        """load questions, answears, right_answears from file given in init Qieston
        Returns:
            List: save all data from file to obj in 'data'
        """
        with open(self.path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

        return self.data

    def display_question_and_answaers(self, question_number=0) -> str:
        """Shows Questino, answears to user
        Args:
            question_number (int, optional): select witch quesiton. by 0-10 example Defaults to 0.
        Returns:
            str: Print out for user
        """
        print(self.data[question_number]["question"])
        for letter, answear in zip(ascii_uppercase, self.data[question_number]["answears"]):
            print(letter+":", answear)

    def get_answears(self, question_number=0):
        """Give all answears of that question
        Args:
            question_number (int, optional): Index of question in dickt. Defaults to 0.

        Returns:
            str: All answears for that question
        """
        return self.data[question_number]["answears"]

    def get_right_answer(self, question_number=0):
        """Give Correct answear of that question
        Args:
            question_number (int, optional): Inedx of question in given file. Defaults to 0.
        Returns:
            str: All answears
        """
        return self.data[question_number]["right_answaer"]

    def get_question(self, question_number=0):
        """Give question
        Args:
            question_number (int, optional): Inedx of question in given file. Defaults to 0.
        Returns:
            str: question
        """
        return self.data[question_number]["question"]

    def get_lenght_questions(self) -> int:
        """ Give lenght of given file Questions
        Returns:
            int: len of file question
        """
        return len(self.data)

    def get_question_data(self):
        """Get data from obj 
        Returns:
            list: all questions, answaers, data in dickts in list
        """
        return self.data


if __name__ == "__main__":

    questions_1 = Questions(PATH)
    first_ques = questions_1.load_questions()

    questions_1.display_question_and_answaers()
