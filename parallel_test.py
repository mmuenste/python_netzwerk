"""Paralleles Sichern der Config"""

from netmiko import ConnectHandler
import concurrent.futures
from getpass import getpass
import time

def save_config(device:dict):
    
    with ConnectHandler(**device) as net_connect:
        host = device["ip"]
        print(f"{host}...connected")
        config = net_connect.send_command("show run")
        filename = f"{host.replace('.', '_')}_{time.strftime('%Y%m%d_%H%M%S')}.config"
        with open(filename, "w") as fobj:
            fobj.write(config)
    
def main():

    user = input('Username: ')
    passw = getpass()

    devices = [{'ip': '192.168.181.21',
            'device_type': 'cisco_nxos',
            'username': user,
            'password': passw},
           {'ip': '192.168.181.22',
            'device_type': 'cisco_nxos',
            'username': user,
            'password': passw},
           {'ip': '192.168.181.23',
            'device_type': 'cisco_nxos',
            'username': user,
            'password': passw},
           {'ip': '192.168.181.24',
            'device_type': 'cisco_nxos',
            'username': user,
            'password': passw}
           ]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        e = executor.map(save_config, devices)
        

if __name__ == '__main__':
    main()
