import os
import sys
from colorama import Fore


def bash(command: str):
    """
     execute bash command

    """
    return os.system(command)

def handle_user_result():
    """
    return the user input for manage function
    """
    return input('{}[1] Perform Evil Twin Attack\n'
                 '[2] Perform Defence on Evil Twin Attack \n'
                 'Please select one of the options mentioned above, or write quit to quit the manager\n'.format(
                    Fore.BLUE))
                    
def exit_and_cleanup(exit_code, message):
    """
    This function execute clean up
    also perform exit with exit code.
    exit code 0 = the program has complete its purpose.
    """
    print('{}{}'.format(Fore.BLUE, 'Perform cleanup'))
    os.system('sudo sh cleanup.sh')
    sys.exit('{} Perform exit() with exit code {} , {}'.format(Fore.WHITE, exit_code, message))
    
    
def attack():
    """
    This function run the python file of the attack
    """
    os.system('sudo python3 attack/wifi_attack.py')
    

def defence():
    """
  	This function run the python file of the defence
    """
    os.system('sudo python3 defence/defence.py')



def print_header(message: str):
    """
    	the function is printing the header of the evil twin 
    """
    print(Fore.WHITE)
    bash('figlet {}'.format(message))



def print_command(message: str):
    """
    print command messages to console
    """
    print('{}{}'.format(Fore.BLUE, message))


def print_errors(message: str):
    """
    print error messages to console (RED)

    """
    print('{}{}'.format(Fore.RED, message))

def manage():
    """
    This is the main program function , this function is responsible for the program flow.
    """
    print_header('Evil Twin Manager by Moran and Amit')
    print_command("Welcome To Evil Twin Manager")
    if os.geteuid():  
        sys.exit('{}Perform exit() , Please run as root user , use sudo command '.format(Fore.RED))

    while True:
        user_input = handle_user_result()
        if user_input == '1':
            attack()
            break
        elif user_input == '2':
            defence()
            break

        else:
            print_errors('Not a valid option please , Please try again.')


if __name__ == '__main__':
    manage()