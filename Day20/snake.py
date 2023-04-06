from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

BORDER = ((280, 280), (280, -280), (-280, -280), (-280, 280))


class Snake():
    def __init__(self):
        self.segments = []
        self.snake_init()
        self.border_init()
        self.head = self.segments[0]

    def border_init(self):
        self.border = Turtle()
        self.border.penup()
        self.border.ht()
        self.border.speed("fastest")
        self.border.color("white")
        self.border.goto((-280, 280))
        self.border.pendown()
        for i in BORDER:
            self.border.goto(i)

    def snake_init(self):
        for position in SNAKE_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            #new_segment.speed("fast")
            new_segment.goto(position)
            self.segments.append(new_segment)
            self.segments[0].color("green")

    def reset_snake(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.snake_init()
        self.head = self.segments[0]

    def snake_grow(self):
        last_block_positio = self.segments[-1].pos()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        #new_segment.speed("fastest")
        new_segment.goto(last_block_positio)
        self.segments.append(new_segment)

    def snake_position(self, what):
        x_position = self.segments[0].xcor()
        y_position = self.segments[0].ycor()
        print(what, x_position, y_position)

    def move(self):
        # for i in range(len(self.segments)):
        #     print("before move", i, self.segments[i].xcor(), self.segments[i].ycor())
        for i in range((len(self.segments) - 1), 0, -1):
            new_x_pos = self.segments[i - 1].xcor()
            new_y_pos = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_pos, new_y_pos)
        self.head.fd(MOVE_DISTANCE)

    def step_turn(self):
        x = int(self.head.xcor())
        y = int(self.head.ycor())
        new_x = x - (x % 20)
        new_y = (y - (y % 20))
        self.head.goto(new_x, new_y)


    def up(self):
        if self.head.heading() != DOWN:
            self.step_turn()
            self.head.setheading(UP)
            # self.snake_position("UP")

    def down(self):
        if self.head.heading() != UP:
            self.step_turn()
            self.head.setheading(DOWN)
            # self.snake_position("DOWN")

    def left(self):
        if self.head.heading() != RIGHT:
            self.step_turn()
            self.head.setheading(LEFT)
            # self.snake_position("LEFT")

    def right(self):
        if self.head.heading() != LEFT:
            self.step_turn()
            self.head.setheading(RIGHT)
            # self.snake_position("RIGHT")
