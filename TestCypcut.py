#coding=utf-8
__author__ = 'Smaug'

from pywinauto import application
import time
import random

apppath = 'C:\Program Files\Friendess\CypCut\CypCut.exe'
apppathx64 = 'C:\Program Files (x86)\Friendess\CypCut\CypCut.exe'
app = application.Application()

def connect_to_program():
    try:
        app.connect_(path = apppath)
    except:
        app.connect_(path = apppathx64)
    global Cypcut, btnStart, btnPause, btnLoop, btnStop, btnWalk, btnLeft, btnFwd, btnBwd, btnRight, btnDirs
    Cypcut = app.window_(title_re = u'CypCut激光切割系统')

    btnStart = Cypcut.TRzBitBtn3
    btnPause = Cypcut.TRzBitBtn6
    btnLoop = Cypcut.TRzBitBtn7
    btnStop = Cypcut.TRzBitBtn2
    btnWalk = Cypcut.TRzBitBtn1

    btnLeft = Cypcut.TRzBmpButton3
    btnFwd = Cypcut.TRzBmpButton4
    btnBwd = Cypcut.TRzBmpButton6
    btnRight = Cypcut.TRzBmpButton2
    btnDirs = [btnLeft, btnRight, btnFwd, btnBwd]

def change_loop_settings():
    btnLoop.Click()
    time.sleep(1)
    global loopDlg, btnLoopIntv, btnLoopTimes, cbStartAfterConfirm, btnConfirm
    loopDlg = app.window_(title_re = u'循环加工设置')

    btnLoopIntv = loopDlg.TRzCalcEdit1
    btnLoopTimes = loopDlg.TRzCalcEdit2
    cbStartAfterConfirm = loopDlg.CheckBox1
    btnConfirm = loopDlg.TBitBtn2

    btnLoopIntv.TypeKeys('1.2')
    btnLoopTimes.TypeKeys('9998')

    if cbStartAfterConfirm.IsEnabled() == True:
        needmanualstart = False
        if cbStartAfterConfirm.GetCheckState() == False:
            cbStartAfterConfirm.Click()
    else:
        needmanualstart = True

    btnConfirm.Click()
    time.sleep(1)

    if needmanualstart:
        if btnStart.IsEnabled():
            btnStart.Click()
            time.sleep(random.uniform(0.1, 2))

def random_jog():
    time.sleep(1)
    random.shuffle(btnDirs)
    for btn in btnDirs:
        if random.random() > 0.5:
            Cypcut.TcxCheckBox6.ClickInput()
        time.sleep(0.5)
        btn.PressMouse()
        time.sleep(random.uniform(0.5, 3))
        btn.ReleaseMouse()

def change_param():
    time.sleep(1)
    Cypcut.TypeKeys('{F2}')
    time.sleep(1)
    paramDlg = app.window_(title_re = u'图层参数设置')
    value = random.uniform(0.1, 300)
    paramDlg.TRzCalcEdit30.TypeKeys('%.2f' % value)
    paramDlg[u'确定'].Click()
    time.sleep(1)



if __name__ == '__main__':
    connect_to_program()
    change_loop_settings()

    testfunclist = [random_jog, change_param]

    for cnt in range(1, 99999):
        btnPause.Click()

        random.shuffle(testfunclist)
        for func in testfunclist:
            func()

        btnStart.Click()
        time.sleep(random.uniform(0.1, 2))













