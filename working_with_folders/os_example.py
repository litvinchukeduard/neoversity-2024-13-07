'.'
'..'
'/home/users/eduard'

import os

# for i in range(1, 7):

# ('/home/eduard', [...], [...])
for root, dirs, files in os.walk('.'):
    print()
    print(f'Current folder: {root}')
    print(f'Folders: {dirs}')
    print(f'Files {files}')
    print()
