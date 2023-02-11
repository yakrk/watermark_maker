import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from PIL import Image, ImageFont, ImageDraw, ImageTk
import os

### Get original image file path
def upload_file():
    global origin_filepath
    global img1
    global origin_image_lbl
    # upload image 
    f_types = [("", "")]
    origin_filepath = filedialog.askopenfilename(filetypes=f_types)
    origin_filepath_entry.config(text = f"filename: {origin_filepath}")
    
    # show image
    img1 = Image.open(origin_filepath)
    img1.thumbnail((200, 200), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(img1)  
    origin_image_lbl.configure(image=img1)
    return 

# add text to image
def create_watermark_transparent_image():
    global origin_filepath
    # get file name and path for new image
    filename = os.path.basename(origin_filepath)
    filepath = os.path.dirname(origin_filepath)
    path, ext = os.path.splitext(filename)
    watermark_text2 = watermark_text.get()
    new_file_text2 = "\\" + new_file_text.get()
    new_image_path_fin = filepath + new_file_text2 + ext
    # create and save watermarked image
    img = Image.open(origin_filepath)
    tk_img = ImageTk.PhotoImage(img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(set_font, 24)
    for j in range(1, tk_img.height(), 50):
        for i in range(1, tk_img.width(), 300):
            draw.text((i, j), watermark_text2, fill=(255, 255, 255, 18), font=font)
    img.save(new_image_path_fin)
    
    # add completed message
    done_label.config(text = f"new file created. filename: {new_image_path_fin}")
    return 


# Create a view with Tkinter
BACKGROUND_COLOR = "white"
## Create window
window = tk.Tk()
window.title("Watermark Maker")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
origin_filepath = None
set_font = 'C:\Windows\Fonts\Arial.ttf'

## Plot buttons
### title
watermark_title = tk.Label(text='Watermark Image Converter', background=BACKGROUND_COLOR, justify="left", anchor="w", pady=20)
watermark_title.grid(sticky = "w", row=0, column=0, columnspan=2)

# Upload button 
b1 = tk.Button(window, text='Upload Original File', width=50, command = upload_file)
b1.grid(sticky = "w", row=1, column=0, columnspan=2)

# Show uploaded image
origin_image_lbl = tk.Label(text="Image Preview: ", bg="white")
origin_image_lbl.grid(sticky = "w", row=2, column=0, columnspan=2)

# Show uploaded image's filename
origin_filepath_entry = tk.Label(text=f"filename: {origin_filepath}", background=BACKGROUND_COLOR)
origin_filepath_entry.grid(sticky = "w", row=3, column=0, columnspan=2)

### Show watermark text entry
watermark_label = tk.Label(text=f"Enter watermark text: ", background=BACKGROUND_COLOR)
watermark_label.grid(sticky = "w", row=4, column=0)
watermark_text = tk.Entry(width=40)
watermark_text.insert(tk.END,"Enter Watermark Text Here")
watermark_text.grid(sticky = "w", row=4,column=1)

### New Filename text entry
new_file_label = tk.Label(text=f"Enter new file name: ", background=BACKGROUND_COLOR)
new_file_label.grid(sticky = "w", row=5, column=0)
new_file_text = tk.Entry(width=40)
new_file_text.insert(tk.END,"new_image")
new_file_text.grid(sticky = "w", row=5,column=1)

# Create watermark image button 
get_image = tk.Button(text="Create Image", highlightthickness=0, width=50, command=create_watermark_transparent_image)
get_image.grid(sticky = "w", row=6, column=0, columnspan=2)

### Show when new file is created
done_label = tk.Label(text="", background=BACKGROUND_COLOR)
done_label.grid(sticky = "w", row=7, column=0, columnspan=2)

window.mainloop()