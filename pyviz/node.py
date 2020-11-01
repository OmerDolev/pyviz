import docker
from main import *


class Node:
    def __init__(self, image='quay.io/prometheus/node-exporter:latest', client=docker.from_env()):
        self.image = image
        self.docker_client = client

    def run(self):
        docker_client = docker.from_env()
        docker_client.containers.run(image=self.image,
                                     detach=True,
                                     network_mode='container:prometheus',
                                     command='--path.rootfs=/host',
                                     pid_mode='host',
                                     volumes={
                                         '/': {'bind': '/host', 'mode': 'ro'}
                                     })
