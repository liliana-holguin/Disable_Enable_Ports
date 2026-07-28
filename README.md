Network Map — Port Enable/Disable GUI

A Tkinter desktop application that displays a floor-plan image with Enable (E) and Disable (D) buttons overlaid at each employee's desk location. Clicking a button uses Netmiko to SSH into the relevant Cisco switch and shut down or re-enable that person's network interface — a visual "kill switch" panel for office network ports.

What It Does
Opens a window (1024×768) titled "Testing Maps".
Loads and displays Map.jpg (a floor plan) as the background.
Overlays a D and E button pair at the pixel coordinates of each person's/room's location on the map.
Each button pair calls a per-person disable_<name>() / enable_<name>() function that:
Opens a Netmiko ConnectHandler session to the configured switch (cisco_switch or mail_switch).
Enters privileged (enable) mode.
Pushes interface x + shutdown (Disable) or interface x + no shutdown (Enable).
Prints "Disabled" / "Enabled" to the console for basic feedback.
Requirements
bash
pip install netmiko pillow
Python 3.x with tkinter (bundled with most standard Python installs).
Map.jpg must exist in the same directory as the script (or update the path).
Network reachability from the machine running the script to both switches, plus valid credentials.
Configuration

Two switch connection dictionaries at the top of the script need real values in place of the 'x' placeholders:

python
cisco_switch = {
    'device_type': 'x',   # e.g. 'cisco_ios'
    'host': 'x',          # switch management IP/hostname
    'username': 'x',
    'password': 'x',
    'secret': 'x',        # enable secret
}

mail_switch = {
    'device_type': 'x',
    'host': 'x',
    'username': 'x',
    'password': 'x',
    'secret': 'x',
}

Each per-person function also has a placeholder interface name:

python
commands = ['interface x', 'shutdown']

interface x must be replaced with the actual switchport (e.g. GigabitEthernet1/0/12) for every single function before this will work — as written, every disable/enable call targets the literal interface x, which doesn't exist on a real switch.

Structure
Two switch groups: most people are wired to cisco_switch; a handful (Anna Juarez, Sheryl Glanton, Amanda Lisby, Jessica Cortez) are wired to mail_switch.
One function pair per person/room, named after their initials (e.g. disable_dtarin / enable_dtarin for Delma Tarin).
One button pair per person/room, placed with .place(x=..., y=...) at the map coordinates matching their desk.
A few names are listed as comments only with no functions/buttons (Bobby Kimbro, Christian Fuksa — noted as "no ethernet").
