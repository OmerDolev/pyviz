import docker
from main import *


class Node:
    def __init__(self, image='quay.io/prometheus/node-exporter:latest', client=docker.from_env()):
        self.image = image
        self.docker_client = client

    def run(self):
        docker_client = docker.from_env()
        docker_client.containers.run(image=self.image,
                                     name='node-exporter',
                                     detach=True,
                                     network_mode='container:prometheus',
                                     command='--path.rootfs=/host',
                                     volumes={
                                         '/': {'bind': '/host', 'mode': 'ro'}
                                     })
