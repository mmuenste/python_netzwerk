import asyncio
import netdev

async def task(param):
    async with netdev.create(**param) as ios:
        # Testing sending simple command
        out = await ios.send_command("show ver")
        print(out)
        print("*" * 30, "\n")
        


async def run():
    dev1 = { 'username' : 'admin',
             'password' : 'cisco',
             'device_type': 'cisco_nxos',
             'host': '192.168.181.21',
    }
    dev2 = { 'username' : 'admin',
             'password' : 'cisco',
             'device_type': 'cisco_nxos',
             'host': '192.168.181.22',
    }
    devices = [dev1, dev2]
    tasks = [task(dev) for dev in devices]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())