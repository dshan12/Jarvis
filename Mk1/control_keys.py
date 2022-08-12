import pyautogui
import time

class General_keys:
    def __init__(self):
        pass

    def SelectAll(self):
        pyautogui.hotkey('ctrl','a')

    def Cut(self):
        pyautogui.hotkey('ctrl','x')
        time.sleep(1)

    def Copy(self):
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)

    def Paste(self):
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        
    def History(self):
        pyautogui.hotkey('ctrl','h')

    def Download(self):
        pyautogui.hotkey('ctrl','j')

    def Undo(self):
        pyautogui.hotkey('ctrl','z')
    
    def Redo(self):
        pyautogui.hotkey('ctrl','y')
    
    def Save(self):
        pyautogui.hotkey('ctrl','s')
    
    def Enter(self):
        pyautogui.hotkey('enter')

    def Find(self):
        pyautogui.hotkey('ctrl','f')

class WindowOpt:
    def __init__(self):
        pass

    def openWindow(self):
        self.maximizeWindow()

    def closeWindow(self):
        pyautogui.hotkey('alt','F4')

    def minimizeWindow(self):
        pyautogui.hotkey('win','down')
        time.sleep(1)
        pyautogui.hotkey('win','down')

    def maximizeWindow(self):
        pyautogui.hotkey('win','up')

    def moveWindow(self, data):
        if "left" in data:
            pyautogui.hotkey('win','left')
        elif "right" in data:
            pyautogui.hotkey('win','right')
        elif "down" in data:
            pyautogui.hotkey('win','down')
        elif "up" in data:
            pyautogui.hotkey('win','up')
            
    def switchWindow(self):
        pyautogui.hotkey('alt','tab')

class TabOpt:
    def __init__(self):
        pass
    
    def switchTab(self):
        pyautogui.hotkey('ctrl','tab')

    def closeTab(self):
        pyautogui.hotkey('ctrl','w')

    def newTab(self):
        pyautogui.hotkey('ctrl','t')


    

def Ctrl_Keys(data):
    keys = General_keys()
    if "select all" in data:
        keys.SelectAll()
        print("Done")
    if "cut" in data:
        keys.Cut()
        print("Done")
    if "copy" in data:
        keys.Copy()
        print("Done")
    if "paste" in data or "test" in data:
        keys.Paste()
        print("Done")
    if "save" in data:
         keys.Save()
         print("Done")
    if "enter" in data or 'search' in data:
        keys.Enter()
        print("Done")
    elif "history" in data:
        keys.History()
        print("Done")
    elif "download" in data:
        keys.Download()
        print("Done")
    elif "undo" in data:
        keys.Undo()
        print("Done")
    elif "Redo" in data:
        keys.Redo()
        print("Done")
    elif "find" in data:
        keys.Find()
        print("Done")
    return

def Win_Opt(data):
    w=WindowOpt()
    if "open" in data:
        w.openWindow()
        print("Done")
    elif "close" in data:
        w.closeWindow()
        print("Done")        
    elif "mini" in data:
        w.minimizeWindow()
        print("Done")
    elif "max" in data:
        w.maximizeWindow()
        print("Done")
    elif "move" in data:
        w.moveWindow(data)
        print("Done")
    elif "switch" in data:
        w.switchWindow()
        print("Done")
    return

def Tab_Opt(data):
    t = TabOpt()
    if "new" in data:
        t.newTab()
        print("Done")
    elif "switch" in data or "move" in data:
        t.switchTab()
        print("Done")
    elif "close" in data or "delete" in data:
        t.closeTab()
        print("Done")
    return
