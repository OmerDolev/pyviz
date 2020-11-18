import docker
import os


class Grafana:
    def __init__(self, image="grafana/grafana:latest", client=docker.from_env()):
        self.image = image
        self.docker_client = client

    def run(self):
        current_workdir = os.getcwd()

        self.docker_client.containers.run(image=self.image,
                                          name='grafana',
                                          detach=True,
                                          network_mode='container:prometheus',
                                          volumes={
                                              '{0}/data/grafana-datasource.yml'.format(current_workdir): {
                                                  'bind': '/etc/grafana/provisioning/datasources/datasource.yml',
                                                  'mode': 'ro'},
                                              '{0}/data/node-exporter-full.json'.format(current_workdir): {
                                                  'bind': '/etc/grafana/provisioning/dashboards/node-exporter-full.json',
                                                  'mode': 'ro'},
                                              '{0}/data/dashboard.yml'.format(current_workdir): {
                                                  'bind': '/etc/grafana/provisioning/dashboards/dashboard.yml',
                                                  'mode': 'ro'}
                                          })
