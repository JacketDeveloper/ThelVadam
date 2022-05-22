from colorama import Fore
import os, time, base64, sys
 
def printlento(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)

os.system('clear')


print("_____________________")
print("[1] Encode base64    |")
print("[2] Descode base64   |")
print("_____________________|")
Encode = input("Elije pibe >> ")

if Encode == "1":
    encript = input(b'Escribe lo que vas a encriptar >> ')
    pito = base64.b64encode(bytes(encript, 'utf-8'))
    print(pito)
