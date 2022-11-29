# Importing files
from turtle import Turtle


# Scoreboard class to calculate and display the score
class Score(Turtle):

    # score field to be used in update_score method
    score = 0

    def __init__(self):
        super().__init__()

    # Method to display the score
    def display(self):
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.write(f"Score:  {self.score}", False, align="center", font=("Garamond", 16, "normal"))
        self.color("white")

    # Method to update the score
    def update_score(self):
        self.score += 1
        self.clear()
        self.display()

    # Method to display the game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Garamond", 16, "normal"))
