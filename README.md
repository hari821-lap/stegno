Description:

This project implements a simple image steganography technique using OpenCV. It allows users to hide a secret message inside an image and later retrieve it using a passcode. 
The message is encoded by modifying the pixel values of the image.

Features:

Encrypt a secret message into an image
Decrypt the hidden message using a passcode
Simple command-line interface

Requirements:

Python 3.x
OpenCV (cv2)
OS module (built-in)

Installation:

Install Python if not already installed.
Install OpenCV:
               pip install opencv-python

Usage
Encryption:

Place your image in the working directory and rename it as mypic.jpg (or modify the script accordingly).
Run the script:
               python script.py
               
Choose (E)ncrypt when prompted.
Enter your secret message.
Provide a passcode for encryption.
The encrypted image will be saved as encryptedImage.jpg.

Decryption:
Run the script again:
                     python script.py
                     
Choose (D)ecrypt when prompted.
Enter the stored passcode.
Provide the length of the original message.
If the passcode is correct, the hidden message will be revealed.

Notes:

The encryption modifies the pixel values in a predictable pattern.
The image must be of a sufficient size to store the message.
Ensure that the correct passcode is used for decryption.

License:

This project is open-source and available for personal and educational use.
Ensure that the correct passcode is used for decryption.
