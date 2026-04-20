import tkinter as tk
from PIL import Image, ImageTk

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

def disable():
    print("Disabled")

button = tk.Button(root, text="D", command=disable)
button.place(x=750, y=279)

def enabled():
    print("Enabled")

button = tk.Button(root, text="D", command=disable)
button.place(x=750, y=279)

btn = tk.Button(root, text="E", command=enabled)
btn.place(x=770, y=279)

root.mainloop()