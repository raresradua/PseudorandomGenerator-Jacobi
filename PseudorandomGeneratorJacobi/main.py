# Jacobi

import zipfile
import random
import sympy
import os
from datetime import datetime


def jacobi(a, n):
    b = a % n
    c = n
    s = 1
    while b >= 2:
        while b % 4 == 0:
            b = b // 4
        if b % 2 == 0:
            if c % 8 == 3 or c % 8 == 5:
                s = -s
            b = b // 2
        if b == 1:
            break
        if b % 4 == c % 4 == 3:
            s = -s
        b, c = c % b, b
    return s * b


def generate_large_prime():
    current_prime = sympy.randprime(2 ** 511, 2 ** 1024)
    #    while current_prime % 4 != 3:
    #    current_prime = sympy.randprime(2 ** 511, 2 ** 1024)
    return current_prime


def bit_freq(bit_out):
    freq = {}
    for i in range(len(bit_out)):
        if bit_out[i] in freq:
            freq[bit_out[i]] += 1
        else:
            freq[bit_out[i]] = 1
    for i in freq:
        print(i + ": " + str((freq[i] * 100 / len(bit_out))) + "%")


def current_time_to_seconds():
    current_time = datetime.now().time()
    in_seconds = current_time.second + current_time.minute * 60 + current_time.hour * 3600
    return in_seconds


def generate_a(n):
    return random.randint(1, n)


def gcd(a, n):
    while n != 0:
        a, n = n, a % n
    return a


def coprime(a, n):
    return gcd(a, n) == 1


def write_file(filename, bit_out):
    file = open(filename, "w")
    file.write(bit_out)
    file.close()


def compress_file(filename):
    file = zipfile.ZipFile(filename + ".zip", "w")
    file.write(filename, compress_type=zipfile.ZIP_DEFLATED)
    file.close()


def main():
    bit_out = ""
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()
    n = p * q
    a = generate_a(n)
    while not coprime(a, n):
        a = generate_a(n)
    for i in range(2 ** 15):
        jacobi_symbol = jacobi(a + i + 1, n)
        bit_res = int((jacobi_symbol + 1) / 2)
        bit_out += str(bit_res)
    print(bit_out)
    bit_freq(bit_out)

    write_file("jacobi.txt", bit_out)
    file_size = os.path.getsize("jacobi.txt")
    compress_file("jacobi.txt")
    file_compressed_size = os.path.getsize("jacobi.txt.zip")
    print("Size file before compression: " + str(file_size))
    print("Compressed file: " + str(file_compressed_size))

    just_ones = ""
    for i in range(2 ** 20):
        just_ones += (str(1))

    write_file("ones.txt", just_ones)
    file_size = os.path.getsize("ones.txt")
    compress_file("ones.txt")
    file_compressed_size = os.path.getsize("ones.txt.zip")
    print("Size file before compression: " + str(file_size))
    print("Compressed file: " + str(file_compressed_size))


if __name__ == '__main__':
    main()





#def jacobi(a, n):
#    assert (n > a > 0 and n % 2 == 1)
#    s = 1
#    while a != 0:
#        while a % 2 == 0:
#            a = a // 2
#            r = n % 8
#            if r == 3 or r == 5:
#                s = -s
#        a, n = n, a
#        if a % 4 == n % 4 == 3:
#            s = -s
#        a = a % n
#    if n == 1:
#        return s
#    else:
#        return 0
