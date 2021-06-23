
from Engine import engine

@engine.update
def late_update(rate):
    print("its working.")

engine.delete_default_update()
win = None
engine.new_win(800, 600, win, (255,255,255))
go = engine.new_object("intro_ball.gif", 0, 0, 1, 1, 0)

engine.main()