# Phish-Phryer
Phish-Phryer is a Python-based application for feeding falsified information to phishing sites.

# Docker Setup
To set up the docker container, simply run the docker_run.sh script contained in the "docker" directory
```commandline
./docker_run.sh
```
If you need to modify the starting port, file locations, or container name, simply edit the 'docker.config' file in the docker folder.

The structure of the docker.config file is, by default, as follows:
```
website_files=index
docker_port=8000
internal_port=80
container_name=phish-server
```

To verify if the container is online, go to the address:
http://127.0.0.1:{docker_port}
Note, http is used because the internal port used is 80. Other ports may require other methods of accessing.
