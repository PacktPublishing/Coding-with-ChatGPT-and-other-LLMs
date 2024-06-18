# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:11:03 2024

@author: Written by Vincent Hall 
of Build Intellect Ltd. and ABT NEWS Ltd. 12 Feb 2024.
"""

from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

# Initialize Tkinter window
root = Tk()

# Create a label to display the image
label = Label(root)
label.pack()

# Define a function to load an image
def load_image():
    filename = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg;*.png")])
    if filename:
        try:
            # Open the image using PIL
            img = Image.open(filename)

            # Convert the image to Tkinter format
            tk_img = ImageTk.PhotoImage(img, master=root)

            # Update the label with the new image
            label.config(image=tk_img)
            label.image = tk_img  # Keep a reference to the image to prevent garbage collection
        except Exception as e:
            print("Error loading image:", e)

# Create a button to trigger the image loading
button = Button(root, text="Load Image", command=load_image)
button.pack()

# Run the window's main loop
root.mainloop()
