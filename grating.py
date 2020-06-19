# to create a moving grating square or sinusoidal with variable parameters masked in a circular field
# the default unit is in pixel and has to adjusted to suit the experimental requirements

from psychopy import visual, event

win0=visual.Window(
        size=[400,400],
        fullscr=False,
        units="pix",
        monitor="testMonitor"
)

grating=visual.GratingStim(
        win=win0,
        size=[400,400],
        units="pix",
        sf=5/400,    # x/y implies x cycles per y pixels
        ori=0,   # unit is in degree
        mask="circle",
        tex="sqr"   # type of grating sqr or sin
)
while(1):
    grating.setPhase(0.01,'+')
    grating.draw()
    win0.flip()
    if len(event.getKeys())>0:
        break
    
event.clearEvents()
win0.close()