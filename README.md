# Basic File Encryption

In this example, a Python code encrypts a file using the simplest encryption method, XOR.
As known, applying XOR operation twice with the same number on a value results in the original value.
In this case, an image file is opened in binary mode, and each byte is individually subjected to XOR
operation with the specified number provided as an argument. Consequently, an image file is encrypted.
When the encrypted image file is subjected to XOR operation again with the same number, the original image file is recovered.

# Usage

>python create_image.py exampleImage.jpg encryptedImage.jpg 45


45 is the key value here.