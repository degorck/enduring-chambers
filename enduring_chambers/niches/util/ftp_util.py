"""
Ftp Util Module to manage images
"""
import datetime
import logging
from ftplib import FTP
import os
from dotenv import load_dotenv
from niches.util.folder_creation_util import create_folder

load_dotenv()
FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASSWORD = os.getenv("FTP_PASSWORD")
FTP_REMOTE_DIRECTORY = os.getenv("FTP_REMOTE_DIRECTORY")
TEMP_FILE_FOLDER = "." + os.getenv("TEMP_FILE_FOLDER")
create_folder(TEMP_FILE_FOLDER)

def __configure_routes_send_image(image_route):
    # Extract the drive and the rest of the path
    drive, path_without_drive = os.path.splitdrive(image_route)
    file_name = image_route.split("/")[-1]
    extension = file_name.split(".")[-1].lower()
    return [drive, path_without_drive, file_name, extension]

def send_image(image_route:str):
    """
    Send image to ftp server
    
    Arguments:
        image_route: str
            route of the image to send
    Returns:
        ftp_image_route: str
            route of the saved image on ftp server
    """
    with FTP(FTP_HOST) as ftp:
        # Login to the server
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        # Change to the remote directory
        ftp.cwd(FTP_REMOTE_DIRECTORY)

        image_details = __configure_routes_send_image(image_route)
                # Set name for file based on current date
        datetime_now = datetime.datetime.now()
        date = (str(datetime_now.year) + str(datetime_now.month) +
                str(datetime_now.day) + str(datetime_now.second))
        # New name for the file on the FTP server
        new_file_name_on_ftp = "image_" + date + "." + image_details[3]
        ftp.mkd(date)
        ftp.cwd(FTP_REMOTE_DIRECTORY + "/" + date)
        # Open the local file in binary mode
        with open(image_route, 'rb') as file:
            # Upload the file to the FTP server
            ftp.storbinary(f'STOR {os.path.basename(image_route)}', file)

        # Rename the file on the FTP server
        ftp.rename(os.path.basename(image_route), new_file_name_on_ftp)
    logging.debug("Se almacenó la imagen en: %s",
                  FTP_REMOTE_DIRECTORY + date + "/" + new_file_name_on_ftp)
    return FTP_REMOTE_DIRECTORY + date + "/" + new_file_name_on_ftp

def delete_image(image_route:str):
    """
    Deletes image to ftp server
    
    Arguments:
        image_route: str
            route of the image to send
    """
    with FTP(FTP_HOST) as ftp:
        # Login to the server
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)
        ftp.cwd(FTP_REMOTE_DIRECTORY)

        # Delete a file
        try:
            ftp.delete(image_route)
            logging.debug("Se eliminó la imagen")
        except Exception as e:
            logging.error("Error deleting file %s: %s", image_route, e)

        # Delete a directory
        folder_route = image_route.split("/")[-2] + "/"
        try:
            ftp.rmd(folder_route)
            logging.debug("Se eliminó la carpeta")
        except Exception as e:
            logging.error("Error deleting directory %s: %s", folder_route, e)

def download_image(image_route):
    """
    Downloads image to ftp server
    
    Arguments:
        image_route: str
            route of the image to download
    Returns:
        ftp_image_route: str
            route of the local saved image
    """
    image_details = __configure_routes_send_image(image_route)
    with FTP(FTP_HOST) as ftp:
        # Login to the server
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)
        ftp.cwd(FTP_REMOTE_DIRECTORY)

        # Change to the remote directory (optional)
        # ftp.cwd('/path/on/ftp/server/')

        # Open the local file in binary write mode

        file_name = "tmp." + image_details[3]
        local_file_path = os.path.join("." + TEMP_FILE_FOLDER, file_name)

        with open(local_file_path, 'wb') as local_file:
            # Download the file from the FTP server
            ftp.retrbinary(f'RETR {image_route}', local_file.write)

    logging.debug("Se descargó la imagen [%s]", TEMP_FILE_FOLDER + file_name)
    return TEMP_FILE_FOLDER + file_name
