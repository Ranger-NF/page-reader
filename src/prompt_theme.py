from inquirer.themes import Default
import inquirer
from colorama import Fore

class CustomTheme(Default):

    def __init__(self):
        super().__init__()
        self.List.unselected_color = Fore.GREEN
        self.Question.brackets_color = Fore.LIGHTCYAN_EX

def modified_inquirer_prompt(q):
    return inquirer.prompt(q, theme = CustomTheme())