from Engine import engine

@engine.update
def late_update(rate):
    print("its working.")

engine.delete_default_update()
win = None
engine.new_win(800, 600, win)
engine.main()