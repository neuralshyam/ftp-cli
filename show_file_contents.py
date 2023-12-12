import os
import platform

from transfer import download_file


def show_file_contents(ftp, remote_file):
    # Extract the filename from the remote path
    _, filename = os.path.split(remote_file)

    # Download the file to a temporary local file with the original filename
    local_temp_file = filename
    download_file(ftp, remote_file, local_temp_file)

    # Open the local temporary file with the default program
    if platform.system() == 'Windows':
        os.startfile(local_temp_file)
    else:
        import subprocess
        subprocess.Popen(['xdg-open', local_temp_file])
    # Download the file to a temporary local file
    local_temp_file = 'temp_file_to_show'
    download_file(ftp, remote_file, local_temp_file)

    # Open the local temporary file with the default program
    if platform.system() == 'Windows':
        os.startfile(local_temp_file)
    else:
        import subprocess
        subprocess.Popen(['xdg-open', local_temp_file])

    # Optionally, you can clean up the local temporary file afterward
    os.remove(local_temp_file)