
from turtle import *
import time
import Snake
from Snake import *
import Food
from Food import *
from Score import *
def main():
    # create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake game')
    screen.tracer(0)
    # setting the screen events
    snake = Snake()
    food = Food()
    screen.listen()
    screen.onkey(fun=snake.mv_right, key='Right')
    screen.onkey(fun=snake.mv_left, key='Left')
    screen.onkey(fun=snake.mv_up, key='Up')
    screen.onkey(fun=snake.mv_down, key='Down')
    score = Score()
   
    while True :
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.snakes[0].distance(food) <15:
            snake.extend()
            food.tp()
            score.update_score()
        if snake.snakes[0].xcor()>280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() >280 or snake.snakes[0].ycor() < -280:
            score.reset()
            snake.reset()

        for part  in snake.snakes :
            if part == snake.snakes[0]:
                pass
            elif snake.snakes[0].distance(part) <10 :
                score.reset()
                snake.reset()






if __name__ == '__main__':
    main()

