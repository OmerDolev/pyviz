import docker
from main import *
import time


class Node:
    def __init__(self, image='quay.io/prometheus/node-exporter:latest', client=docker.from_env()):
        self.image = image
        self.docker_client = client

    def run(self):
        node_container = self.docker_client.containers.run(image=self.image,
                                                           name='node-exporter',
                                                           detach=True,
                                                           network_mode='container:prometheus',
                                                           command='--path.rootfs=/host',
                                                           volumes={
                                                               '/': {'bind': '/host', 'mode': 'ro'}
                                                           })

        time.sleep(5)
        if node_container.status != 'running' and node_container.status != 'created':
            print("node conatiner stopped running...\n")
            print("{0}".format(node_container.logs().decode("utf-8")))
            cleanup(self.docker_client)
            exit(2)
