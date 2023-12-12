from ftplib import error_perm
import os
import progressbar

import os
from tqdm import tqdm

def upload_file(ftp, local_file, remote_file):
    file_size = os.path.getsize(local_file)

    def callback(data):
        pbar.update(len(data))

    with open(local_file, 'rb') as file:
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=f'Uploading {remote_file}') as pbar:
            ftp.storbinary(f'STOR {remote_file}', file, callback=callback, blocksize=8192)

# Usage example:
# upload_file(ftp, 'local_file.txt', 'remote_file.txt')

import os
from tqdm import tqdm

def download_file(ftp, remote_file, local_file=None):
    if local_file is None:
        local_file = os.path.basename(remote_file)  # Extract filename from the remote path

    file_size = ftp.size(remote_file)

    def callback(data):
        pbar.update(len(data))
        file.write(data)

    with open(local_file, 'wb') as file:
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=f'Downloading {remote_file}') as pbar:
            ftp.retrbinary(f'RETR {remote_file}', callback=callback, blocksize=8192)

# Usage example:
# download_file(ftp, 'remote_file.txt', 'local_file.txt')



def delete_file(ftp, remote_file):
    try:
        ftp.delete(remote_file)
        print(f"File '{remote_file}' deleted successfully.")
    except error_perm as e:
        print(f"FTP Error: {e}")