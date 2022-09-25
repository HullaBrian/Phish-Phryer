import sys


arg = sys.argv[1]

with open("docker.config", "r") as file:
    for line in file.readlines():
        if line.split("=")[0] == arg:
            print(line.split("=")[1])
            break
