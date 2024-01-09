from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import addHook
import subprocess
def open_wezterm_with_nvim():
    try:
        reviewer = mw.reviewer
        if reviewer.card:
            note = reviewer.card.note()
            if 'Vault-Reference' in note:
                field_value = note['Vault-Reference']
                if field_value:
                    command = ["wezterm", "start", "--", "nvim", field_value]
                    subprocess.Popen(command)
                else:
                    showInfo("No vault reference in current card")
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
