import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py", # Python interpreter will consider it as a local environment, which means we can import something from the folder
    "src/helper.py", # We will write all the functionality
    "src/prompt.py", # We will write the prompt
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]



for filepath in list_of_files:
    filepath= Path(filepath) # define the path type, it will ignore the(/) and create the files and folder
    filedir,filename=os.path.split(filepath)# For Separating the file and Folder name

    # Create the directory
    if filedir != "":       # Not  empty,present(if folder is present)
        os.makedirs(filedir,exist_ok=True) # Make directory, exist_ok=True:- If it is created then it won't be created again
        logging.info(f" Creating Directory ; {filedir} for the file: {filename}")

    # Creating the files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # Check  file not exists or check the size of the file,if it is empty ,if it is not empty then it will not replace it

        with open(filepath, "w" ) as f: # Create that file
            pass
            logging.info(f"Creating Empty File: {filepath}")


    else:
        logging.info(f"{filename} is already exists ")

# All Files And Folder will be created