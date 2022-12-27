#   Yookiscan by GodAlecs
#   This script is NOT FOR SALE

#   Library
import socket, re, time, os
from colorama import Fore
from mcstatus import JavaServer

#   General Variables
folder = "yookiscan-results" # Nome della cartella
reset = Fore.RESET # For color CLEAN
yellow = Fore.YELLOW # For color YELLOW
red = Fore.RED # For color RED
green = Fore.GREEN # For color GREEN
white = Fore.WHITE # For color WHITE
banner = f"""
{yellow}
╔╗  ╔╗╔═══╗╔═══╗╔╗╔═╗╔══╗╔═══╗╔═══╗╔═══╗╔═╗ ╔╗
║╚╗╔╝║║╔═╗║║╔═╗║║║║╔╝╚╣╠╝║╔═╗║║╔═╗║║╔═╗║║║╚╗║║
╚╗╚╝╔╝║║ ║║║║ ║║║╚╝╝  ║║ ║╚══╗║║ ╚╝║║ ║║║╔╗╚╝║
 ╚╗╔╝ ║║ ║║║║ ║║║╔╗║  ║║ ╚══╗║║║ ╔╗║╚═╝║║║╚╗║║
  ║║  ║╚═╝║║╚═╝║║║║╚╗╔╣╠╗║╚═╝║║╚═╝║║╔═╗║║║ ║║║
  ╚╝  ╚═══╝╚═══╝╚╝╚═╝╚══╝╚═══╝╚═══╝╚╝ ╚╝╚╝ ╚═╝

    {red}Telegram » {white}sickalex
    {red}Github » {white}github.com/GodAlecs                                       
""" # Banner


#   Function check_folder, that creates the folder if it doesn't exist
def check_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

#   Function check_file, that creates the file if it doesn't exist
def check_file(name):
    try: # Try opening the file
        checkFile = open(f"{folder}/{name}.txt", "a") # Open file
        checkFile.truncate(0) # Clear all data from the file
        checkFile.close() # Close File
    except FileNotFoundError: # If the file doesn't exist, create it
        createFile = open(f"{folder}/{name}.txt", "w") # Open file
        createFile.close() # Close File

#   Function update_file, that update a file with new string
def update_file(name, content):
    addtofile = open(f"{folder}/{name}.txt", "a") # Open file
    addtofile.write(f"{content}\n") # Add new string in the file
    addtofile.close() # Close file


#   Fuction scan, this fuction is for
#   scan server with given parameters
#   ADDRESS -> IP
#   PORT_START = port X
#   PORT_END = port Y
def scan(address, port_start, port_end):
    counter = 0 # For count server founds
    check_folder(folder) # Call the fuction check_folder
    check_file(address) # Call the fuction check_file
    start_time = time.perf_counter() # Start the TIMER
    for port in range(port_start, port_end):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
        try: # Try to connect
            s.connect((address, port))
            server = JavaServer.lookup(f"{address}:{port}")
            players_on = server.status().players.online
            players_max = server.status().players.max
            version = server.status().version.name
            motd = re.sub(r"§\w", "", server.status().description)
            print(f"""
{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}
{green} >> {reset}{address}:{port}
{green} >> {reset}{players_on}/{players_max}
{green} >> {reset}{version}
{green} >> {reset}{motd}
{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}""")
            counter += 1 # Counter add 1
            update_file(address, f"({address}:{port}) - ({players_on}/{players_max}) - ({version}) - ({motd})")
        except Exception:
            pass
        finally:
            s.close() # Close a socket
    end_time = time.perf_counter() # End the TIMER
    elapsed_time = end_time - start_time # Calculate the time taken
    print(f"\n\n{green}[*]{reset} Scan terminated!\n{green}[*]{reset} Server founds: {counter}\n{green}[*]{reset} Scan time: {elapsed_time:.2f}s\n\n")


#   Fuction main
def main():
    print(banner) # Print banner
    try:
        address = input(f"{reset}[*] {green}inserisci l'indirizzo IP > {reset}") # Requires the value "address"
        port_start = int(input(f"{reset}[*] {green}inserisci la porta X > {reset}")) # Requires the value "port X"
        port_end = int(input(f"{reset}[*] {green}inserisci la porta Y > {reset}")) # Requires the value "port Y"
        scan(address, port_start, port_end) # Call the fuction SCAN with given parameters
    except KeyboardInterrupt:
        print(f"\n\n{green}Bye bye!{reset}")

if __name__ == "__main__":
    main()
