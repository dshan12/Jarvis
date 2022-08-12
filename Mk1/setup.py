from cx_Freeze import setup, Executable

base = None    

executables = [Executable("jarvis.py", base=base)]

packages = ["idna", "requests", "speedtest", "cv2", "psutil", "pyautogui", "os", "sys", "pyjokes", "pyttsx3", "speech_recognition", "wikipedia", "winshell", "selenium", "translate", "youtubetaggenerator", "geocoder", "pytube", "numpy", "pandas", "cmake", "face_recognition", "screen_brightness_control", "watchdog", "pipwin", "uiautomation", "pyaudio"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Jarvis",
    options = options,
    version = "1",
    description = '<any description>',
    executables = executables
)
