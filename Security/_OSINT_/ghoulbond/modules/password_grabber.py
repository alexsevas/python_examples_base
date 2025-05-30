# conda activate allpy310

"""Modules"""
import os
from prettytable import PrettyTable
from colorama import Fore
import platform

"""Main function"""
def passwords():

    """Check"""
    if platform.uname()[0] != 'Windows':
        print(Fore.RED + "This work's only for Windows")
        exit()
    
    else:

        """OS command"""
        ssid_raw = os.popen('netsh wlan show profile').read()
        ssid_raw_array = ssid_raw.split('\n')

        """Arrays to store information"""

        ssid_name = []
        ssid_authentication = []
        # ssid_cipher = []
        ssid_key = []

        for individual_name in ssid_raw_array:
            if('All User Profile     :') in individual_name:
                ssid_name.append(individual_name.replace('All User Profile     :', '').strip())

        for individual_name in ssid_name:
            sys_out = os.popen(f'netsh wlan show profile "{individual_name}" key=clear').read()
            sys_out_array = sys_out.split('\n')

            ssid_authentication_index = 0

            for individual in sys_out_array:
                if("Security key           : Absent") in individual:
                    ssid_key.append("N/A")

                elif("Authentication         :") in individual:
                    if(ssid_authentication_index < 1):
                        ssid_authentication.append(individual.replace('Authentication         :' , '').strip())
                    ssid_authentication_index += 1
                
                elif("Key Content            :") in individual:
                    ssid_key.append(individual.replace('Key Content            :','').strip())
            
        """SSID Table"""
        if(len(ssid_key) == 0):
            print(Fore.RED+f"No Saved Wifi Password's are found\n[-]Aborting!!\n")
                
        ssid_table = PrettyTable()
        ssid_table.add_column("SSID",ssid_name)
        ssid_table.add_column("Authentication",ssid_authentication)
        ssid_table.add_column("Key",ssid_key)

        print(Fore.LIGHTYELLOW_EX + f"\n{ssid_table}\n")
        print(Fore.RESET,end='')

if __name__ == '__main__':
    passwords()