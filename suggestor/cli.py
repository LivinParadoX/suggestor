from pymetasploit3.msfrpc import MsfRpcClient
from tabulate import tabulate
from pyfzf.pyfzf import FzfPrompt
import click

@click.command()
@click.option("--rpc-password")
@click.option("--rpc-port", default=55552)
@click.option("--rpc-server", default="127.0.0.1")
@click.option("--rpc-use-ssl", is_flag=True)
@click.option("--workspace")
def main(rpc_password, rpc_port, rpc_server, rpc_use_ssl, workspace):
    if rpc_password is None:
        rpc_password = click.prompt("Password", hide_input=True)
    client = MsfRpcClient(rpc_password, server=rpc_server, port=rpc_port, ssl=rpc_use_ssl)
    if workspace is None:
        workspace = FzfPrompt().prompt([workspace["name"] for workspace in client.db.workspaces.list])
    workspace = client.db.workspaces.workspace(workspace)
    services = workspace.services.find(only_up=True, limit=9223372036854775807)
    print(tabulate(services, headers="keys"))
