# Define file extensions and flags
EXT = .py
PYTHON = python3
ZIP_FILE = xmifka00_xpator00_xanton07_xbalaz12

# Define source files and output files
SRC_FILES = app
SRC_DEV = stddev

ifeq ($(OS),Windows_NT)
	RM = cmd /C del /S /Q
	MKDIR = cmd /C mkdir
	VENV_ACTIVATE = venv\Scripts\activate.bat &&
	PIP = venv\Scripts\pip.exe
	CP = xcopy /I /Y /S
	SLASH = \\
	ZIP = tar -a -c -f $(ZIP_FILE).zip $(ZIP_FILE)
	RMDIR = cmd /C rmdir /S /Q
	RMVENV = if exist venv (rmdir /S /Q venv)
	RMDOX = if exist ..\doxygen (rmdir /S /Q ..\doxygen)
	RMCACHE = if exist __pycache__ (rmdir /S /Q __pycache__) &&\
	if exist ..\__pycache__ (rmdir /S /Q ..\__pycache__) &&\
	if exist .\tests\__pycache__ (rmdir /S /Q .\tests\__pycache__) &&\
	if exist .\exceptions\__pycache__ (rmdir /S /Q .\exceptions\__pycache__) &&\
	if exist .pytest_cache (rmdir /S /Q .pytest_cache) &&\
	if exist ..\.pytest_cache (rmdir /S /Q ..\.pytest_cache) &&\
	if exist .\tests\.pytest_cache (rmdir /S /Q .\tests\.pytest_cache) &&\
	if exist .\exceptions\.pytest_cache (rmdir /S /Q .\exceptions\.pytest_cache)
else
	RM = rm -rf
	MKDIR = mkdir -p $(dir $@)
	VENV_ACTIVATE = . venv/bin/activate &&
	PIP = venv/bin/pip
	CP = cp -r
	SLASH = /
	ZIP = zip -r $(ZIP_FILE).zip $(ZIP_FILE)
	RMDIR = rm -rf
	RMVENV = rm -rf venv
	RMDOX = rm -rf ../doxygen
	RMCACHE = rm -rf __pycache__ &&\
	rm -rf ../__pycache__ &&\
	rm -rf ./tests/__pycache__ &&\
	rm -rf ./exceptions/__pycache__ &&\
	rm -rf .pytest_cache &&\
	rm -rf ../.pytest_cache &&\
	rm -rf ./tests/.pytest_cache &&\
	rm -rf ./exceptions/.pytest_cache
endif

ZIP_PATH = ..$(SLASH)..$(SLASH)xmifka00_xpator00_xanton07_xbalaz12

.PHONY: all clean run test doc pack

all: venv $(SRC_FILES)
	$(VENV_ACTIVATE) $(PIP) install -r requirements.txt --quiet --disable-pip-version-check

clean:
	$(RMVENV)
	$(RMDOX)
	$(RMCACHE)

run: all
	$(VENV_ACTIVATE) $(PYTHON) $(addsuffix $(EXT), $(SRC_FILES))

profile: all
	$(VENV_ACTIVATE) echo 10 20 30 40 | $(PYTHON) $(addsuffix $(EXT), $(SRC_DEV))

test:
	$(VENV_ACTIVATE) pytest

doc:
	doxygen Doxyfile

pack: clean doc
	$(MKDIR) $(ZIP_PATH)$(SLASH)repo
	$(MKDIR) $(ZIP_PATH)$(SLASH)install
	$(MKDIR) $(ZIP_PATH)$(SLASH)doc
	$(CP) ..$(SLASH)installers$(SLASH)  $(ZIP_PATH)$(SLASH)install
	$(CP) ..$(SLASH)  $(ZIP_PATH)$(SLASH)repo
	$(CP) ..$(SLASH)doxygen$(SLASH)  $(ZIP_PATH)$(SLASH)doc
	$(RMDIR) $(ZIP_PATH)$(SLASH)repo$(SLASH)doxygen
	$(RMDIR) $(ZIP_PATH)$(SLASH)repo$(SLASH)installers
	cd ..$(SLASH)..$(SLASH) && $(ZIP) && $(RMDIR) $(ZIP_FILE)

venv:
	$(PYTHON) -m venv venv

$(SRC_FILES): requirements.txt | venv
