from colorama import Fore, Back, Style

# print(Fore.BLUE + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


print(Fore.BLUE + Back.GREEN + 'blue with green background' + Style.RESET_ALL)
print("Not green")

print(Fore.BLUE + "B" + Fore.GREEN + "G" + Style.RESET_ALL)
