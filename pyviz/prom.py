import subprocess
import os


class Prom:
    def __init__(self, version="latest", storage_retention_days="2"):
        self.version = version
        self.storage_retention_days = storage_retention_days

    def run(self):
        current_workdir = os.getcwdb()
        prom_command = ["/bin/prometheus", "--config.file=/etc/prometheus/prometheus.yml",
                        "--storage.tsdb.path=/prometheus",
                        "--web.console.libraries=/usr/share/prometheus/console_libraries",
                        "--web.console.templates=/usr/share/prometheus/consoles",
                        "--storage.tsdb.retention.time={0}".format(self.storage_retention_days)]

        docker_command = ['docker run -d',
                          '-v {0}/../data/prometheus.yml:/etc/prometheus/prometheus.yml'.format(current_workdir),
                          '-p 9090:9090',
                          "prom/prometheus:{0}".format(self.version),
                          ' '.join(prom_command)]

        subprocess.run(' '.join(docker_command))
