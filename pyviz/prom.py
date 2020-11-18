import docker
import os
from main import *


class Prom:
    def __init__(self, version="latest", storage_retention_days="2d", client=docker.from_env()):
        self.version = version
        self.storage_retention_days = storage_retention_days
        self.docker_client = client

    def run(self):
        docker_client = docker.from_env()
        current_workdir = os.getcwd()
        prom_command = ["--config.file=/etc/prometheus/prometheus.yml",
                        "--storage.tsdb.path=/prometheus",
                        "--web.console.libraries=/usr/share/prometheus/console_libraries",
                        "--web.console.templates=/usr/share/prometheus/consoles",
                        '--log.level=debug',
                        "--storage.tsdb.retention.time={0}".format(self.storage_retention_days)]

        docker_client.containers.run(image="prom/prometheus:{0}".format(self.version),
                                     name='prometheus',
                                     detach=True,
                                     command=' '.join(prom_command),
                                     ports={
                                         '9090/tcp': ('127.0.0.1', 9090),
                                         '9100/tcp': ('127.0.0.1', 9100),
                                         '3000/tcp': ('127.0.0.1', 3000)
                                     },
                                     volumes={
                                          '{0}/data/prometheus.yml'.format(current_workdir): {'bind': '/etc/prometheus/prometheus.yml', 'mode': 'ro'}
                                     })
