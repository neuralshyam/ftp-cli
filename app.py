from ftplib import FTP
import platform
import shlex
import configparser
from transfer import delete_file, upload_file 
from transfer import download_file
from show_file_contents import show_file_contents
ftp = FTP()
ftp.timeout = 3000  # Set the timeout to 5 minutes (in seconds)

def get_ftp_credentials():
    config = configparser.ConfigParser()
    config.read('config.ini')
    ftp_host = config.get('FTP', 'host')
    ftp_user = config.get('FTP', 'username')
    ftp_pass = config.get('FTP', 'password')
    return ftp_host, ftp_user, ftp_pass
def list_files(ftp):
    data = []
    ftp.retrlines('LIST', data.append)
    for line in data:
        print(line)

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    # Get FTP credentials from the user
    ftp_host, ftp_user, ftp_pass = get_ftp_credentials()

    # Connect to the FTP server
    ftp = FTP()
    ftp.connect(ftp_host)

    # Disable Extended Passive Mode
    ftp.set_pasv(False)

    # Log in to the FTP server
    ftp.login(ftp_user, ftp_pass)

    while True:
        # List files on the FTP server
        list_files(ftp)

        # Prompt the user for the next action
        action = input("Enter a command (e.g., 'ls', 'cd <directory>', 'mkdir <directory>', 'upload <local_file> <remote_file>', 'download <remote_file> <local_file>', 'clear', 'quit'): ")

        # Process the user's command
        if action.lower() == 'quit':
            break
        elif action.lower().startswith('cd'):
            _, directory = action.split(' ', 1)
            ftp.cwd(directory)
        elif action.lower().startswith('mkdir'):
            _, new_directory = action.split(' ', 1)
            ftp.mkd(new_directory)
        elif action.lower().startswith('upload'):
            _, *file_args = shlex.split(action)
            local_file, remote_file = file_args[0], file_args[1]
            upload_file(ftp, local_file, remote_file)
        elif action.lower().startswith('download'):
            _, *file_args = shlex.split(action)
            remote_file, local_file = file_args[0], file_args[1]
            download_file(ftp, remote_file, local_file)
        elif action.lower().startswith('delete'):
            _, remote_file = shlex.split(action, 1)
            delete_file(ftp, remote_file)
        elif action.lower().startswith('show'):
            _, remote_file = shlex.split(action, 1)
            show_file_contents(ftp, remote_file)
        elif action.lower() == 'ls':
            continue  # The next iteration of the loop will list files
        elif action.lower() == 'clear':
            clear_screen()
        else:
            print("Invalid command. Try again.")
            # Close the FTP connection               




if __name__ == "__main__":
    main()
