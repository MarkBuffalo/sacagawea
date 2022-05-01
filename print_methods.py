from colorama import Fore
from tqdm import tqdm

FORE1 = Fore.WHITE
FORE2 = Fore.LIGHTGREEN_EX

FORE_WARNING = Fore.YELLOW
FORE_ERROR = Fore.RED
FORE_SUCCESS = Fore.LIGHTBLUE_EX
FORE_INFORMATION = Fore.LIGHTBLUE_EX

BAR1 = Fore.LIGHTCYAN_EX
BAR2 = Fore.LIGHTBLUE_EX


# Regular printing via tqdm, so it doesn't get in the way of the progress bar. No colors.
def t_print(msg):
    tqdm.write(msg)


# Color printing via tqdm. We don't want this to get in the way of the progressbar.
def ct_print(msg):
    tqdm.write(colorize_output(msg))


# Non-tqdm-based printing
def c_print(msg):
    print(colorize_output(msg))


# Color format. Not perfect.
def colorize_output(msg):
    return msg.replace("[", f"{FORE2}[{FORE1}"). \
               replace("]", f"{FORE2}]{FORE1}"). \
               replace("?", f"{FORE_WARNING}?{FORE1}"). \
               replace("!", f"{FORE_SUCCESS}!{FORE1}"). \
               replace("*", f"{FORE_INFORMATION}*{FORE1}"). \
               replace("|", f"{FORE2}|{FORE1}"). \
               replace(": ", f"{FORE2}:{FORE1} ") + Fore.RESET


# This is so we can use different colors for the progress bar.
def colorize_bar_output(msg):
    return msg.replace("[", f"{BAR2}[{BAR1}"). \
               replace("]", f"{BAR2}]{BAR1}"). \
               replace("?", f"{FORE_WARNING}?{BAR1}"). \
               replace("!", f"{FORE_SUCCESS}!{BAR1}"). \
               replace("*", f"{FORE_INFORMATION}*{BAR1}"). \
               replace("|", f"{BAR2}|{BAR1}"). \
               replace(": ", f"{BAR2}:{BAR1} ") + Fore.RESET
