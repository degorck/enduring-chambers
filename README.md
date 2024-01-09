# Enduring Chambers

## Installation for development

1.  Configure INITIAL_ADMIN_PASSWORD on .env file
2.  Run salt_and_password_generator.py, copy the result
3.  Configure SALT on .env file, based on the salt_and_password_generator.py
4.  Review  and install dependencies on requirements.txt
5.  Install and configure postgresql database
6.  Install and configure ftp server
7.  Configure .env file, based on .env_example
8.  run /script/db_creation.py

Build application script without terminal

```
pyinstaller -w -F -i .\icon\enduring_chambers_initials.ico enduring_chambers.py
```

Build application script with terminal

```
pyinstaller -n enduring_chambers_terminal -F -i .\icon\enduring_chambers_initials_terminal.ico enduring_chambers.py
```

## Server installation.

1.  Run the setup.exe and navigate for installation folder
2.  Install postgresql and create an user and database for this project.
3.  Install the FTP server, and create an user for this project.
4.  Configure .env file located on installation folder with the values for FTP and DB (Postgresql)
5.  Configure INITIAL_ADMIN_PASSWORD on .env file
6.  Run salt_and_password_generator.py, copy the result and save it.
7.  Configure SALT on .env file, based on the salt_and_password_generator.py
8.  Configure INITIAL_ADMIN_HASHED_PASSWORD on .env file, based on the salt_and_password_generator.py
9.  Run db_creation.py
10. Finish the configurations on the .env file
11. Save the .env file in a safe place. It will be required for other installations.
12. Allow remote connections for FTP, addind a firewall rule for the connection port (default is port 21)
13. Allow remote connections for DB, adding a firewall rule for the connecction port (default port is 5432)
14. Modify the pg_hba.conf file, adding  your _**network gateway IP**_ in the line:  ***host    all             all             192.168.86.1/24            md5***

Note: Be sure that the server has static ip configured.

## Client installation.

1.  Run the setup.exe and navigate for installation folder
2.  Configure .env file located on installation folder, with the values from server. Be sure that the FTP_HOST and DB_HOST contains the IP of the main server.
3.  Finish the configurations on the .env file.

## .env File Constants

_**Database configuration**_

DB_NAME: Name of the database for the project

DB_USER: Database user for the project

DB_PASSWORD: Password of the database user

DB_PORT: Port of the database installation

DB_HOST: IP of the server that host the database. ("**localhost**" or "**127.0.0.1**" can be used if the database is hosted in the same PC that the client)

_**FTP configuration**_

FTP_HOST: IP of the server that host the ftp server. ("**localhost**" or "**127.0.0.1**" can be used if the ftp server is hosted in the same PC that the client)

FTP_USER: User of the ftp server

FTP_PASSWORD: Password of the ftp user.

_**Hash configuration**_

INITIAL_ADMIN_PASSWORD: First password of the admin user of the project. Is recomended to change the password inmediatly.

SALT: Is a random value that will be used to hash the password of all users.

INITIAL_ADMIN_HASHED_PASSWORD: First password of the admin user, hashed with "SALT".

_**Ftp remote directory**_

FTP_REMOTE_DIRECTORY: Is the folder on the ftp directory that will store all the images for deceased. Is recomended to use "/images/" as default

_**Log configuration**_

CONSOLE_LOG_ENABLED: Indicates if the logs shows in the console. Only valid values are "True" or "False". Recommended to use "False" as default.

LOGGING_LEVEL: Indicates the level of the logs that will be shown. Valid names "INFO", "DEBUG", "WARNING", "ERROR and "CRITICAL". Recommentede to use "DEBUG" as default.

LOG_FOLDER = Is the local folder where the logs will be stored. Is recomended to use "/log/" as default.

DAY_LIMIT: Indicates the number of days that the logs will be saved. All the older files that this value will be deleted. Recommended to use 7 as default.

TEMP_FILE_FOLDER: Is the local folder where the local images will be stored. Is recomended to use "/tmp/" as default.
