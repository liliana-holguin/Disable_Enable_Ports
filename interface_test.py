import tkinter as tk
from netmiko import ConnectHandler

cisco_switch = {
    'device_type': 'cisco_xe',
    'host': 'x',
    'username': 'x',
    'password': 'x',
    'secret': 'x',
}

root = tk.Tk()
root.title("Testing Buttons")
root.geometry('300x200')
label = tk.Label(root, text="Enable and Disable Network")
label.pack()



def disable():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface Gi5/0/36', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface Gi5/0/36', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

btn_disable = tk.Button(root, text="Disable", command=disable)
btn_disable.pack(pady=20)

btn_enable = tk.Button(root, text="Enable", command=enable)
btn_enable.pack(pady=20)

root.mainloop()
