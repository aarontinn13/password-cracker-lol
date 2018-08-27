import zipfile
import itertools


def brute_force_attack(filename, chars, n):
    def permutations(chars,n):
        all_perms = [''.join(x) for i in range(1,n) for x in itertools.product(chars,repeat=i+1)]
        return all_perms

    with zipfile.ZipFile(filename, 'r') as zip_file:
        for i in permutations(chars,n):
            i = str.encode(i)
            try:
                zip_file.extractall(pwd=i)
                print('Password:', i.decode('utf-8'))
                return
            except zipfile.BadZipFile:
                continue
            except RuntimeError:
                continue
    raise LookupError



def dictionary_attack(filename, dict_file, max_words=None):
    def read_file(dict_file, max_words=None):
        with open(dict_file, 'r', encoding='latin-1') as download_file:
            all_words = download_file.read().split()
        return all_words

    with zipfile.ZipFile(filename, 'r') as zip_file:
        for i in read_file(dict_file,max_words):
            i = str.encode(i)
            try:
                zip_file.extractall(pwd=i)
                print('Password:', i.decode('utf-8'))
                return
            except zipfile.BadZipFile:
                continue
            except RuntimeError:
                continue
    raise LookupError


def main():
    while True:
        x = str(input('Enter .zip file: '))
        y = str(input('Cracking Method <bruteforce> or <dictionary>: ' ))
        string = 'abcdefghijklmnopqrstuvwxyz'
        if y == 'bruteforce':
            try:
                z = int(input('Maximum Length: '))
                brute_force_attack(x, string, z )
                break
            except FileNotFoundError:
                print('This file was not found!\n')
                continue

        elif y == 'dictionary':
            try:
                z = str(input('Enter dictionary file: '))
                dictionary_attack(x,z)
                break
            except FileNotFoundError:
                print('This file was not found! \n')
                continue


if __name__ == '__main__':
    main()
