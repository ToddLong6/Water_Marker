from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image, ImageGrab
import tkinter

root = Tk()
root.geometry("800x600")
root.title("Image Water Marker")

# Upload a Picture
def get_image():
    global display_image
    filename = filedialog.askopenfilename()
    new_image = Image.open(filename)
    resized_image = new_image.resize((300,400))
    display_image = ImageTk.PhotoImage(resized_image)
    image_container = upload_canvas.create_image(0,0, anchor="nw",image=display_image)

# Download a Picture
def save():
    box = (download_canvas.winfo_rootx(),download_canvas.winfo_rooty(),download_canvas.winfo_rootx()+download_canvas.winfo_width(),download_canvas.winfo_rooty() + download_canvas.winfo_height())
    image = ImageGrab.grab(bbox=box, include_layered_windows=False)
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".png")
    if not filename:
        return
    image.save(filename)
    

# Add Water mark to Picture
def update_image():
    global update_label
    mark = water_mark_entry.get()
    update_label = ttk.Label(download_canvas, text=mark, image=display_image, compound='center')
    update_label.grid(column=5, row=5, columnspan=2, rowspan=4)
    
    


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# I need two Content Canvas, 3 Button, 1 text box, and 4 Label,
# Labels
ttk.Label(mainframe, text="The Water Marker").grid(column=0, row=1, columnspan=3, sticky=W)
ttk.Label(mainframe, text="Water Mark Text").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Your Uploaded Photo").grid(column=2, row=4, sticky=E)
ttk.Label(mainframe, text="Your Marked Photo").grid(column=5, row=4, sticky=E)

# Text Box
water_mark = StringVar()
water_mark_entry = ttk.Entry(mainframe, width=25, textvariable=water_mark)
water_mark_entry.grid(column=2, row=2, sticky=(W, E))

# Canvas
upload_canvas = Canvas(mainframe, width=300, height= 400)
upload_canvas.grid(column=2, row=5, columnspan=2, rowspan=4)

download_canvas = Canvas(mainframe, width=300, height= 400)
download_canvas.grid(column=5, row=5, columnspan=2, rowspan=4)

# Button
ttk.Button(mainframe, text="Upload Image", command=get_image).grid(column=2, row=9)
ttk.Button(mainframe, text="Add Mark", command=update_image).grid(column=4, row=9)
ttk.Button(mainframe, text="Download Image", command=save).grid(column=6, row=9)

root.mainloop()