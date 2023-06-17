# Phish-Phryer
Phish-Phryer is a Python-based application for feeding falsified information to phishing sites.

### Disclaimer
This software is provided AS IS and has no warranty whatsoever. I am not responsible for any damage done to any entity due to anything pertaining to this project.

# Docker Setup
There are two docker containers in this project: one for the cli and another for the webserver running the target phishing site.
Simply run 
```commandline
docker-compose up --detach
```

Then, the webserver should point to port **8080** on the local machine (and port 80 in the container).
- Go to http://127.0.0.1:8080 to reach the webserver

## Volumes within the Containers
Each container has a volume.

```
phish-phryer-cli-1          ->    phish-phryer/
phish-phryer-webserver-1    ->    webserver/
```

Therefore, updating any file in the volume on the local machine will update it within the container. This allows you to update the project in real-time.

## What Services are Running?
- nginx (Port 8080) for the webserver
- tor (Port 9050) for running requests (outside of development) on actual phishing sites

# CLI Use
In order to use the CLI, enter the container's CLI interface
```commandline
(phish-phryer-py3.11) $ docker container list     
CONTAINER ID   IMAGE                     COMMAND                  CREATED        STATUS         PORTS                  NAMES
4fd5362c4abf   nginx:mainline-bullseye   "/docker-entrypoint.…"   16 hours ago   Up 3 minutes   0.0.0.0:8080->80/tcp   phish-phryer-webserver-1
7e992be6c989   phish-phryer-cli          "python3"                16 hours ago   Up 3 minutes                          phish-phryer-cli-1
(phish-phryer-py3.11) $ docker exec -it 7e992be6c989 bash  
root@7e992be6c989:/phish-phryer#
```

Then enter the poetry shell (It won't work otherwise)

```commandline
root@7e992be6c989:/phish-phryer# poetry shell
Spawning shell within /root/.cache/pypoetry/virtualenvs/phish-phryer-82-V_4Ra-py3.11
root@7e992be6c989:/phish-phryer# . /root/.cache/pypoetry/virtualenvs/phish-phryer-82-V_4Ra-py3.11/bin/activate
(phish-phryer-py3.11) root@7e992be6c989:/phish-phryer#
```