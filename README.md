# Phish-Phryer
Phish-Phryer is a Python-based application for feeding falsified information to phishing sites.

# Docker Setup
There are two docker containers in this project: one for the cli and another for the webserver running the target phishing site.
Simply run ```$ docker-compose up --detach```

Then, the webserver should point to port **8080** on the local machine (and port 80 in the container).
- Go to http://127.0.0.1:8080 to reach the webserver

## Volumes within the Containers
Each container has a volume.

```
phish-phryer-cli-1          ->    phish-phryer/
phish-phryer-webserver-1    ->    webserver/
```

Therefore, updating any file in the volume on the local machine will update it within the container. This allows you to update the project in real-time.

# CLI Use
In order to use the CLI, enter the container's CLI interface, then enter the poetry shell (It won't work otherwise)

```$ poetry shell```