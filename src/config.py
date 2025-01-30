##
# @file config.py
# @brief Config file for apllication
# @author Radim Mifka (xmifka00)
# @date April 2023

import pathlib

TITLE = "Calcify"

# WIDTHxHEIGHT in pixels
# OPTIONAL
SIZE = "700x600"
MINSIZE_WIDTH = 300
MINSIZE_HEIGHT = 450

# Entry Config
ENTRY_FONT_FAMILY = "Cambria"
ENTRY_FONT_SIZE = 60

ENTRY_BACKGROUND_COLOR = "#303030"
ENTRY_FOREGROUND_COLOR = "white"
ENTRY_ICURSOR_COLOR = "#FF9500"
ENTRY_SELECT_COLOR = "#FF9500"

# Scrollbar config
SCROLLBAR_FOREGROUND_COLOR = "#444444"
SCROLLBAR_BACKGROUND_COLOR = "#303030"

# Button Config
BUTTON_FONT_FAMILY = "Cambria"
BUTTON_FONT_SIZE = 15

BUTTON_BACKGROUND_COLOR = "#303030"
BUTTON_HOVER_COLOR = "#444444"
BUTTON_FOREGROUND_COLOR = "white"
BUTTON_BORDER_COLOR = "#444444"

INFO_BUTTON_FONT_FAMILY = "Arial Bold"
INFO_BUTTON_FONT_SIZE = 15

SRC_PATH = pathlib.Path(__file__).parent.resolve()

INFO_TEXT_FILE = SRC_PATH / "info.html"
CALCULATOR_ICON = SRC_PATH / "calculator.ico"

# temporary buttons, any amount can be added
COLUMNS = 4
BUTTONS = [
    'C', '←', '→', '⌫',
    '(', ')', 'ln', 'log',
    '√', '^', '*', '%',
    '7', '8', '9', '÷',
    '4', '5', '6', '+',
    '1', '2', '3', '-',
    '0', '.', '!', '=',
]

OPS = [
    '+',
    '-',
    '*',
    '÷',
    '%',  # mod
    '^',
    '√',
    'log',
    'ln',
    '!',
]

PRECEDENCE = {"+": 1,
              "-": 1,
              "*": 2,
              '÷': 2,
              '%': 2,  # mod
              "^": 3,
              '√': 3,
              'log': 4,  # log
              'ln': 4,  # ln
              '!': 4,
              }

ERRORS = [
    "SyntaxError",
    "MathError",
    "UnknownError",
]

ENABLED_CHARACTERS = "long" + "".join(ERRORS)
