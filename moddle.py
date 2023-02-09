from colorama import init, Fore


def display(message, is_warning=False):
    if is_warning:
        # print('This is a warning')
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)