<img src="https://socialify.git.ci/hullabrian/Phish-Phryer/image?description=1&descriptionEditable=Anyone%20up%20for%20a%20phish%20phry%3F&font=Bitter&language=1&name=1&pattern=Solid&theme=Dark">

# Phish-Phryer
Phish-Phryer is a Python-based application for feeding falsified information to phishing sites.

**Currently, Phish-Phryer is not in a very useful state, but is currently public to showcase its project structure**

### Disclaimer
This software is provided AS IS and has no warranty whatsoever. I am not responsible for any damage done to any entity due to anything pertaining to this project.

# Docker Setup
There are two docker containers in this project: one for the cli and another for the webserver running the target phishing site.
Simply run 
```shell
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
```shell
docker exec -it phish-phryer_cli_1 bash  
```

Then enter the poetry shell (It won't work otherwise)

```shell
poetry shell
```
