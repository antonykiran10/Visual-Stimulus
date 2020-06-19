from psychopy import visual, event


win0=visual.Window(
        size=(800,800),
        fullscr=False,
        units="pix",
        color=[1,1,1],
        monitor="testMonitor"
)


circle1=visual.Circle(
        win=win0,
        radius=30,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)
circle2=visual.Circle(
        win=win0,
        radius=30,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)
circle3=visual.Circle(
        win=win0,
        radius=30,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)
circle4=visual.Circle(
        win=win0,
        radius=30,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)
circle5=visual.Circle(
        win=win0,
        radius=30,
        fillColor=[-1,-1,-1],
        lineColor=[-1,-1,-1],
        units="pix",
       # edges=128
)
circle1.pos=(-350,-400)
circle2.pos=(-200,-425)
circle3.pos=(200,-475)
circle4.pos=(350,-410)
circle5.pos=(0,-450)

f=0

while (f<=800):
        circle1.pos+=(0,1)
        circle2.pos+=(0,1)
        circle3.pos+=(0,1)
        circle4.pos+=(0,1)
        circle5.pos+=(0,1)
        circle1.draw()
        circle2.draw()
        circle3.draw()
        circle4.draw()
        circle5.draw()
        win0.flip()
        f+=1


win0.flip()
event.waitKeys()
win0.close()
