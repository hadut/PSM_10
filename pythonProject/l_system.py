import turtle
import time
import tkinter as tk


class Plant:
    def __init__(self, word, n, l, angle):
        self.rules = {"X": "F-[[X]+X]+F[+FX]-X", "F": "FF"}
        self.word = word
        self.n = n
        self.l = l
        self.angle = angle
        self.word = self.generate_word()
        self.root = tk.Tk()
        self.draw()
        self.root.mainloop()

    def generate_word(self):
        new_word = self.word
        for i in range(self.n):
            new_word = self.make_word(new_word)
        return new_word

    def make_word(self, word):
        new_word = ""
        for char in word:
            new_word += self.rules.get(char, char)
        return new_word

    def draw(self):
        canavs = tk.Canvas(self.root, width=1200, height=700)
        canavs.pack(side=tk.RIGHT)
        length = len(self.word)
        progress = tk.Label(self.root, text=f"{round(0 / length * 100, 2)}%  {0}/{length}")
        progress.pack(side=tk.TOP)
        frequency = tk.Label(self.root, text=f"frequency: {round(0 / (time.time() - 0), 2)}")
        frequency.pack(side=tk.TOP)
        remaining = tk.Label(self.root, text=f"estimated remaining time: {0}")
        remaining.pack(side=tk.TOP)
        screen = turtle.TurtleScreen(canavs)
        screen.setworldcoordinates(-25, -25, 1175, 675)
        t = turtle.RawTurtle(screen)
        t.speed(0)
        t.pensize(1)
        t.color("green")
        t.penup()
        t.hideturtle()
        t.goto(0, 0)
        t.pendown()
        t.setheading(self.angle)

        positions = []
        i = 0
        start = time.time()
        for char in self.word:
            i += 1
            progress.config(text=f"{round(i / length * 100, 2)}%  {i}/{length}")
            if time.time() - start != 0 and i != 0:
                frequency.config(text=f"frequency: {round(i / (time.time() - start), 2)} iter/second")
                remaining.config(text=f"estimated remaining time: \n"
                                      f"{round((length - i) / (i / (time.time() - start)), 2)} seconds\n"
                                      f"{round((length - i) / (i / (time.time() - start)) / 60, 2)} minutes\n"
                                      f"{round((length - i) / (i / (time.time() - start)) / 3600, 2)} hours")
            match char:
                case "F":
                    t.forward(self.l)
                case "-":
                    t.left(self.angle)
                case "+":
                    t.right(self.angle)
                case "[":
                    positions.append((t.position(), t.heading()))
                case "]":
                    pos, heading = positions.pop()
                    t.penup()
                    t.setposition(pos)
                    t.setheading(heading)
                    t.pendown()


if __name__ == "__main__":
    plant = Plant("X", 8, 1, 25)
