from gtts import gTTS
from inquirer import List
import os
from colorama import Fore

import file_check
import extract_text
import prompt_theme

project_path = os.path.abspath(os.getcwd())


questions = [
    List('file_name',
        message="Which file do you need the extracted text from?",
        choices=os.listdir(project_path + '/Files/'),
    ),

    List("make_audio",
        message="Do you want the text to be made in to an audio file?",
        choices=["Yes","No"],
    ),

    List("make_it_single",
        message="Do you want to it to be made into a sinle line?",
        choices=["Yes","No"],
    ),
    
]

input_from_user = prompt_theme.modified_inquirer_prompt(questions)

target_file_name = input_from_user['file_name']
make_audio = input_from_user['make_audio']
remove_new_lines = input_from_user["make_it_single"]

taget_file_path = project_path + '/Files/' + target_file_name

is_valid_file = file_check.check_valid_file(taget_file_path)

text = ''

if is_valid_file['success']:
    if is_valid_file['file_type'] == 'image':
        text = extract_text.extract_from_image(taget_file_path)
    elif is_valid_file['file_type'] == 'pdf':
        text = extract_text.extract_from_pdf(taget_file_path)
    
    if remove_new_lines == 'Yes' :
        text = text.replace("\n", " ")

    print(text)


if make_audio == 'Yes' and text:

    try:
        tts = gTTS(text.replace('\n', ' '))
        tts.save('text.wav')
        print(Fore.GREEN + 'Success!' + Fore.RESET)
    except:
        print(Fore.RED + 'Failed!' + Fore.RESET)
