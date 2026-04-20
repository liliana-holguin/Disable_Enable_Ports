#################### Imports ####################
import tkinter as tk
from netmiko import ConnectHandler
from PIL import Image, ImageTk

#################### Switch Info ####################
cisco_switch = {
    'device_type': 'cisco_xe',
    'host': 'x',
    'username': 'x',
    'password': 'x',
    'secret': 'x',
}

mail_switch = {
    'device_type': 'cisco_xe',
    'host': 'x',
    'username': 'x',
    'password': 'x',
    'secret': 'x',
}

#################### Set Up GUI ####################
root = tk.Tk()
root.title("Testing Maps")
root.geometry('1024x768')

label = tk.Label(root, text="Enable and Disable Network Map")
label.pack()

image = Image.open("Map.jpg")
image = image.resize((1024, 768))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image)
image_label.pack()

#################### Disable and Enable Commands ####################

# Delma Tarin
def disable_dtarin():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_dtarin():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Liliana Holguin
def disable_lholguin():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_lholguin():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Jorge Ortega
def disable_jortega():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_jortega():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Kyle Coleman
def disable_kcoleman():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_kcoleman():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Training Room 1
def disable_train1():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_train1():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Rosa Arroyo
def disable_rarroyo():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_rarroyo():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Mari Valencia
def disable_mvalencia():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_mvalencia():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Chris Bessenecker
def disable_cbessen():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_cbessen():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# April Aranda
def disable_aaranda():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_aaranda():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Jasmine Watson
def disable_jwatson():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_jwatson():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Denise McDaniel
def disable_dmcdaniel():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_dmcdaniel():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Nelly Dominguez
def disable_ndominguez():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_ndominguez():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Jane Salcido
def disable_jsalcido():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_jsalcido():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Cherol Autry
def disable_cautry():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_cautry():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Delaine Velasco
def disable_dvelasco():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_dvelasco():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Anna Juarez
def disable_ajuarez():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_ajuarez():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Diana Hernandez
def disable_dhernandez():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_dhernandez():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Sheryl Glanton
def disable_sglanton():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_sglanton():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Amanda Lisby
def disable_alisby():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_alisby():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

#### Front Room ####

# Nellie Arenivas
def disable_narenivas():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_narenivas():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Yesenia Rebolledo
def disable_yrebolledo():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_yrebolledo():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")
        
# Cynthia Brown
def disable_cbrown():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_cbrown():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Checkuser
def disable_checkuser():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_checkuser():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

#####

# Jessica Cortez
def disable_jcortez():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_jcortez():
    with ConnectHandler(**mail_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Robert Capps
def disable_rcapps():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_rcapps():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Training Room 2
def disable_train2():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_train2():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# John Cartwright
def disable_cartwright():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_cartwright():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")
# Bobby Kimbro

# Christian Fuksa - no ethernet

# Heli Mendoza
def disable_hmendoza():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_hmendoza():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Rick Porras
def disable_rporras():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_rporras():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Ray Rivera
def disable_erivera():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_erivera():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Nathaneal Camp
def disable_ncamp():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_ncamp():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Alma Griffin
def disable_agriffin():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_agriffin():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")

# Bobby Ferris
def disable_bferris():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'shutdown']
        net_connect.send_config_set(commands)
        print("Disabled")

def enable_bferris():
    with ConnectHandler(**cisco_switch) as net_connect:
        net_connect.enable()
        commands = ['interface x', 'no shutdown']
        net_connect.send_config_set(commands)
        print("Enabled")        

#################### Disable and Enable Buttons ####################

# Delma Tarin
d_dtarin = tk.Button(root, text="D", command=disable_dtarin)
d_dtarin.place(x=700, y=312)

e_dtarin = tk.Button(root, text="E", command=enable_dtarin)
e_dtarin.place(x=720, y=312)

# Liliana Holguin
d_lholguin = tk.Button(root, text="D", command=disable_lholguin)
d_lholguin.place(x=750, y=312)

e_lholguin = tk.Button(root, text="E", command=enable_lholguin)
e_lholguin.place(x=770, y=312)

# Jorge Ortega
d_jortega = tk.Button(root, text="D", command=disable_jortega)
d_jortega.place(x=720, y=399)

