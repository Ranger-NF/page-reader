from gtts import gTTS
from inquirer import List
import os
from colorama import Fore
from tkinter import filedialog

from logger import log_error
import file_check
import extract_text
import prompt_theme
from process_input import extract_inputs

project_path = os.path.abspath(os.getcwd())
path_to_usable_files = project_path
BROWSE_BTN = "Browse..."


def get_available_files():
    available_files = os.listdir(path_to_usable_files)

    if not len(available_files) > 0:
        return

    return available_files


def prepare_questions(usable_files: list = None, isInitial: bool = False):

    if isInitial:
        questions = [
            List('file_name',
                 message="Which file do you need the extracted text from?",
                 choices=usable_files,
                 )
        ]

        return questions

    questions = [
        List("make_audio",
             message="Do you want the text to be made in to an audio file?",
             choices=["Yes", "No"],
             ),

        List("make_it_single",
             message="Do you want to it to be made into a single line?",
             choices=["Yes", "No"],
             ),
        List("lang_to_be_used",
             message="Which language should I identify from it?",
             choices=["Malayalam", "English"],
             ),

    ]

    return questions


usable_files = get_available_files()

if not usable_files:
    usable_files = [BROWSE_BTN]
else:
    usable_files.append(BROWSE_BTN)

file_from_user = prompt_theme.modified_inquirer_prompt(
    prepare_questions(usable_files, True)
)

target_file_name = file_from_user['file_name']

if target_file_name == BROWSE_BTN:
    taget_file_path = filedialog.askopenfilename(
        filetypes=[("PNG image", ".png"), ("PDF File", ".pdf")])
else:
    taget_file_path = path_to_usable_files + target_file_name

input_from_user = prompt_theme.modified_inquirer_prompt(
    prepare_questions()
)



lang_to_be_used = 'eng'

# if lang_requested == 'Malayalam':
#     lang_to_be_used = 'mal'
# elif lang_requested == 'English':
#     lang_to_be_used = 'eng'


is_valid_file = file_check.check_valid_file(taget_file_path)

text = ''

if is_valid_file['success']:
    if is_valid_file['file_type'] == 'image':
        text = extract_text.extract_from_image(
            taget_file_path, lang_to_be_used)
    elif is_valid_file['file_type'] == 'pdf':
        text = extract_text.extract_from_pdf(
            taget_file_path, lang_to_be_used)

    # if remove_new_lines == 'Yes':
    #     text = text.replace("\n", " ")

    print(text)

# if make_audio == 'Yes' and text:

#     try:
#         tts = gTTS(text.replace('\n', ' '))
#         tts.save('text.wav')
#         print(Fore.GREEN + 'Success!' + Fore.RESET)
#     except:
#         print(Fore.RED + 'Failed!' + Fore.RESET)
