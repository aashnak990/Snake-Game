import turtle
import time
import random

delay=0.1
score=0
high_score=0
#set up the screen
window = turtle.Screen()
window.title("Dodo The Hungry Snake")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)
#turns off animation on Screen updates

#snake head
head=turtle.Turtle()
head.speed(0) #animation speed as 0 is fastest speed
head.shape("square")
head.color("black")
head.penup() #does not draw anything
head.goto(0,0) #head starts from center of Screen
head.direction ="stop"

#snake food
food=turtle.Turtle()
food.speed(0) #animation speed as 0 is fastest speed
food.shape("circle")
food.color("red")
food.penup() #does not draw anything
food.goto(0,100) #head starts from center of Screen

segments=[]
#pen for scoring on screen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0   High score: 0",align="center",font=("courier",24,"normal"))
#functions
def go_up():
    if head.direction !="down":
       head.direction = "up"

def go_down():
    if head.direction !="up":
      head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
       head.direction = "right"


def move():
    if (head.direction =="up"):
        y=head.ycor()
        head.sety(y+20)
    if (head.direction =="down"):
        y=head.ycor()
        head.sety(y-20)
    if (head.direction =="left"):
        x=head.xcor()
        head.setx(x-20)
    if (head.direction =="right"):
        x=head.xcor()
        head.setx(x+20)

#keyboard bindings (connects key with particularfunction)
window.listen() #listen for key press
window.onkeypress(go_up , "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left , "Left")
window.onkeypress(go_right , "Right")
#main game mainloop
while True:
    window.update() #updates the screen
    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    #hide segments
        for segment in segments:
          segment.goto(1000,1000)
          #clear segment listen
        segments = []
        #reset score
        score=0
        delay=0.1
        pen.clear()
        pen.write("score : {}   High score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))

    #check for collision with the food

    if head.distance(food) < 40:
        #move food to random position
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

    #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup() #no draw
        segments.append(new_segment)
        #shorten delay
        delay -= 0.001
            #increase score
        score= score+10

        if score>high_score:
             high_score=score
        pen.clear()
        pen.write("score : {}   High score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))


    #move end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    #check for head collisions with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide segments
            for segment in segments:
                 segment.goto(1000,1000)
                  #clear segment listen
            segments = []
            score=0
            delay=0.1
            pen.clear()
            pen.write("score : {}   High score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))


    time.sleep(delay)

window.mainloop()
