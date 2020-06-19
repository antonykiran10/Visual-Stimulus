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
        radius=1,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)

f=1
while(f<=200):
    circle.radius=f
    f+=1
    circle.draw()
    win0.flip()


event.waitKeys()
win0.close()
