READ ME
If you run into bugs contact Ethan


****************
RUNNING PIPELINE
****************

You must export to a .json file w/ shortened filenames
  - Note, you can import any signals you want to export and the script should parse and export them to CSV, and place 0s for missing data in other trials so data lines up properly
  - You can name the .json whatever you like, make sure you select a new file path to save to in v3d



****************
RUNNING SCRIPT
****************
To run script: open up command prompt or terminal (type "cmd" in widows explorer, or command space and type "terminal" on macOS)
Ensure python is installed type "python3 --version"
If not installed: install python 3 - if on windows10 or later download from Microsoft store

type "pip3 --version"
type "pip3 install tk"


To run script change directory to folder the script is saved to:

type "cd *folder location*" e.g. my computer/documents/algorithm/
Then type: "python3 parse-v3d-json_v1.3.py"

***********************
ONCE SCRIPT IS RUNNING
***********************

Script will run and prompt you to select a file, select the json file you exported from Visual3D
will export as csv in same location as the json you selected
DONE
