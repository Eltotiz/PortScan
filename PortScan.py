import nmap
import time
import os
from colorama import init, Fore

os.system("clear")
print(Fore.BLUE + """  ___              _    ___                
 | . \ ___  _ _  _| |_ / __> ___  ___ ._ _ 
 |  _// . \| '_>  | |  \__ \/ | '<_> || ' |
 |_|  \___/|_|    |_|  <___/\_|_.<___||_|_|
                                           

""")
print()
print(Fore.YELLOW + "            Creado por Eltotiz")
print(Fore.BLUE + "")
ip=input("[+] IP Objetivo ==> ")
print()
print()
print("Añadirle Nombre al archivo donde se guardara los puertos abiertos.")
print()
archivo=input("[+] Inserte nombre al archivo ==> ")
f = open(f"/$HOME/PortScan/ports/{archivo}.txt", "w")

print()
print("Archivo creado.")

time.sleep(2)
os.system('clear')

nm = nmap.PortScanner()
puertos_abiertos="-p "
results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
count=0
#print (results)

print("==============================")
print("      Escaneo de puertos")
print()
print("\n[+] Host : %s" % ip)
print()
print("[+] Estado : %s" % nm[ip].state())
print()
for proto in nm[ip].all_protocols():
	print("[+] Protocolo : %s" % proto)
	print()
	lport = nm[ip][proto].keys()
	sorted(lport)
	
	for port in lport:
		print (Fore.GREEN + "[+] puerto : %s\testado : %s" % (port, nm[ip][proto][port]["state"]))
		if count==0:
			puertos_abiertos=puertos_abiertos+str(port)
			count=1
		else:
			puertos_abiertos=puertos_abiertos+","+str(port)
			
			print("\n[+] Puertos abiertos: "+ puertos_abiertos +" "+str(ip), file=f)
			
f = open(f"{archivo}.txt", "w")
print("\nPuertos abiertos: "+ puertos_abiertos +" "+str(ip), file=f)
f.close()

print()
print()
print(Fore.BLUE + f"[+] Puertos abiertos guardados en {archivo}.txt en la carpeta ports")
print()
print("==============================")
