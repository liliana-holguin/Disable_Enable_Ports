etwork map · MD
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
Known Issues
Hardcoded interface name: every function uses the literal string 'interface x' — this is a placeholder that must be replaced with each person's actual switchport before the tool will function.
Credentials in plaintext: switch credentials are stored directly in the script. Consider pulling them from environment variables, a .env file (with python-dotenv), or a secrets manager instead of committing them to source.
Copy-paste bug: the "E" button for Jane Salcido is wired to the wrong handler —
python
  e_jsalcido = tk.Button(root, text="E", command=enable_ndominguez)

This calls enable_ndominguez instead of enable_jsalcido, meaning clicking Jane Salcido's Enable button actually re-enables Nelly Dominguez's port. Should be:

python
  e_jsalcido = tk.Button(root, text="E", command=enable_jsalcido)
No error handling: if a switch is unreachable or credentials are wrong, ConnectHandler will raise an exception that isn't caught, likely crashing that button's callback silently in the GUI.
No confirmation dialog: clicking "D" immediately shuts down a port with no "are you sure?" prompt — easy to fat-finger and disconnect the wrong person.
Duplicated logic: every disable/enable function is nearly identical (same commands, different switch object). This could be collapsed into two generic functions parameterized by switch + interface name, which would also make fixing the two issues above much easier and less error-prone.
Suggested Improvements
Replace the ~50 near-duplicate functions with a single reusable pair:
python
  def disable_port(switch, interface):
      with ConnectHandler(**switch) as net_connect:
          net_connect.enable()
          net_connect.send_config_set([f'interface {interface}', 'shutdown'])

  def enable_port(switch, interface):
      with ConnectHandler(**switch) as net_connect:
          net_connect.enable()
          net_connect.send_config_set([f'interface {interface}', 'no shutdown'])

Then drive both the button command= and interface data from a single list/dict of (name, switch, interface, x, y) tuples, generating buttons in a loop.
