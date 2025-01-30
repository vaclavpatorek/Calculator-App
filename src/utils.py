##
# @file utils.py
# @brief Utility functions
# @author Radim Mifka (xmifka00)
# @date April 2023

import os


##
# @brief Load HTML file
# @param file: path to HTML file
# @return: HTML file as string
def loadHTML(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"No such HTML file: {file}")

    with open(file, "r", encoding="utf8") as f:
        html = f.read()

    return str(html)
