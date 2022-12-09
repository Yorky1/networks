#!/usr/local/bin/python3

import click
import typing as tp
import subprocess

HEADER_SIZE = 28


def ping(host: str, mtu: int) -> tp.Tuple[bool, str]:
    """
    Try to ping host with selected MTU
    """

    command = ['ping', '-c', '1', '-M', 'do', '-s', str(mtu), host]

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        return True, None
    except subprocess.CalledProcessError as err:
        return False, err.output.decode()


def check_connection_availability(host):
    is_available, err = ping(host, 0)
    if not is_available:
        print(f'Connection is unavailable, because of error:\n{err}')
        exit(0)


def find_max_right_bound(host) -> int:
    result = 1
    while ping(host, result)[0]:
        result *= 2
    return result


@click.command(help='Finds minimal MTU between your host and destination host')
@click.option('--host', required=True, type=str, help='Destination host')
def find_min_mtu(host):
    check_connection_availability(host)

    left_bound = 0
    right_bound = find_max_right_bound(host)

    while right_bound - left_bound > 1:
        middle = (left_bound + right_bound) // 2
        if ping(host, middle)[0]:
            left_bound = middle
        else:
            right_bound = middle

    print(
        f'Minimal MTU between local_host and {host} is {left_bound + HEADER_SIZE}')


if __name__ == '__main__':
    find_min_mtu()
