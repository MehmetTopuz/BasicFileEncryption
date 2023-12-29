import os
import sys


def xorData (data, key:int):
    return bytes(x ^ key for x in data)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        fileName = sys.argv[1]
        encryptedFileName = sys.argv[2]
        key = sys.argv[3]

        try:
            sizeOfFile = os.path.getsize(fileName)
            with open(fileName, 'rb') as file:
                bytesOfFile = file.read()

            with open(encryptedFileName, 'wb') as file2:
                file2.write(xorData(bytesOfFile, int(key)),)

            print("File encrypted.")
        
        except Exception as e:
            print(f"Error: {e}")

    else:
        print("Error: Argument size.")