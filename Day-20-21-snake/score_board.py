from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("./highest_score.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()

        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Fira Code", 12, "normal"),
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./highest_score.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
