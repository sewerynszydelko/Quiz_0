""" Quiz Game File """
from questions import Questions

PATH = "Path_to_Questions_Answears.json"


class Quiz():
    """Quiz obj for stering game
    """

    def __init__(self) -> None:
        """Initalize points and number of quesiton
        """
        self.number_question = 0
        self.points = 0

    def next_question(self, question_obj: object) -> None:
        """Give next quesiton in obj
        Args:
            question_obj (object): object with questions
        Returns:
            str: Print out to user next question and answear , uses form Question class
        """
        return question_obj.display_question_and_answaers(self.number_question)

    def get_user_input(self):
        """Get user input 
        Returns:
            str: Give user input in lower case
        """
        return input("waht's your answear: ").lower()

    def check_answear(self, user_input: str, question_obj: object, question_number: int) -> bool:
        """Checks if answear of user in specifyc question is right
        Args:
            user_input (str): leter from user a-d
            question_obj (object): object with questions
            question_number (int): number of cheking question
        Returns:
            bool: True or False if values are same
        """
        return user_input == question_obj.get_right_answer(question_number)

    def add_point(self):
        """Add point to quiz obj
        """
        self.points += 1

    def show_points(self) -> int:
        """ Display points to user
        Returns:
            int: Points erned by play
        """
        return self.points

    def play(self, quiz, question_obj):
        """ Plays game in for loop depends of amount of question
        Args:
            quiz (object): quiz object itself
            question_obj (object): object with all questions

        Returns:
            str: Print out info to user about points earned in this quiz
        """
        for i in range(len(question_obj.get_question_data())):

            quiz.next_question(question_obj)
            self.number_question = i + 1
            answear = quiz.get_user_input()

            if quiz.check_answear(answear, question_obj, i):
                quiz.add_point()

        return print(f"You got points: {quiz_game.show_points()} Congratulation!")

    def about_quiz(self):
        """Show how to play and explain
        """
        print("Hello welcom in quiz game about python code !!\n")
        print("I have 10 question for you\nyou can answaer from a - d")
        print("In the end i will tell you how many points you get!\n")
        input("If you ready press any key... ")


quiz_game = Quiz()

if __name__ == "__main__":

    questions = Questions(PATH)
    questions.load_questions()

    quiz_game.play(quiz_game, questions)
