import docker
import os
from main import *
import time


class Prom:
    def __init__(self, version="latest", storage_retention="48h", client=docker.from_env()):
        self.version = version
        self.storage_retention = storage_retention
        self.docker_client = client

    def run(self):
        current_workdir = os.getcwd()

        if self.version.startswith("v1"):
            prom_command = ["-config.file=/etc/prometheus/prometheus.yml",
                            '-log.level=debug',
                            "-storage.local.retention={0}".format(self.storage_retention)]
        else:
            prom_command = ["--config.file=/etc/prometheus/prometheus.yml",
                            "--storage.tsdb.path=/prometheus",
                            "--web.console.libraries=/usr/share/prometheus/console_libraries",
                            "--web.console.templates=/usr/share/prometheus/consoles",
                            '--log.level=debug',
                            "--storage.tsdb.retention.time={0}".format(self.storage_retention)]

        prom_container = self.docker_client.containers.run(image="prom/prometheus:{0}".format(self.version),
                                                           name='prometheus',
                                                           detach=True,
                                                           command=' '.join(prom_command),
                                                           ports={
                                                               '9090/tcp': ('127.0.0.1', 9090),
                                                               '9100/tcp': ('127.0.0.1', 9100),
                                                               '3000/tcp': ('127.0.0.1', 3000)
                                                           },
                                                           volumes={
                                                               '{0}/data/prometheus.yml'.format(current_workdir): {
                                                                   'bind': '/etc/prometheus/prometheus.yml',
                                                                   'mode': 'ro'}
                                                           })

        time.sleep(5)
        if prom_container.status != 'running' and prom_container.status != 'created':
            print("prom conatiner stopped running...\n")
            print("{0}".format(prom_container.logs().decode("utf-8")))
            cleanup(self.docker_client)
            exit(2)
