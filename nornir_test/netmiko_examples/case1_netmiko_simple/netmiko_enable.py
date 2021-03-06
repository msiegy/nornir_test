from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir_test.nornir_utilities import nornir_set_creds


def netmiko_test(task):
    net_connect = task.host.get_connection("netmiko", task.nornir.config)
    net_connect.enable()
    task.run(netmiko_send_command, command_string="show ip int brief", use_textfsm=True)


def main():
    norn = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(norn)
    result = norn.run(netmiko_test, num_workers=20)
    print_result(result)


if __name__ == "__main__":
    main()
