
from Engine import engine

class ExampleComponent(engine.Component):
    def start(self):
        print("start.")

win = None
engine.new_win(800, 600, win, (0,0,0))
go = engine.new_object("intro_ball.gif", 0, 0, 1, 1, 0)
go.addComponent(ExampleComponent)
engine.main()