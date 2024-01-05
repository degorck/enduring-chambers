# Enduring Chambers

### Installation for development

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
pyinstaller -w -D --add-data ".env;." --add-data ".\log;.\log" --add-data ".\tmp;.\tmp" enduring_chambers.py
```

Build application script with terminal

```
pyinstaller -n enduring_chambers_terminal -F --add-data ".env;." --add-data ".\log;.\log" --add-data ".\tmp;.\tmp" enduring_chambers.py
```

Server installation.

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

Note: Be sure that the server has static ip configured.

Client installation.

1.  Run the setup.exe and navigate for installation folder
2.  Configure .env file located on installation folder, with the values from server. Be sure that the FTP_HOST and DB_HOST contains the IP of the main server.
3.  Finish the configurations on the .env file.
