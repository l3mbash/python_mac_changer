import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface", help = "Nombre de la Interface que desea cambiar")
    parser.add_option("-m","--mac", dest = "new_mac", help = "Ingrese la nueva direccion MAC")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor ingrese una interfaz, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-] Por favor ingresa una direccion MAC, usa --help para mas informacion")
    return options

def changemac(interface, new_mac):
    print("[+] Cambiando la direcion mac para "+ interface + " a " + new_mac)

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    
    ifconfig_results = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] No se pudo leer la direccion MAC")




options = get_args()

current_mac = get_current_mac(options.interface)
print("La direccion mac actual es = " + str(current_mac))

changemac(options.interface, options.new_mac)

current_mac = str(get_current_mac(options.interface))

if current_mac == options.new_mac:
    print("[+] La direcion mac se a ha cambiado a " + current_mac)
else:
    print("[-] La direccion mac no se ha cambiado")

