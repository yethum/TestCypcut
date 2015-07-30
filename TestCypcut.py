#coding=utf-8
__author__ = 'Smaug'

from pywinauto import application
import time
import random

app = application.Application()

apppath = 'C:\Program Files\Friendess\CypCut\CypCut.exe'
apppathx64 = 'C:\Program Files (x86)\Friendess\CypCut\CypCut.exe'


try:
    app.connect_(path = apppath)
except:
    app.connect_(path = apppathx64)

Cypcut = app.window_(title_re = u'CypCut激光切割系统')


# time.sleep(1)
# Cypcut.TypeKeys('{F2}')
# time.sleep(1)
# paramDlg = app.window_(title_re = u'图层参数设置')
# time.sleep(1)
# paramDlg.print_control_identifiers()


btnStart = Cypcut.TRzBitBtn3
btnPause = Cypcut.TRzBitBtn6
btnLoop = Cypcut.TRzBitBtn7
btnStop = Cypcut.TRzBitBtn2
btnWalk = Cypcut.TRzBitBtn1

btnLeft = Cypcut.TRzBmpButton3
btnFwd = Cypcut.TRzBmpButton4
btnBwd = Cypcut.TRzBmpButton6
btnRight = Cypcut.TRzBmpButton2

btnLoop.Click()
time.sleep(1)

loopDlg = app.window_(title_re = u'循环加工设置')

btnLoopIntv = loopDlg.TRzCalcEdit1
btnLoopTimes = loopDlg.TRzCalcEdit2
cbStartAfterConfirm = loopDlg.CheckBox1
btnConfirm = loopDlg.TBitBtn2

btnLoopIntv.TypeKeys('1.2')
btnLoopTimes.TypeKeys('9998')

if cbStartAfterConfirm.IsEnabled() == True:
    needManualStart = False
    if cbStartAfterConfirm.GetCheckState() == False:
        cbStartAfterConfirm.Click()
else:
    needManualStart = True

btnConfirm.Click()
time.sleep(1)

if needManualStart:
    btnStart.Click()
    time.sleep(random.uniform(1, 5))

btnDirs = [btnLeft, btnRight, btnFwd, btnBwd]

def randomJog():
    time.sleep(1)
    random.shuffle(btnDirs)
    for btn in btnDirs:
        # if random.random() > 0.5:
        Cypcut.TcxCheckBox6.PressMouse()
        time.sleep(0.1)
        Cypcut.TcvCheckBox6.ReleaseMouse()
        time.sleep(0.5)
        btn.PressMouse()
        time.sleep(random.uniform(0.5, 3))
        btn.ReleaseMouse()

def ChangeParam():
    time.sleep(1)
    Cypcut.TypeKeys('{F2}')
    time.sleep(1)
    paramDlg = app.window_(title_re = u'图层参数设置')
    value = random.uniform(0.1, 300)
    paramDlg.TRzCalcEdit30.TypeKeys('%.2f' % value)
    paramDlg[u'确定'].Click()
    time.sleep(1)


testfunclist = [randomJog, ChangeParam]

for cnt in range(1, 99999):
    btnPause.Click()

    random.shuffle(testfunclist)
    for func in testfunclist:
        func()

    btnStart.Click()
    time.sleep(random.uniform(0.1, 2))















