import os, sys
from colorama import Fore, Style

YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
RED = '\033[1;31m'
WHITE = '\033[1;37m'
END = '\033[0m'

os.system("clear")

def banner():
	print('''

\033[1;37m ███████╗    \033[1;33m██╗  ██╗███████╗██╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ \033[0m
\033[1;37m ██╔════╝    \033[1;33m██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗\033[0m
\033[1;37m █████╗█████╗\033[1;33m█████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝\033[0m
\033[1;37m ██╔══╝╚════╝\033[1;33m██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗\033[0m
\033[1;37m ███████╗    \033[1;33m██║  ██╗███████╗   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║\033[0m
\033[1;37m ╚══════╝    \033[1;33m╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ \033[1;37mv2.0\033[0m

                                  \033[1;41;37m.: GITHUB: R3LI4NT :.\033[0m                                                                                        
''')