##
# @file gui.py
# @brief GUI class for Calculator
# @author Radim Mifka (xmifka00)
# @date April 2023

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from tkhtmlview import HTMLLabel

import styles
from calculator import calculate
from config import (BUTTON_BORDER_COLOR, BUTTONS, CALCULATOR_ICON, COLUMNS,
                    ENABLED_CHARACTERS, ENTRY_BACKGROUND_COLOR,
                    ENTRY_FONT_FAMILY, ENTRY_FONT_SIZE, INFO_TEXT_FILE,
                    MINSIZE_HEIGHT, MINSIZE_WIDTH, OPS, SIZE, TITLE)
from exceptions.syntax import SyntaxError
from utils import loadHTML

##
# @class GUI
# @brief GUI class for Calculator
# @return


class GUI:
    ##
    # @brief Constructs a new GUI object.
    # @param self A pointer to the object.
    # @return None
    def __init__(self) -> None:
        self.title = TITLE
        self.size = SIZE
        self.display_value = ""
        self.last_display_value = ""
        self.info = False
        self.error = False
        self.generate_widgets()

    ##
    # @brief Starts the GUI.
    # @param self A pointer to the object.
    # @return None
    def generate_widgets(self):
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(self.size)
        self.window.minsize(MINSIZE_WIDTH, MINSIZE_HEIGHT)
        self.window.iconbitmap(CALCULATOR_ICON)
        self.window.bind('<KeyRelease>', self.move_view)
        self.style = styles.load(self.window)

        self.font = Font(family=ENTRY_FONT_FAMILY, size=ENTRY_FONT_SIZE)

        self.display_frame = tk.Frame(
            self.window, bg=ENTRY_BACKGROUND_COLOR, borderwidth=0)
        self.button_frame = tk.Frame(
            self.window, bg=ENTRY_BACKGROUND_COLOR, borderwidth=0)

        # setup the weight of the frames 1/3 and 2/3
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=2)

        self.display_frame.grid(row=0, column=0, sticky="nsew")
        self.button_frame.grid(row=1, column=0, sticky="nsew")

        self.display_entry = ttk.Entry(
            self.display_frame, font=self.font, cursor="arrow",
            validate="key", validatecommand=(self.display_frame.register(self.validate_entry), '%S'), justify="left")
        self.display_entry.place(relx=0, rely=0, relheight=self.display_frame.winfo_height(
        ), relwidth=self.display_frame.winfo_width())
        self.display_entry.focus()

        self.scrollbar = ttk.Scrollbar(
            self.display_frame, orient="horizontal", command=self.display_entry.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.display_entry.configure(xscrollcommand=self.scrollbar.set)

        self.info_button = ttk.Button(
            self.display_frame, text="Nápověda", command=self.info_callback, style="info.TButton")
        self.info_button.pack(side="bottom", anchor="se")

        self.info_frame = tk.Frame(self.window, bg="red")
        self.info_canvas = tk.Canvas(self.info_frame, borderwidth=0,
                                     highlightthickness=0, bg=ENTRY_BACKGROUND_COLOR)
        self.info_scrollbar = ttk.Scrollbar(
            self.info_frame, orient='vertical', command=self.info_canvas.yview)

        self.info_label = HTMLLabel(
            self.info_frame, html=loadHTML(INFO_TEXT_FILE), background=ENTRY_BACKGROUND_COLOR, bd=0, highlightthickness=0, pady=10, padx=10)
        self.info_label.pack(fill=tk.BOTH, expand=True)

        self.display_entry.bind('<Key>', self.bind_keys)
        self.display_entry.bind('<Control-c>', self.copy)
        self.display_entry.bind('<Control-v>', self.paste)
        self.generate_buttons()

    ##
    # @brief Generates the button widgets.
    # @param self A pointer to the object.
    # @return None
    def generate_buttons(self, event=None):
        for index, button in enumerate(BUTTONS):
            row = index // COLUMNS + 1
            col = index % COLUMNS
            self.button_frame.columnconfigure(col, weight=1)
            self.button_frame.rowconfigure(row, weight=1)
            btf = tk.Frame(self.button_frame,
                           background=BUTTON_BORDER_COLOR, borderwidth=1,)
            tk_b = ttk.Button(btf, text=button,
                              command=lambda button=button: self.button_callback(button))
            tk_b.pack(fill=tk.BOTH, expand=True)
            btf.grid(row=row, column=col, sticky="nsew")

    ##
    # @brief Move the cursor to the next valid position in the text editor.
    # @param self A pointer to the object.
    # @param right When set to True, move the cursor to the right valid position.
    #             Otherwise, move it to the left valid position.
    # @return index of the next valid position
    def next_valid_icursor(self, right=False):
        self.display_value = self.display_entry.get()
        if len(self.display_value) > 0:
            eindex = index = self.display_entry.index(tk.INSERT)
            if right:
                if self.display_value[index:index+2] == "ln":
                    eindex += 1
                if self.display_value[index:index+3] == "log":
                    eindex += 2
            else:
                if self.display_value[index-1] == "g":
                    eindex -= 2
                elif self.display_value[index-1] == "n":
                    eindex -= 1
            return eindex
        return 0

    ##
    # @brief Binds keyboard keys to calculator button callbacks.
    # @param event The tkinter event object representing the key that was pressed.
    # @return 'break' if the key press event should be ignored by Tkinter, otherwise None.
    def bind_keys(self, event):
        self.display_value = self.display_entry.get()
        if self.error:
            self.error = False
            self.button_callback("C")
        if event.keysym == "Return" or event.keysym == "KP_Enter":
            self.display_value = self.display_entry.get()
            self.button_callback("=")
        elif event.keysym == "c" or event.keysym == "C":
            self.button_callback("C")
        elif event.keysym == "Up":
            self.button_callback("Up")
        elif event.keysym == "slash":
            self.button_callback("÷")
        elif event.keysym == "r":
            self.button_callback("√")
            return 'break'
        elif event.keysym == "Left":
            self.display_entry.icursor(self.next_valid_icursor())
        elif event.keysym == "Right":
            self.display_entry.icursor(self.next_valid_icursor(right=True))
        elif event.keysym == "BackSpace":
            self.display_entry.delete(self.next_valid_icursor(), tk.INSERT)
        elif event.keysym == "Delete":
            self.display_entry.delete(
                tk.INSERT, self.next_valid_icursor(right=True))
        elif event.keysym == "l":
            self.display_entry.insert(tk.INSERT, "log")
            self.display_value = self.display_entry.get()
            return 'break'
        elif event.keysym == "n":
            self.display_entry.insert(tk.INSERT, "ln")
            self.display_value = self.display_entry.get()
            return 'break'
        elif event.keysym in ENABLED_CHARACTERS:
            return 'break'

    ##
    # @brief Moves the view of the display entry widget to the right if on the right edge.
    # @param self A pointer to the object.
    # @param event: Tkinter event object
    # @return None
    def move_view(self, event=None):
        index = self.display_entry.index(tk.INSERT)
        width = int(self.display_entry["width"])

        if index >= len(self.display_entry.get()) - width // 2:
            self.display_entry.xview_moveto(1.0)

    ##
    # @brief Copies the selected text, or the display value, to the clipboard.
    # @param self A pointer to the object.
    # @param event: Tkinter event object
    # @return None
    def copy(self, event):
        try:
            text = self.display_entry.selection_get()
            if text:
                self.window.clipboard_clear()
                self.window.clipboard_append(text)
        except tk.TclError:
            if self.display_value:
                self.window.clipboard_clear()
                self.window.clipboard_append(self.display_value)

    ##
    # @brief Pastes the clipboard contents to the display entry widget
    # @param self A pointer to the object.
    # @param event: Tkinter event object
    # @return None
    def paste(self, event):
        try:
            index = self.display_entry.index(tk.INSERT)
            self.display_entry.insert(index, self.window.clipboard_get())
            self.display_value = self.display_entry.get()
        except tk.TclError:
            pass

    ##
    # @brief Shows the error message on the display entry widget.
    # @param self A pointer to the object.
    # @param error: The error message to be shown.
    # @return None
    def show_error(self, error):
        self.display_value = error
        self.error = True

    ##
    # @brief Shows the info frame.
    # @param self A pointer to the object.
    # @return None
    def show_info(self):
        self.info_button.configure(text="Zpět")
        self.info_frame.grid(row=1, column=0, sticky="nsew")
        self.window.after(1, lambda: self.info_canvas.focus_set())
        self.window.after(1, lambda: self.info_label.focus_set())
        self.info = True

    ##
    # @brief Hides the info frame.
    # @param self A pointer to the object.
    # @return None
    def hide_info(self):
        self.info_button.configure(text="Nápověda")
        self.info_frame.grid_forget()
        self.info = False
        self.window.after(1, lambda: self.display_entry.focus_set())

    ##
    # @brief Toggles the info frame.
    # @param self A pointer to the object.
    # @return None
    def info_callback(self):
        if not self.info:
            self.show_info()
        else:
            self.hide_info()

    ##
    # @brief Callback for the calculator buttons.
    # @param self A pointer to the object.
    # @param button: The button that was pressed.
    # @return None
    def button_callback(self, button):
        if self.error:
            self.error = False
            self.button_callback("C")

        if button == "=":
            self.last_display_value = self.display_value
            try:
                result = calculate(self.display_value)
                self.display_value = str(result)
            except SyntaxError:
                self.show_error("Syntax Error")
            except ValueError:
                self.show_error("Math Error")
            except ZeroDivisionError:
                self.show_error("Math Error")
            except Exception:
                self.show_error("Unknown Error")
            self.reinsert_display()

        elif button == "C":
            self.display_value = ""
            self.reinsert_display()
        elif button == "Up":
            self.display_value = self.last_display_value
            self.reinsert_display()
        elif button == "⌫":
            self.display_entry.delete(self.next_valid_icursor()-1, tk.INSERT)
            self.display_value = self.display_entry.get()
        elif button == "←":
            self.display_entry.icursor(self.next_valid_icursor()-1)
        elif button == "→":
            self.display_entry.icursor(self.next_valid_icursor(right=True)+1)
        else:
            self.display_entry.insert(tk.INSERT, button)
            self.display_value = self.display_entry.get()

        if button != "→" and button != "←" and button != "⌫":
            self.move_view()
        self.window.after(1, lambda: self.display_entry.focus_set())

    ##
    # @brief Reinserts the display value to the display entry widget.
    # @param self A pointer to the object.
    # @return None
    def reinsert_display(self):
        index = self.display_entry.index(tk.INSERT)
        self.display_entry.delete(0, tk.END)
        self.display_entry.insert(0, self.display_value)
        self.display_entry.icursor(index+len(self.display_value))

    ##
    # @brief Validates the input of the display entry widget.
    # @param self A pointer to the object.
    # @param text: The text to be validated.
    # @return True if the text is valid, False otherwise.
    def validate_entry(self, text):
        for key in text:
            if not key.isdigit() and key not in OPS \
                    and key not in '.()' + ENABLED_CHARACTERS:
                return False
            return True

    ##
    # @brief mainloop of the GUI.
    # @param self A pointer to the object.
    # @return None
    def run(self):
        self.window.mainloop()
