from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import addHook
import subprocess


def open_wezterm_with_nvim():
    try:
        reviewer = mw.reviewer
        if reviewer.card:
            anki_note = reviewer.card.note()
            if 'Vault-Reference' in anki_note:
                try:
                    print(anki_note['Vault-Reference'])
                    note, header  = anki_note['Vault-Reference'].split('<br>')
                except:
                    note = None
                    header = None
                if note and header:
                    command = ["wezterm", "start", "--", "nvim", "-c", f"call OpenNeorgHeader('~/doc/vault/{note}', '{header}')"]
                    subprocess.Popen(command)
                else:
                    showInfo("Vault-Reference field is not valid")
            else:
                showInfo("Current note does not have a Vault-Reference field")
        else:
            showInfo("No card selected")
    except Exception as e:
        showInfo(f"Failed to open WezTerm with nvim: {e}")


def setup_shortcut():
    action = QAction("Open WezTerm with nvim", mw)
    action.setShortcut(QKeySequence("Ctrl+A"))
    action.triggered.connect(open_wezterm_with_nvim)
    mw.addAction(action)


addHook("profileLoaded", setup_shortcut)
