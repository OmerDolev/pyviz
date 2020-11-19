# imports
import argparse
import docker
from prom import *
from node import *
from grafana import *
import atexit
import time
import signal


def main():

    # adding arguments to parser
    parser.add_argument('--prom-version', dest='promver', default='latest', help='Prometheus version (default: latest)')
    parser.add_argument('--retention', dest='retention', default='48h', help='Prometheus version (default: 48h)')
    args = parser.parse_args()

    prom = Prom(client=docker_client, version=args.promver, storage_retention=args.retention)
    prom.run()
    print(docker_client.containers.list())
    node = Node(client=docker_client)
    node.run()
    grafana = Grafana(client=docker_client)
    grafana.run()

    while docker_client.containers.list():
        time.sleep(10)


def cleanup(dclient):
    for container in dclient.containers.list(all=True):
        container.remove(force=True)


if __name__ == '__main__':
    docker_client = docker.from_env()
    parser = argparse.ArgumentParser(description='getting prometheus version')
    atexit.register(cleanup, docker_client)
    main()
