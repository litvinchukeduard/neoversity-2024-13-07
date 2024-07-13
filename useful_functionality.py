'''
Some useful functions


'''

def return_one() -> int:
    return 1

# Hello, world -> ['Hello,', 'world']
def split_into_words(line: str) -> list[str]:
    return line.split(' ')

# print(dir("Hello"))
print(__name__)
if __name__ == '__main__':
    print(return_one())
