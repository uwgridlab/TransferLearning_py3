#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Tue Mar  2 22:03:21 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

vis = 0;
cont_vis = 0
sync = ['audio', 'diode', 'TTL']
pair_ind = 1
right_image = None
left_image = None
stim_image = None
sides = ['left', 'right']


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'TL_Human_new'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/llevinson/Documents/TransferLearning_py3/TL_Human_new_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "settings"
settingsClock = core.Clock()
day_text = visual.TextStim(win=win, name='day_text',
    text='Choose TL day (1 or 2)',
    font='Arial',
    pos=(-.3, .45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    size=(.2, 0.05), pos=(-.3, .35), units=None,
    labels=['1', '2'], ticks=(1, 2),
    granularity=1, style=['radio'],
    color='Black', font='HelveticaBold',
    flip=False, depth=-1)
set_text = visual.TextStim(win=win, name='set_text',
    text='Choose picture set (1 or 2)',
    font='Arial',
    pos=(-.3, .15), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
slider_2 = visual.Slider(win=win, name='slider_2',
    size=(0.2, 0.05), pos=(-.3, 0.05), units=None,
    labels=['1', '2'], ticks=(1, 2),
    granularity=1, style=['radio'],
    color='Black', font='HelveticaBold',
    flip=False, depth=-3)
pergroup_text = visual.TextStim(win=win, name='pergroup_text',
    text='Choose number of images per group (3-5)',
    font='Arial',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
slider_3 = visual.Slider(win=win, name='slider_3',
    size=(.3, 0.05), pos=(0, -0.25), units=None,
    labels=['3', '4', '5'], ticks=(3, 4, 5),
    granularity=1, style=['radio'],
    color='Black', font='HelveticaBold',
    flip=False, depth=-5)
cont_text = visual.TextStim(win=win, name='cont_text',
    text='Click arrow to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
sync_text = visual.TextStim(win=win, name='sync_text',
    text='Choose a sync method',
    font='Arial',
    pos=(.3, .45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
slider_4 = visual.Slider(win=win, name='slider_4',
    size=(.3, .05), pos=(.3, 0.35), units=None,
    labels=['audio', 'diode', 'TTL'], ticks=(0, 1, 2),
    granularity=1, style=['radio'],
    color='black', font='HelveticaBold',
    flip=False, depth=-9)
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0.3, .1),     letterHeight=0.05,
     size=[.5, .2], borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)
text = visual.TextStim(win=win, name='text',
    text='Enter com port name (see readme for instructions)',
    font='Arial',
    pos=(.3, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-11.0);
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2',
    vertices=[[-(.1, .1)[0]/2.0,-(.1, .1)[1]/2.0], [+(.1, .1)[0]/2.0,-(.1, .1)[1]/2.0], [0,(.1, .1)[1]/2.0]],
    ori=90, pos=(.4, -.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-12.0, interpolate=True)
cont_mouse = event.Mouse(win=win)
x, y = [None, None]
cont_mouse.mouseClock = core.Clock()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Please figure out which image belongs to which side (left or right) by pressing the arrow keys.\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_trls = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix_cross = visual.ImageStim(
    win=win,
    name='fix_cross', 
    image='Cross.png', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "trl_img_loc"
trl_img_locClock = core.Clock()
stim = visual.ImageStim(
    win=win,
    name='stim', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
left = visual.ImageStim(
    win=win,
    name='left', 
    image='sin', mask=None,
    ori=0, pos=(-.6, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
right = visual.ImageStim(
    win=win,
    name='right', 
    image='sin', mask=None,
    ori=0, pos=(.6, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
key_resp_2 = keyboard.Keyboard()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-.75, -.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)

# Initialize components for Routine "feedback1"
feedback1Clock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI_2"
ISI_2Clock = core.Clock()
ISI_text = visual.TextStim(win=win, name='ISI_text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thank_you"
thank_youClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Thank you for your participation! Press esc to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "settings"-------
continueRoutine = True
# update component parameters for each repeat
slider.reset()
slider_2.reset()
slider_3.reset()
slider_4.reset()
# setup some python lists for storing info about the cont_mouse
cont_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
settingsComponents = [day_text, slider, set_text, slider_2, pergroup_text, slider_3, cont_text, sync_text, slider_4, textbox, text, polygon_2, cont_mouse]
for thisComponent in settingsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
settingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "settings"-------
while continueRoutine:
    # get current time
    t = settingsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=settingsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *day_text* updates
    if day_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        day_text.frameNStart = frameN  # exact frame index
        day_text.tStart = t  # local t and not account for scr refresh
        day_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(day_text, 'tStartRefresh')  # time at next scr refresh
        day_text.setAutoDraw(True)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    
    # *set_text* updates
    if set_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        set_text.frameNStart = frameN  # exact frame index
        set_text.tStart = t  # local t and not account for scr refresh
        set_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(set_text, 'tStartRefresh')  # time at next scr refresh
        set_text.setAutoDraw(True)
    
    # *slider_2* updates
    if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_2.frameNStart = frameN  # exact frame index
        slider_2.tStart = t  # local t and not account for scr refresh
        slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
        slider_2.setAutoDraw(True)
    
    # *pergroup_text* updates
    if pergroup_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pergroup_text.frameNStart = frameN  # exact frame index
        pergroup_text.tStart = t  # local t and not account for scr refresh
        pergroup_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pergroup_text, 'tStartRefresh')  # time at next scr refresh
        pergroup_text.setAutoDraw(True)
    
    # *slider_3* updates
    if slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_3.frameNStart = frameN  # exact frame index
        slider_3.tStart = t  # local t and not account for scr refresh
        slider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
        slider_3.setAutoDraw(True)
    
    # *cont_text* updates
    if cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cont_text.frameNStart = frameN  # exact frame index
        cont_text.tStart = t  # local t and not account for scr refresh
        cont_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_text, 'tStartRefresh')  # time at next scr refresh
        cont_text.setAutoDraw(True)
    if cont_text.status == STARTED:  # only update if drawing
        cont_text.setOpacity(cont_vis)
    if slider_4.getRating() is not None:
        if sync[slider_4.getRating()] == 'TTL':
            vis = 1
        else:
            vis = 0
        if slider_3.getRating() is not None:
            if slider_2.getRating() is not None:
                if slider.getRating() is not None:
                    cont_vis = 1
                else:
                    cont_vis = 0
            else:
                cont_vis = 0
        else:
            cont_vis = 0
    else:
        vis = 0
        cont_vis = 0
    
    # *sync_text* updates
    if sync_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sync_text.frameNStart = frameN  # exact frame index
        sync_text.tStart = t  # local t and not account for scr refresh
        sync_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sync_text, 'tStartRefresh')  # time at next scr refresh
        sync_text.setAutoDraw(True)
    
    # *slider_4* updates
    if slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_4.frameNStart = frameN  # exact frame index
        slider_4.tStart = t  # local t and not account for scr refresh
        slider_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
        slider_4.setAutoDraw(True)
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    if textbox.status == STARTED:  # only update if drawing
        textbox.setOpacity(vis)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:  # only update if drawing
        text.setOpacity(vis)
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:  # only update if drawing
        polygon_2.setOpacity(cont_vis)
    # *cont_mouse* updates
    if cont_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cont_mouse.frameNStart = frameN  # exact frame index
        cont_mouse.tStart = t  # local t and not account for scr refresh
        cont_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_mouse, 'tStartRefresh')  # time at next scr refresh
        cont_mouse.status = STARTED
        cont_mouse.mouseClock.reset()
        prevButtonState = cont_mouse.getPressed()  # if button is down already this ISN'T a new click
    if cont_mouse.status == STARTED:  # only update if started and not finished!
        buttons = cont_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [polygon_2]:
                    if obj.contains(cont_mouse):
                        gotValidClick = True
                        cont_mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in settingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "settings"-------
for thisComponent in settingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('day_text.started', day_text.tStartRefresh)
thisExp.addData('day_text.stopped', day_text.tStopRefresh)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('slider.started', slider.tStartRefresh)
thisExp.addData('slider.stopped', slider.tStopRefresh)
thisExp.addData('set_text.started', set_text.tStartRefresh)
thisExp.addData('set_text.stopped', set_text.tStopRefresh)
thisExp.addData('slider_2.response', slider_2.getRating())
thisExp.addData('slider_2.rt', slider_2.getRT())
thisExp.addData('slider_2.started', slider_2.tStartRefresh)
thisExp.addData('slider_2.stopped', slider_2.tStopRefresh)
thisExp.addData('pergroup_text.started', pergroup_text.tStartRefresh)
thisExp.addData('pergroup_text.stopped', pergroup_text.tStopRefresh)
thisExp.addData('slider_3.response', slider_3.getRating())
thisExp.addData('slider_3.rt', slider_3.getRT())
thisExp.addData('slider_3.started', slider_3.tStartRefresh)
thisExp.addData('slider_3.stopped', slider_3.tStopRefresh)
thisExp.addData('cont_text.started', cont_text.tStartRefresh)
thisExp.addData('cont_text.stopped', cont_text.tStopRefresh)
day = slider.getRating()
if day == 1:
    num_trls = 200
elif day == 2:
    num_trls = 250
thisExp.addData('day', day)

pic_set = slider_2.getRating()
if pic_set == 1:
    direc = 'Set1/'
elif pic_set == 2:
    direc = 'Set2/'
thisExp.addData('picture_set', pic_set)

import pandas as pd #for csv reading
num_per_group = slider_3.getRating()
if num_per_group == 3:
    img_grps = pd.read_csv('image_groups_3p.csv')
elif num_per_group == 4:
    img_grps = pd.read_csv('image_groups_4p.csv')
elif num_per_group == 5:
    img_grps = pd.read_csv('image_groups_5p.csv')
thisExp.addData('num_per_group', num_per_group)

sync_method = sync[slider_4.getRating()]
if sync_method == 'audio':
    audio = 1.5
    diode = 0
elif sync_method == 'diode':
    audio = 0
    diode = 1.5
else:
    import serial
    audio = 0
    diode= 0
    ser = serial.Serial(textbox.text, 19200, timeout = 1)
    ser.dtr = False;
thisExp.addData('sync_method', sync_method)
thisExp.addData('sync_text.started', sync_text.tStartRefresh)
thisExp.addData('sync_text.stopped', sync_text.tStopRefresh)
thisExp.addData('slider_4.response', slider_4.getRating())
thisExp.addData('slider_4.rt', slider_4.getRT())
thisExp.addData('slider_4.started', slider_4.tStartRefresh)
thisExp.addData('slider_4.stopped', slider_4.tStopRefresh)
thisExp.addData('textbox.text',textbox.text)
textbox.reset()
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('cont_mouse.started', cont_mouse.tStart)
thisExp.addData('cont_mouse.stopped', cont_mouse.tStop)
thisExp.nextEntry()
# the Routine "settings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
start_trls.keys = []
start_trls.rt = []
_start_trls_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, start_trls]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *start_trls* updates
    waitOnFlip = False
    if start_trls.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_trls.frameNStart = frameN  # exact frame index
        start_trls.tStart = t  # local t and not account for scr refresh
        start_trls.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_trls, 'tStartRefresh')  # time at next scr refresh
        start_trls.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_trls.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_trls.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_trls.status == STARTED and not waitOnFlip:
        theseKeys = start_trls.getKeys(keyList=['space'], waitRelease=False)
        _start_trls_allKeys.extend(theseKeys)
        if len(_start_trls_allKeys):
            start_trls.keys = _start_trls_allKeys[-1].name  # just the last key pressed
            start_trls.rt = _start_trls_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# check responses
if start_trls.keys in ['', [], None]:  # No response was made
    start_trls.keys = None
thisExp.addData('start_trls.keys',start_trls.keys)
if start_trls.keys != None:  # we had a response
    thisExp.addData('start_trls.rt', start_trls.rt)
thisExp.addData('start_trls.started', start_trls.tStartRefresh)
thisExp.addData('start_trls.stopped', start_trls.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=num_trls, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix_cross]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fix_cross.started', fix_cross.tStartRefresh)
    trials.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    
    # ------Prepare to start Routine "trl_img_loc"-------
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('group_pair', pair_ind);
    
    # choose center image
    image_sign = randint(0, 2*num_per_group) # choose randomly from 2 groups of images
    image_num = image_sign + 2*num_per_group*(pair_ind - 1) # get chosen image from correct set of groups
    stim_image = img_grps.loc[image_num, 'image']
    stim_group = img_grps.loc[image_num, 'group']
    stim_group_num = img_grps.loc[image_num, 'group_num']
    
    # choose in-group image
    in_group = img_grps[img_grps.group_num == stim_group_num]
    in_group = in_group[in_group.group != stim_group]
    in_group = in_group.reset_index()
    rand_in = randint(0, len(in_group))
    in_group_image = in_group.loc[rand_in, 'image']
    in_group_group = in_group.loc[rand_in, 'group']
    
    # choose out-group image
    if stim_group_num == 1: #add |3
        out_group_num = stim_group_num + 1
    elif stim_group_num == 3:
        out_group_num = stim_group_num + 1
    else:
        out_group_num = stim_group_num - 1
    out_group = img_grps[img_grps.group_num == out_group_num]
    out_group = out_group.reset_index()
    rand_out = randint(0, len(out_group))
    out_group_image = out_group.loc[rand_out, 'image']
    out_group_group = out_group.loc[rand_out, 'group']
    
    # test: in-group always left
    #left_image = in_group_image
    #right_image = out_group_image
    
    # randomly assign side
    side_sign = randint(0, 2) #non-inclusive (] for some reason
    if side_sign == 0:
        left_image = in_group_image
        right_image = out_group_image
    else:
        left_image = out_group_image
        right_image = in_group_image
        
    # save image choices
    thisExp.addData('stim_image', stim_image)
    thisExp.addData('left_image', left_image)
    thisExp.addData('right_image', right_image)
    
    # after 50 trials, move onto second set of image groups
    if day == 2:
        if trials.thisRepN == 49:
            pair_ind = 2;
            
    # send TTL if it is sync method
    if sync_method == 'TTL':
        ser.dtr = True;
    stim.setImage(direc + stim_image)
    left.setImage(direc + left_image)
    right.setImage(direc + right_image)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_1.setSound('A', secs=audio, hamming=True)
    sound_1.setVolume(1, log=False)
    # keep track of which components have finished
    trl_img_locComponents = [stim, left, right, key_resp_2, polygon, sound_1]
    for thisComponent in trl_img_locComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trl_img_locClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trl_img_loc"-------
    while continueRoutine:
        # get current time
        t = trl_img_locClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trl_img_locClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim* updates
        if stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim.frameNStart = frameN  # exact frame index
            stim.tStart = t  # local t and not account for scr refresh
            stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
            stim.setAutoDraw(True)
        if stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                stim.tStop = t  # not accounting for scr refresh
                stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim, 'tStopRefresh')  # time at next scr refresh
                stim.setAutoDraw(False)
        
        # *left* updates
        if left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left.frameNStart = frameN  # exact frame index
            left.tStart = t  # local t and not account for scr refresh
            left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left, 'tStartRefresh')  # time at next scr refresh
            left.setAutoDraw(True)
        if left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                left.tStop = t  # not accounting for scr refresh
                left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(left, 'tStopRefresh')  # time at next scr refresh
                left.setAutoDraw(False)
        
        # *right* updates
        if right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right.frameNStart = frameN  # exact frame index
            right.tStart = t  # local t and not account for scr refresh
            right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
            right.setAutoDraw(True)
        if right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                right.tStop = t  # not accounting for scr refresh
                right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right, 'tStopRefresh')  # time at next scr refresh
                right.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(sides[side_sign])) or (key_resp_2.keys == sides[side_sign]):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + diode-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + audio-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trl_img_locComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trl_img_loc"-------
    for thisComponent in trl_img_locComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # end TTL if it is sync method
    if sync_method == 'TTL':
        ser.dtr = False;
        
    if key_resp_2.corr:
        correct = 'CORRECT'
        thisExp.addData('ans_correctness', 1)
    else:
        correct = 'INCORRECT'
        thisExp.addData('ans_correctness', 0)
    if len(key_resp_2.keys) == 0:
        thisExp.addData('choice', None)
    else:
        thisExp.addData('choice', key_resp_2.keys)
    trials.addData('stim.started', stim.tStartRefresh)
    trials.addData('stim.stopped', stim.tStopRefresh)
    trials.addData('left.started', left.tStartRefresh)
    trials.addData('left.stopped', left.tStopRefresh)
    trials.addData('right.started', right.tStartRefresh)
    trials.addData('right.stopped', right.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(sides[side_sign]).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStartRefresh)
    trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    # the Routine "trl_img_loc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedback_text.setText(correct)
    # keep track of which components have finished
    feedback1Components = [feedback_text]
    for thisComponent in feedback1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback1"-------
    for thisComponent in feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedback_text.started', feedback_text.tStartRefresh)
    trials.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    
    # ------Prepare to start Routine "ISI_2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_2Components = [ISI_text]
    for thisComponent in ISI_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISI_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISI_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISI_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_text* updates
        if ISI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_text.frameNStart = frameN  # exact frame index
            ISI_text.tStart = t  # local t and not account for scr refresh
            ISI_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_text, 'tStartRefresh')  # time at next scr refresh
            ISI_text.setAutoDraw(True)
        if ISI_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ISI_text.tStop = t  # not accounting for scr refresh
                ISI_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISI_text, 'tStopRefresh')  # time at next scr refresh
                ISI_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI_2"-------
    for thisComponent in ISI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ISI_text.started', ISI_text.tStartRefresh)
    trials.addData('ISI_text.stopped', ISI_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed num_trls repeats of 'trials'


# ------Prepare to start Routine "thank_you"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
thank_youComponents = [end_text]
for thisComponent in thank_youComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thank_youClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thank_you"-------
while continueRoutine:
    # get current time
    t = thank_youClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thank_youClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thank_you"-------
for thisComponent in thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# the Routine "thank_you" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
