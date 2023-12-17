# Enduring Chambers

### Installation

- Review  and install dependencies on requirements.txt
- Install and configure postgresql database
- Install and configure ftp server
- Configure .env file, based on .env_example
- run /script/db_creation.py

Build application script

```
pyinstaller -w -D --add-data ".env;." --add-data ".\log;.\log" --add-data ".\niches\tmp;.\niches\tmp" main.py
```

continue
