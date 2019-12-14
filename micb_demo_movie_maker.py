from psychopy import core, event, visual, gui, data, monitors
from psychopy.tools.monitorunittools import pix2deg
from random import randint, sample, choice, shuffle
import math, numpy as np

win = visual.Window((800, 600), monitor='testMonitor',color=[.4, .4, .4], units='deg')
mon = monitors.Monitor('testMonitor', distance=150)
mouse = event.Mouse(visible=False)

def make_centers(numGabors, r=2.3):
    return [[r*math.cos((i-1)*(2*math.pi/numGabors)), r*math.sin((i-1)*(2*math.pi/numGabors))] for i in range(numGabors)]

def demo_slow(window, monitor, flexion, index): #0=control, 1=experimental
    speed = pix2deg(10, monitor) # this line is for modifying the speed of the balls
    rotation = 35 #degrees
    rot_idx = index
    radius = 2.3
    # flexion = 1 means the ball will rotate when changing direction
    flexion_point = [[0, -pix2deg(.5*window.size[1], monitor) + .5*radius],
                    [-pix2deg(.5*window.size[0], monitor) + .5*radius, -pix2deg(.5*window.size[1], monitor) + .5*radius]][flexion]
    path_change = [-pix2deg(.5*window.size[0], monitor) + .5*radius, -pix2deg(.5*window.size[1], monitor) + .5*radius]
    fixation = visual.Circle(window, pos=(-pix2deg(.5*window.size[0], monitor) + .5*radius, pix2deg(.5*window.size[1], monitor) - .5*radius),
                            lineColor='black', fillColor='black', radius = .1)
    gabor_coords = make_centers(6, 2.3)
    gabors = [visual.ImageStim(win=window, image='gab.png', size=1, ori=randint(0, 179),
                               pos=(c[0] - pix2deg(.5*window.size[0], monitor) + .5*radius, 
                               c[1] + pix2deg(.5*window.size[1], monitor) - .5*radius), 
                               units='deg') for c in gabor_coords]
    [gabor.draw() for gabor in gabors]
    fixation.draw()
    window.flip()
    rotated = False
    path_end = False
    path_changed = False
    v = [0, -1]
    while not path_end:
        if fixation.pos[1] <= path_change[1] and not path_changed:
            v = [1, 0]
            path_changed = True
        if ((fixation.pos[0] >= flexion_point[0] and not flexion) or (fixation.pos[1] <= flexion_point[1] and flexion)) and not rotated:
            gabors[rot_idx].ori += choice([-1, 1])*rotation
            rotated = True
        fixation.pos = (fixation.pos[0] + v[0]*speed, fixation.pos[1] + v[1]*speed)
        [gabor.setPos((gabor.pos[0] + v[0]*speed, gabor.pos[1] + v[1]*speed)) for gabor in gabors]
        [gabor.draw() for gabor in gabors]
        fixation.draw()
        window.flip()
        window.getMovieFrame()
        path_end = fixation.pos[0] >= pix2deg(.5*window.size[0], monitor) - .5*radius
    window.saveMovieFrames('slow' + str(index) + '.mp4', fps=60)

