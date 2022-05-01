from print_methods import colorize_output, ct_print, c_print, t_print
from colorama import Fore


class Banner:
    def __init__(self):
        self.c = Fore.LIGHTCYAN_EX
        self.d = Fore.LIGHTBLUE_EX
        self.e = Fore.RED
        self.g = Fore.LIGHTCYAN_EX
        self.r = Fore.RESET

        self.banner = ""
        self.banner += f"         {self.d},{self.r}\n"
        self.banner += f"        {self.c}/{self.d}:{self.c}\\{self.r}\n"
        self.banner += f"        {self.c}>{self.d}:{self.c}<{self.r}  This project is dedicated to{self.r}\n"
        self.banner += f"        {self.c}>{self.d}:{self.c}<  {self.r}Missing {self.d}and{self.r} Murdered Indigenous Women{self.r}\n"
        self.banner += f"        {self.c}>{self.d}:{self.c}<  \n"
        self.banner += f"   {self.e},,,,,{self.c}\\{self.d}:{self.c}/{self.r}  May you find your way home...{self.r}\n"
        self.banner += f"  {self.g}#########{self.r}\n"
        self.banner += f"{self.d}//////\\\\\\\\ \\{self.r}\n"
        self.banner += f"{self.d}// {self.c} _   _{self.d}  \\\\  .---.{self.r}\n"
        self.banner += f"{self.d}\(  {self.r}O {self.c}_{self.r} O{self.c}  )/  \\___  ,-. ,-. ,-. ,-. ,-. . , , ,-. ,-.{self.r}\n"
        self.banner += f"{self.d}/\\\\{self.e}=  {self.c}_\\{self.e} ={self.d}//\      {self.r}\\ ,-| |   ,-| | | ,-| |/|/  |-' ,-|{self.r}\n"
        self.banner += f"{self.d}\\\\/\\ {self.c}---{self.d} /\//  {self.c}`---' `-^ `-' `-^ `-| `-^ ' {self.d}'   `-' `-^{self.r}\n"
        self.banner += f"{self.d}//\ '---' /\\\\                     {self.r},|{self.r}\n"
        self.banner += f"{self.d}\//       \\\\/                     `'{self.r}\n"
        self.banner += f"{self.d}/\\\\       //\\\\{self.r}\n"
        self.banner += f"{self.d}\\\\/       \\//{self.r}\n"
        self.banner += f"{self.e} #         #{self.r}\n"
        self.banner += f"{self.c} \"         \"{self.r}\n"

        print(self.banner)