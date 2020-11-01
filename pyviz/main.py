# imports
import argparse
import docker
from prom import *
from node import *
import atexit
import time
import signal


def main():
    prom = Prom(client=docker_client)
    prom.run()
    print(docker_client.containers.list())
    node = Node(client=docker_client)
    node.run()

    while docker_client.containers.list():
        time.sleep(10)


def receive_signal():
    for container in docker_client.containers.list():
        container.stop()


if __name__ == '__main__':
    # signal.signal(signal.SIGHUP, receive_signal)
    # signal.signal(signal.SIGINT, receive_signal)
    # signal.signal(signal.SIGQUIT, receive_signal)
    # signal.signal(signal.SIGILL, receive_signal)
    # signal.signal(signal.SIGTRAP, receive_signal)
    # signal.signal(signal.SIGABRT, receive_signal)
    # signal.signal(signal.SIGBUS, receive_signal)
    # signal.signal(signal.SIGFPE, receive_signal)
    docker_client = docker.from_env()
    # atexit.register(receive_signal)
    main()
