from netmiko import ConnectHandler

cisco_switch = {
    'device_type': 'cisco_xe',
    'host': 'x',
    'username': 'x',
    'password': 'x',
    'secret': 'x',
}

with ConnectHandler(**cisco_switch) as net_connect:
    net_connect.enable()
    commands = ['interface GiX', 'no shutdown']
    net_connect.send_config_set(commands)
    print("Enabled")