e_jortega = tk.Button(root, text="E", command=enable_jortega)
e_jortega.place(x=740, y=399)

# Kyle Coleman
d_kcoleman = tk.Button(root, text="D", command=disable_kcoleman)
d_kcoleman.place(x=970, y=312)

e_kcoleman = tk.Button(root, text="E", command=enable_kcoleman)
e_kcoleman.place(x=990, y=312)

# Training Room 1
d_train1 = tk.Button(root, text="D", command=disable_train1)
d_train1.place(x=970, y=399)

e_train1 = tk.Button(root, text="E", command=enable_train1)
e_train1.place(x=990, y=399)

# Rosa Arroyo
d_rarroyo = tk.Button(root, text="D", command=disable_rarroyo)
d_rarroyo.place(x=895, y=399)

e_rarroyo = tk.Button(root, text="E", command=enable_rarroyo)
e_rarroyo.place(x=915, y=399)

# Mari Valencia
d_mvalencia = tk.Button(root, text="D", command=disable_mvalencia)
d_mvalencia.place(x=770, y=424)

e_mvalencia = tk.Button(root, text="E", command=enable_mvalencia)
e_mvalencia.place(x=790, y=424)

# Chris Bessenecker
d_cbessen = tk.Button(root, text="D", command=disable_cbessen)
d_cbessen.place(x=970, y=462)

e_cbessen = tk.Button(root, text="E", command=enable_cbessen)
e_cbessen.place(x=990, y=462)

# April Aranda
d_aaranda = tk.Button(root, text="D", command=disable_aaranda)
d_aaranda.place(x=872, y=462)

e_aaranda = tk.Button(root, text="E", command=enable_aaranda)
e_aaranda.place(x=892, y=462)

# Jasmine Watson
d_jwatson = tk.Button(root, text="D", command=disable_jwatson)
d_jwatson.place(x=814, y=552)

e_jwatson = tk.Button(root, text="E", command=enable_jwatson)
e_jwatson.place(x=834, y=552)

# Denise McDaniel
d_dmcdaniel = tk.Button(root, text="D", command=disable_dmcdaniel)
d_dmcdaniel.place(x=814, y=582)

e_dmcdaniel = tk.Button(root, text="E", command=enable_dmcdaniel)
e_dmcdaniel.place(x=834, y=582)

# Nelly Dominguez
d_ndominguez = tk.Button(root, text="D", command=disable_ndominguez)
d_ndominguez.place(x=664, y=582)

e_ndominguez = tk.Button(root, text="E", command=enable_ndominguez)
e_ndominguez.place(x=684, y=582)

# Jane Salcido
d_jsalcido = tk.Button(root, text="D", command=disable_jsalcido)
d_jsalcido.place(x=644, y=495)

e_jsalcido = tk.Button(root, text="E", command=enable_ndominguez)
e_jsalcido.place(x=664, y=495)

# Cherol Autry
d_cautry = tk.Button(root, text="D", command=disable_cautry)
d_cautry.place(x=614, y=582)

e_cautry = tk.Button(root, text="E", command=enable_cautry)
e_cautry.place(x=634, y=582)

# Delaine Velasco
d_dvelasco = tk.Button(root, text="D", command=disable_dvelasco)
d_dvelasco.place(x=514, y=582)

e_dvelasco = tk.Button(root, text="E", command=enable_dvelasco)
e_dvelasco.place(x=534, y=582)

# Anna Juarez
d_ajuarez = tk.Button(root, text="D", command=disable_ajuarez)
d_ajuarez.place(x=564, y=495)

e_ajuarez = tk.Button(root, text="E", command=enable_ajuarez)
e_ajuarez.place(x=584, y=495)

# Diana Hernandez
d_dhernandez = tk.Button(root, text="D", command=disable_dhernandez)
d_dhernandez.place(x=489, y=495)

e_dhernandez = tk.Button(root, text="E", command=enable_dhernandez)
e_dhernandez.place(x=509, y=495)

# Sheryl Glanton
d_sglanton = tk.Button(root, text="D", command=disable_sglanton)
d_sglanton.place(x=409, y=495)

