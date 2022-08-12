#! /usr/bin/env python3


from time import sleep

from pathlib import Path

from watchdog.observers import Observer

from Deskcleaner.EventHandler import *

EventHandler.run_as_admin()

def activate(a, b):
    watch_path = Path(a)
    destination_root = Path(b)
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:
        while True:
            sleep(1)
    except:
        return
    observer.join()

def deactivate():
    observer.stop()

