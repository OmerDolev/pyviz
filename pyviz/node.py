import subprocess


class NodeExporter:
    def __init__(self, image):
        self.image = image

    def run(self):
        docker_command = ['docker run -d',
                          '{0}:latest'.format(self.image),
                          '--pid_mode="host"',
                          '-p 9100:9100',
                          '-v "/:/host:ro"',
                          '--path.rootfs=/host'
                          ]

        subprocess.run(' '.join(docker_command))
