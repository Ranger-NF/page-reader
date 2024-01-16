import os
from colorama import Fore
img_file_extensions = ['.png', '.jpg', '.jpeg']

def check_valid_file(file_path):
    filename, file_extension = os.path.splitext(file_path)

    if file_extension in img_file_extensions:
        return {'success': True, 'file_type': 'image'}

    if file_extension == '.pdf':
        return {'success': True, 'file_type': 'pdf'}

    print(f'{Fore.RED} I need a file with {" , ".join(img_file_extensions)} or .pdf extension {Fore.RESET}')
    return {'success': False}
