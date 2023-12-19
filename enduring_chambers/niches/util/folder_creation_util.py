"""
Folder Creation Util Module
"""
import os
from dotenv import load_dotenv
load_dotenv()

def create_folder(folder_name:str):
    """
    Creates a folder in the route

    Arguments:
        folder_name : str
            Name of the folder to be created
    """
    # Create the folder
    folder_path = os.path.join(os.path.curdir, folder_name)

    try:
        os.makedirs(folder_path)
    except FileExistsError:
        pass
    except Exception:
        pass
