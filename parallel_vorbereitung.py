"""Das Modul concurrent.futures"""

import concurrent.futures


def func(arg):
    pass
    
def main():
    
    iterable = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        e = executor.map(func, iterable)
        

if __name__ == '__main__':
    main()
