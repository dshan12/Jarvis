import shutil
from datetime import date
from pathlib import Path
import os
import time
import sys
import ctypes

from watchdog.events import FileSystemEventHandler

from Deskcleaner.extensions import extension_paths


def add_date_to_path(path: Path):
    """
    Helper function that adds current year/month to destination path. If the path
    doesn't already exist, it is created.

    :param Path path: destination root to append subdirectories based on date
    """
    dated_path = path / f'{date.today().year}' / f'{date.today().month:02d}'
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path


def rename_file(source: Path, destination_path: Path):
    """
    Helper function that renames file to reflect new path. If a file of the same
    name already exists in the destination folder, the file name is numbered and
    incremented until the filename is unique (prevents overwriting files).

    :param Path source: source of file to be moved
    :param Path destination_path: path to destination directory
    """
    if Path(destination_path / source.name).exists():
        increment = 0

        while True:
            increment += 1
            new_name = destination_path / f'{source.stem}_{increment}{source.suffix}'

            if not new_name.exists():
                return new_name
    else:
        return destination_path / source.name


class EventHandler(FileSystemEventHandler):
    def __init__(self, watch_path: Path, destination_root: Path):
        path, dirs, files = next(os.walk(watch_path))
        file_count = len(files)
        dir_count = len(dirs)
        self.watch_path = watch_path.resolve()
        self.destination_root = destination_root.resolve()
        self.file_count = file_count
        self.files = files
        self.dirs = dirs
        self.dir_count = dir_count

    def on_modified(self, event):
        while self.file_count > 0:
            for child in self.watch_path.iterdir():
                # skips directories and non-specified extensions
                if child.is_file() and child.suffix.lower() in extension_paths:
                    destination_path = self.destination_root / extension_paths[child.suffix.lower()]
                    destination_path = add_date_to_path(path=destination_path)
                    time.sleep(0.1)
                    destination_path = rename_file(source=child, destination_path=destination_path)
                    time.sleep(0.1)
                    shutil.move(src=child, dst=destination_path)
                self.file_count -= 1
        while self.dir_count > 0:
            for a in self.dirs:
                for child in (Path(f"{self.watch_path}\\{a}")).resolve().iterdir():
                    if child.is_file() and child.suffix.lower() in extension_paths:
                        destination_path = self.destination_root / extension_paths[child.suffix.lower()]
                        destination_path = add_date_to_path(path=destination_path)
                        destination_path = rename_file(source=child, destination_path=destination_path)
                        shutil.move(src=child, dst=destination_path)
                x = f"{self.watch_path}\\{a}"
                if x == str(self.destination_root):
                    return None
                else:
                    os.rmdir(f"{self.watch_path}\\{a}")
                    self.dirs.remove(a)

    def run_as_admin(argv=None, debug=False):
        shell32 = ctypes.windll.shell32
        if argv is None and shell32.IsUserAnAdmin():
            return True

        if argv is None:
            argv = sys.argv
        if hasattr(sys, '_MEIPASS'):
            arguments = map(str, argv[1:])
        else:
            arguments = map(str, argv)
        argument_line = u' '.join(arguments)
        executable = str(sys.executable)
        if debug:
            print('Command line: ', executable, argument_line)
        ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
        if int(ret) <= 32:
            return False
        return None