e_sglanton = tk.Button(root, text="E", command=enable_sglanton)
e_sglanton.place(x=429, y=495)

# Amanda Lisby
d_alisby = tk.Button(root, text="D", command=disable_alisby)
d_alisby.place(x=333, y=495)

e_alisby = tk.Button(root, text="E", command=enable_alisby)
e_alisby.place(x=353, y=495)

#### Front Room ####

# Nellie Arenivas
d_narenivas = tk.Button(root, text="D", command=disable_narenivas)
d_narenivas.place(x=313, y=568)

e_narenivas = tk.Button(root, text="E", command=enable_narenivas)
e_narenivas.place(x=333, y=568)

# Yesenia Rebolledo
d_yrebolledo = tk.Button(root, text="D", command=disable_yrebolledo)
d_yrebolledo.place(x=313, y=618)

e_yrebolledo = tk.Button(root, text="E", command=enable_yrebolledo)
e_yrebolledo.place(x=333, y=618)

# Cynthia Brown
d_cbrown = tk.Button(root, text="D", command=disable_cbrown)
d_cbrown.place(x=413, y=618)

e_cbrown = tk.Button(root, text="E", command=enable_cbrown)
e_cbrown.place(x=433, y=618)

# Checkuser
d_checkuser = tk.Button(root, text="D", command=disable_checkuser)
d_checkuser.place(x=413, y=568)

e_checkuser = tk.Button(root, text="E", command=enable_checkuser)
e_checkuser.place(x=433, y=568)

#####

# Jessica Cortez
d_jcortez = tk.Button(root, text="D", command=disable_jcortez)
d_jcortez.place(x=166, y=525)

e_jcortez = tk.Button(root, text="E", command=enable_jcortez)
e_jcortez.place(x=186, y=525)

# Robert Capps
d_rcapps = tk.Button(root, text="D", command=disable_rcapps)
d_rcapps.place(x=166, y=495)

e_rcapps = tk.Button(root, text="E", command=enable_rcapps)
e_rcapps.place(x=186, y=495)

# Training Room 2
d_train2 = tk.Button(root, text="D", command=disable_train2)
d_train2.place(x=15, y=432)

e_train2 = tk.Button(root, text="E", command=enable_train2)
e_train2.place(x=35, y=432)

# John Cartwright
d_cartwright = tk.Button(root, text="D", command=disable_cartwright)
d_cartwright.place(x=15, y=372)

e_cartwright = tk.Button(root, text="E", command=enable_cartwright)
e_cartwright.place(x=35, y=372)
# Bobby Kimbro

# Christian Fuksa


# Heli Mendoza
d_hmendoza = tk.Button(root, text="D", command=disable_hmendoza)
d_hmendoza.place(x=475, y=394)

e_hmendoza = tk.Button(root, text="E", command=enable_hmendoza)
e_hmendoza.place(x=495, y=394)

# Rick Porras
d_rporras = tk.Button(root, text="D", command=disable_rporras)
d_rporras.place(x=475, y=311)

e_rporras = tk.Button(root, text="E", command=enable_rporras)
e_rporras.place(x=495, y=311)

# Ray Rivera
d_erivera = tk.Button(root, text="D", command=disable_erivera)
d_erivera.place(x=522, y=394)

e_erivera = tk.Button(root, text="E", command=enable_erivera)
e_erivera.place(x=542, y=394)

# Nathaneal Camp
d_ncamp = tk.Button(root, text="D", command=disable_ncamp)
d_ncamp.place(x=570, y=394)

e_ncamp = tk.Button(root, text="E", command=enable_ncamp)
e_ncamp.place(x=590, y=394)

# Alma Griffin
d_agriffin = tk.Button(root, text="D", command=disable_agriffin)
d_agriffin.place(x=814, y=242)

e_agriffin = tk.Button(root, text="E", command=enable_agriffin)
e_agriffin.place(x=834, y=242)

# Bobby Ferris
d_bferris = tk.Button(root, text="D", command=disable_bferris)
d_bferris.place(x=814, y=210)

e_bferris = tk.Button(root, text="E", command=enable_bferris)
e_bferris.place(x=834, y=210)








#################### Run It ####################
root.mainloop()
