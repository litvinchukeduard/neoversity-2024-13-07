import sys

print(sys.argv) # ['sys_example.py', '/home/users/eduard']
"""
Написати додоток, який буде отримувати шлях до файлу через термінал і виводити цей файл
"""

# print('Hello!')
def print_file(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        # print(f.read())
        for line in f:
            # print(line.rstrip())
            print(line, end='')
    # f = open(path, 'r', encoding='utf-8')
    # f.close()

if len(sys.argv) > 1:
    path_to_file = sys.argv[1]
    print_file(path_to_file)
else:
    print('Please provide path to file')

# C:\Users\User\Documents\file.txt
# /home/user/documents/file.txt

# /Users/eddielitvinchuk/Documents/Repositories/neoversity-13-0/file.txt
