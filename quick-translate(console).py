from ahk import AHK
import pyperclip
import tkinter as tk
from translate import Translator
import pyautogui

data = {
    "lang": 'en',
    "key": "q"
}

temp = input("Enter quick-translate output language(acronym)(default en): ")
if temp: data['lang'] = temp
temp = input("Enter quick-translate shortcut key(default q): ")
if temp: data['key'] = temp

ahk = AHK()
translator = Translator(to_lang=data['lang'])


def get_text():
    last_copy = pyperclip.paste()
    ahk.key_down('Control')
    ahk.key_press('c')
    ahk.key_up('Control')
    text = pyperclip.paste()
    pyperclip.copy(last_copy)
    return text


def translate(string):
    return translator.translate(string)


def show(string):
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry(f'+{pyautogui.position()[0]}+{pyautogui.position()[1] - 50}')
    root.attributes("-topmost", True)

    # label = tk.Label(root, text=string, font=16)
    label = tk.Button(root, text=string, font=16, command=root.quit)
    label.pack(side=tk.LEFT)

    root.mainloop()


def run():
    show(translate(get_text()))


ahk.add_hotkey(f'^{data["key"]}', callback=run)
ahk.start_hotkeys()
ahk.block_forever()
