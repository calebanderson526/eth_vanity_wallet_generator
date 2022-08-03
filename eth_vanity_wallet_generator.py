from eth_account import Account
import secrets
import multiprocessing
import time
import math
import string


def main():
    input_strings = []
    print('Wallet prefixes longer than 6 characters will take very long to generate, shorter prefixes are found faster')
    print('This program will use floor(0.9 * your available cpus) so if you have 12 threads, it will use 10 of them at 100%\n')
    while True:
        val = input("Enter your desired wallet prefix, or enter n to start generating wallets: ")
        if val == 'n' and len(input_strings) == 0:
            print('you must have at least one wallet prefix inputted')
        elif val == 'n' and not len(input_strings) == 0:
            break
        test = True
        for c in val:
            if c not in string.hexdigits:
                print('input string must only contain a-f or 0-9')
                test = False
                break
        if test:
            input_strings.append(val)
    hour = input('How long would you like to search for wallets? (in hours): ')
    avail_cpus = multiprocessing.cpu_count()
    processes = []
    start = time.perf_counter()
    for i in range(0, math.floor(avail_cpus * .9)):
        processes.append(multiprocessing.Process(target=absolute_memes, args=(input_strings,)))
        processes[i].start()
        print('Starting process: ' + str(i + 1))
    print('generating wallets')
    while True:
        if time.perf_counter() - start > (3600 * float(hour)):
            for p in processes:
                p.kill()
            break


def absolute_memes(prefixes):
    while True:
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key)
        addr = acct.address
        for p in prefixes:
            last_index = 2 + len(p)
            if addr[2: last_index] == p:
                with open(p + '_wallets.txt', 'a') as memes:
                    memes.write(addr + ', ' + private_key + '\n')
                    print(p + ' wallet found')


if __name__ == '__main__':
    main()

