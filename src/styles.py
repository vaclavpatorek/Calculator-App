##
# @file styles.py
# @brief Style definitions for ttk widgets
# @author Radim Mifka (xmifka00)
# @date April 2023

import tkinter as tk
from tkinter import ttk

from config import (BUTTON_BACKGROUND_COLOR, BUTTON_FONT_FAMILY,
                    BUTTON_FONT_SIZE, BUTTON_FOREGROUND_COLOR,
                    BUTTON_HOVER_COLOR, ENTRY_BACKGROUND_COLOR,
                    ENTRY_FOREGROUND_COLOR, ENTRY_ICURSOR_COLOR,
                    ENTRY_SELECT_COLOR, INFO_BUTTON_FONT_FAMILY,
                    INFO_BUTTON_FONT_SIZE, SCROLLBAR_BACKGROUND_COLOR,
                    SCROLLBAR_FOREGROUND_COLOR)


##
# @brief Load styles for ttk widgets
# @param window: window to load styles for
# @return: ttk style object
def load(window):
    style = ttk.Style(window)
    style.theme_use("default")
    style.configure("TButton",
                    font=(BUTTON_FONT_FAMILY, BUTTON_FONT_SIZE),
                    background=BUTTON_BACKGROUND_COLOR,
                    foreground=BUTTON_FOREGROUND_COLOR,
                    borderwidth=0)

    style.map("TButton",
              foreground=[('active', "white")],
              background=[('active', BUTTON_HOVER_COLOR)])

    style.configure("info.TButton",
                    foreground=ENTRY_ICURSOR_COLOR,
                    font=(INFO_BUTTON_FONT_FAMILY, INFO_BUTTON_FONT_SIZE))

    style.configure("TScrollbar",
                    background=SCROLLBAR_FOREGROUND_COLOR,
                    arrowcolor=SCROLLBAR_BACKGROUND_COLOR,
                    foreground=SCROLLBAR_FOREGROUND_COLOR,
                    troughcolor=SCROLLBAR_BACKGROUND_COLOR,
                    lightcolor="white",
                    borderwidth=0,
                    relief=tk.FLAT)

    style.map("TScrollbar",
              background=[('active', SCROLLBAR_FOREGROUND_COLOR)])

    style.configure("TEntry",
                    fieldbackground=ENTRY_BACKGROUND_COLOR,
                    foreground=ENTRY_FOREGROUND_COLOR,
                    insertcolor=ENTRY_ICURSOR_COLOR,
                    selectbackground=ENTRY_SELECT_COLOR,
                    insertwidth=2,
                    borderwidth=0,
                    )
    return style
