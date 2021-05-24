"""
"""

from importlib import resources

import click
import icecream


@click.command()
@click.argument("services_csv", type=click.File())
def main(services_csv):
    headers = services_csv.readline()
    services = []
    for line in services_csv:
        host,port,proto,name,state,info = line.strip().split(",")
        if state == '"open"':
            services.append(
                    {
                        "host": host[1:-1],
                    "port": port[1:-1],
                    "proto": proto[1:-1],
                    "name": name[1:-1],
                    "state": state[1:-1],
                    "info": info[1:-1]

                        }
                    )
    for service in services:
        print(service)
