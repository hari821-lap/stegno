import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

def create_mappings():
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}
    return d, c

def upload_image():
    global img_path, img_display
    img_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.png;*.bmp")])
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((150, 150))
        img_display = ImageTk.PhotoImage(img)
        img_label.config(image=img_display)
        img_label.pack()

def encode_message():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please upload an image first!")
        return
    
    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter a passcode:", show='*')
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    img = cv2.imread(img_path)
    d, _ = create_mappings()
    
    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if index < len(msg):
                img[i, j, index % 3] = d[msg[index]]
                index += 1
            else:
                break
        if index >= len(msg):
            break
    
    encrypted_path = "encryptedImage.png"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")
    messagebox.showinfo("Success", "Message encoded successfully! Image saved as encryptedImage.png")
    
    with open("passcode.txt", "w") as file:
        file.write(password)

def decode_message():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please upload an encrypted image first!")
        return
    
    pas = simpledialog.askstring("Input", "Enter passcode for Decryption:", show='*')
    
    try:
        with open("passcode.txt", "r") as file:
            stored_password = file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "No stored passcode found!")
        return
    
    if pas != stored_password:
        messagebox.showerror("Error", "YOU ARE NOT authorized")
        return
    
    img = cv2.imread(img_path)
    _, c = create_mappings()
    
    message = ""
    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            char_value = img[i, j, index % 3]
            if char_value in c:
                message += c[char_value]
                index += 1
            else:
                break
        if char_value not in c:
            break
    
    msg_window = tk.Toplevel(app)
    msg_window.title("Decrypted Message")
    msg_window.geometry("500x300")
    msg_window.configure(bg="#f0f0f0")
    
    label = tk.Label(msg_window, text="Decrypted Message:", font=("Arial", 12, "bold"), bg="#f0f0f0")
    label.pack(pady=10)
    
    text_box = tk.Text(msg_window, wrap="word", height=10, width=60, font=("Arial", 10))
    text_box.pack(padx=10, pady=10)
    text_box.insert("1.0", message)
    text_box.config(state="disabled", bg="white")

app = tk.Tk()
app.title("Image Steganography")
app.geometry("350x350")
app.configure(bg="#e6f7ff")

frame = tk.Frame(app, bg="#e6f7ff")
frame.pack(pady=20)

tk.Label(frame, text="Image Steganography", font=("Arial", 14, "bold"), bg="#e6f7ff").pack(pady=5)

style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)

upload_button = ttk.Button(frame, text="Upload Image", command=upload_image)
upload_button.pack(pady=5, fill=tk.X, padx=20)

img_label = tk.Label(frame, bg="#e6f7ff")
img_label.pack()

encode_button = ttk.Button(frame, text="Encode Message", command=encode_message)
encode_button.pack(pady=5, fill=tk.X, padx=20)

decode_button = ttk.Button(frame, text="Decode Message", command=decode_message)
decode_button.pack(pady=5, fill=tk.X, padx=20)

exit_button = ttk.Button(frame, text="Exit", command=app.destroy)
exit_button.pack(pady=5, fill=tk.X, padx=20)

app.mainloop()
