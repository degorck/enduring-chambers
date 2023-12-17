# Enduring Chambers

### Installation

- Review  and install dependencies on requirements.txt
- Install and configure postgresql database
- Install and configure ftp server
- Configure .env file, based on .env_example
- run /script/db_creation.py

Build application script without terminal

```
pyinstaller -w -D --add-data ".env;." --add-data ".\log;.\log" --add-data ".\tmp;.\tmp" main.py
```

Build application script with terminal

```
pyinstaller -n enduring_chambers_terminal -F --add-data ".env;." --add-data ".\log;.\log" --add-data ".\tmp;.\tmp" enduring_chambers.py
```

continue
