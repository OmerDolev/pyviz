# pyviz
A visibility mini-app running on Python

## About

This is a simple local visibility environment comprised from 3 containers.

A Prometheus container, a node_exporter container and a grafana container

## Installation & Usage
Before installing you need to have docker and python3 installed on your machine.
For mac and windows it can be docker desktop, and for linux it can be docker-ce for example.
Regular Python3 installation should suffice.

Steps:

1. Clone this respository to a local dir

2. run pip install -r requirements.txt

3. Now you can run the app. Here are examples of commands:

python3 ./pyviz/main.py --help

python3 ./pyviz/main.py

** The above command will use default values for arguments which you can see in the help output

python3 ./pyviz/main.py --prom-version v1.8.1 --retention 48h

## Notes

- When the app exits it removes all the containers it created.

- If a container failed to run for some reason, the app will print it's logs and exit
