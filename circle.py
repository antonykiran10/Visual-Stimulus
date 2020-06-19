from psychopy import visual, event


win0=visual.Window(
        size=(800,800),
        fullscr=False,
        units="pix",
        color=[1,1,1],
        monitor="testMonitor"
)


circle=visual.Circle(
        win=win0,
        radius=30,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)



circle.draw()
win0.flip()
event.waitKeys()
win0.close()
