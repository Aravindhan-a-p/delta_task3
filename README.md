# ARCHIVE SERVER
clone my git repo "https://github.com/Aravindhan-a-p/delta_task3"
# run  database
```
python3.11 database.py
```
# run user.sh
if it doesnt work run the commands manually
# 1st run server script and then client script
```
python3.11 server.py
python3.11 client.py
```
enter username and passwd
# DOCKERING
from curr working dir run 
```
 docker compose up
```
and open new terminal and run
```
docker ps
```
get id of the container and run the client script
```
docker exec -it <ID> /bin/sh
client.py
```

