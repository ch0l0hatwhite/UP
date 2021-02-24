import os
import time


print("""
          ──█─▄▀█──█▀▄─█──
          ─▐▌──────────▐▌─
          ─█▌▀▄──▄▄──▄▀▐█─
          ▐██──▀▀──▀▀──██▌
          ████▄──▐▌──▄████
""")

print(' Bienvenidos a UDT Herramienta de automátizacion de descarga de herramientas')
time.sleep(3)


print('cargando...')
time.sleep(3)

print("Preparando herramientas a descargar ")
time.sleep(2)
os.system("clear")
time.sleep(2)

print("cargando...")
time.sleep(3)
	
os.system(" clear")
os.system("apt update")
os.system("pkg install mc ")
os.system("pkg install python2 -y")
os.system("pkg install ruby -y")
os.system("pkg install cmatrix -y")
os.system("pkg install nano -y")
os.system("pkg install php -y")
os.system("pkg install wget -y")
os.system("pkg install curl -y")
os.system("pkg install sqlmap -y")
os.system("pkg install irssi -y")
os.system("pkg install root-repo ")
os.system("pkg install x11-repo ")
os.system("pkg install unstable-repo")
os.system("pkg update ")
os.system("nmap -y")
os.system("pkg install openssh -y")
meta = input("la siguiente herramienta en instalarse es Framework Metasploit y Tiene un peso de 3gb Desea continuar? y / n  >> ")

if meta == "y":
        os.sytem("clear")
print("metasploit framework esta instalandose..")
time.sleep(3)

print("NO CIERRE LA CONSOLA Y NO APAGUE EL INTERNET")
time.sleep(3)

os.system("clear")
os.system("pkg install metasploit")

elif meta == "n":
   	os.system("pkg update")
        os.system("apt update")
        os.system("exit")
        
print("Herramientas Instaladas Con Exito :)")
print("vuelva pronto")

os.system("cmatrix")