def demo_med(window, monitor, flexion, index): #0=control, 1=experimental
    speed = pix2deg(18, monitor) # this line is for modifying the speed of the balls
    rotation = 35 #degrees
    rot_idx = index
    radius = 2.3
    # flexion = 1 means the ball will rotate when changing direction
    flexion_point = [[0, -pix2deg(.5*window.size[1], monitor) + .5*radius],
                    [-pix2deg(.5*window.size[0], monitor) + .5*radius, -pix2deg(.5*window.size[1], monitor) + .5*radius]][flexion]
    path_change = [-pix2deg(.5*window.size[0], monitor) + .5*radius, -pix2deg(.5*window.size[1], monitor) + .5*radius]
    fixation = visual.Circle(window, pos=(-pix2deg(.5*window.size[0], monitor) + .5*radius, pix2deg(.5*window.size[1], monitor) - .5*radius),
                            lineColor='black', fillColor='black', radius = .1)
    gabor_coords = make_centers(6, 2.3)
    gabors = [visual.ImageStim(win=window, image='gab.png', size=1, ori=randint(0, 179),
                               pos=(c[0] - pix2deg(.5*window.size[0], monitor) + .5*radius, 
                               c[1] + pix2deg(.5*window.size[1], monitor) - .5*radius), 
                               units='deg') for c in gabor_coords]
    [gabor.draw() for gabor in gabors]
    fixation.draw()
    window.flip()
    rotated = False
    path_end = False
    path_changed = False
    v = [0, -1]
    while not path_end:
        if fixation.pos[1] <= path_change[1] and not path_changed:
            v = [1, 0]
            path_changed = True
        if ((fixation.pos[0] >= flexion_point[0] and not flexion) or (fixation.pos[1] <= flexion_point[1] and flexion)) and not rotated:
            gabors[rot_idx].ori += choice([-1, 1])*rotation
            rotated = True
        fixation.pos = (fixation.pos[0] + v[0]*speed, fixation.pos[1] + v[1]*speed)
        [gabor.setPos((gabor.pos[0] + v[0]*speed, gabor.pos[1] + v[1]*speed)) for gabor in gabors]
        [gabor.draw() for gabor in gabors]
        fixation.draw()
        window.flip()
        window.getMovieFrame()
        path_end = fixation.pos[0] >= pix2deg(.5*window.size[0], monitor) - .5*radius
    window.saveMovieFrames('medium' + str(index) + '.mp4', fps=60)

def demo_fast(window, monitor, flexion, index): #0=control, 1=experimental
    speed = pix2deg(26, monitor) # this line is for modifying the speed of the balls
    rotation = 35 #degrees
    rot_idx = index
    radius = 2.3
    # flexion = 1 means the ball will rotate when changing direction
    flexion_point = [[0, -pix2deg(.5*window.size[1], monitor) + .5*radius],
                    [-pix2deg(.5*window.size[0], monitor) + .5*radius, -pix2deg(.5*window.size[1], monitor) + .5*radius]][flexion]
    path_change = [-pix2deg(.5*window.size[0], monitor) + .5*radius, -pix2deg(.5*window.size[1], monitor) + .5*radius]
    fixation = visual.Circle(window, pos=(-pix2deg(.5*window.size[0], monitor) + .5*radius, pix2deg(.5*window.size[1], monitor) - .5*radius),
                            lineColor='black', fillColor='black', radius = .1)
    gabor_coords = make_centers(6, 2.3)
    gabors = [visual.ImageStim(win=window, image='gab.png', size=1, ori=randint(0, 179),
                               pos=(c[0] - pix2deg(.5*window.size[0], monitor) + .5*radius, 
                               c[1] + pix2deg(.5*window.size[1], monitor) - .5*radius), 
                               units='deg') for c in gabor_coords]
    [gabor.draw() for gabor in gabors]
    fixation.draw()
    window.flip()
    rotated = False
    path_end = False
    path_changed = False
    v = [0, -1]
    while not path_end:
        if fixation.pos[1] <= path_change[1] and not path_changed:
            v = [1, 0]
            path_changed = True
        if ((fixation.pos[0] >= flexion_point[0] and not flexion) or (fixation.pos[1] <= flexion_point[1] and flexion)) and not rotated:
            gabors[rot_idx].ori += choice([-1, 1])*rotation
            rotated = True
        fixation.pos = (fixation.pos[0] + v[0]*speed, fixation.pos[1] + v[1]*speed)
        [gabor.setPos((gabor.pos[0] + v[0]*speed, gabor.pos[1] + v[1]*speed)) for gabor in gabors]
        [gabor.draw() for gabor in gabors]
        fixation.draw()
        window.flip()
        window.getMovieFrame()
        path_end = fixation.pos[0] >= pix2deg(.5*window.size[0], monitor) - .5*radius
    window.saveMovieFrames('fast' + str(index) + '.mp4', fps=60)

for i in range(6):
    [demo_slow(win, mon, 1, i)]
    [demo_med(win, mon, 1, i)]
    [demo_fast(win, mon, 1, i)]

win.close()
core.quit()
