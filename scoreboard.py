from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/ken_nzioka/Desktop/data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.shape()
        self.goto(0, 170)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_file:
                new_file.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
