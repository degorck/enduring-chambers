# Enduring Chambers v1.0.0

## Installation for development

1.  Configure INITIAL\_ADMIN\_PASSWORD on .env file
2.  Run salt\_and\_password\_generator.py, copy the result
3.  Configure SALT on .env file, based on the salt\_and\_password\_generator.py
4.  Review  and install dependencies on requirements.txt
5.  Install and configure postgresql database
6.  Install and configure ftp server
7.  Configure .env file, based on .env\_example
8.  run /script/db\_creation.py

Build application script without terminal

```
pyinstaller -w -F -i .\icon\enduring_chambers_initials.ico enduring_chambers.py
```

Build application script with terminal

```
pyinstaller -n enduring_chambers_terminal -F -i .\icon\enduring_chambers_initials_terminal.ico enduring_chambers.py
```

Packaged with **InstallForge**, compression level _**Normal.**_

## Server installation.

1.  Run the setup.exe and navigate for installation folder
2.  Install postgresql and create an user and database for this project.
3.  Install the FTP server, and create an user for this project.
4.  Configure .env file located on installation folder with the values for FTP and DB (Postgresql)
5.  Configure INITIAL\_ADMIN\_PASSWORD on .env file
6.  Run salt\_and\_password\_generator.py, copy the result and save it.
7.  Configure SALT on .env file, based on the salt\_and\_password\_generator.py
8.  Configure INITIAL\_ADMIN\_HASHED\_PASSWORD on .env file, based on the salt\_and\_password\_generator.py
9.  Run db\_creation.py
10.  Finish the configurations on the .env file
11.  Save the .env file in a safe place. It will be required for other installations.
12.  Allow remote connections for FTP, addind a firewall rule for the connection port (default is port 21)
13.  Allow remote connections for DB, adding a firewall rule for the connecction port (default port is 5432)
14.  Modify the pg\_hba.conf file, adding  your _**network gateway IP**_ in the line:  _**host    all             all             192.168.86.1/24            md5**_

Note: Be sure that the server has static ip configured.

## Client installation.

1.  Run the setup.exe and navigate for installation folder
2.  Configure .env file located on installation folder, with the values from server. Be sure that the FTP\_HOST and DB\_HOST contains the IP of the main server.
3.  Finish the configurations on the .env file.

## .env File Constants

_**Database configuration**_

DB\_NAME: Name of the database for the project

DB\_USER: Database user for the project

DB\_PASSWORD: Password of the database user

DB\_PORT: Port of the database installation

DB\_HOST: IP of the server that host the database. ("**localhost**" or "**127.0.0.1**" can be used if the database is hosted in the same PC that the client)

_**FTP configuration**_

FTP\_HOST: IP of the server that host the ftp server. ("**localhost**" or "**127.0.0.1**" can be used if the ftp server is hosted in the same PC that the client)

FTP\_USER: User of the ftp server

FTP\_PASSWORD: Password of the ftp user.

_**Hash configuration**_

INITIAL\_ADMIN\_PASSWORD: First password of the admin user of the project. Is recomended to change the password inmediatly.

SALT: Is a random value that will be used to hash the password of all users.

INITIAL\_ADMIN\_HASHED\_PASSWORD: First password of the admin user, hashed with "SALT".

_**Ftp remote directory**_

FTP\_REMOTE\_DIRECTORY: Is the folder on the ftp directory that will store all the images for deceased. Is recomended to use "/images/" as default

_**Log configuration**_

CONSOLE\_LOG\_ENABLED: Indicates if the logs shows in the console. Only valid values are "True" or "False". Recommended to use "False" as default.

LOGGING\_LEVEL: Indicates the level of the logs that will be shown. Valid names "INFO", "DEBUG", "WARNING", "ERROR and "CRITICAL". Recommended to use "DEBUG" as default.

LOG\_FOLDER = Is the local folder where the logs will be stored. Is recomended to use "/log/" as default.

DAY\_LIMIT: Indicates the number of days that the logs will be saved. All the older files that this value will be deleted. Recommended to use 7 as default.

TEMP\_FILE\_FOLDER: Is the local folder where the local images will be stored. Is recomended to use "/tmp/" as default.

## Generate icon package

pyside6-rcc enduring\_chambers\_initials.qrc -o enduring\_chambers\_initials\_rc.py

## Chagelog

### 1.0.0

*   Allows to write and update deceased with unknown death and birth dates.
*   Show "last record" in the window for niche creation
*   Adds "is\_donated" field to database for all niches
*   All tables are no ordered by database id
*   Allows to write holders without maternal surname
*   Improves performance (does not show all records by request)
*   Improves payments windows and functionality
*   Adds more control with .env file