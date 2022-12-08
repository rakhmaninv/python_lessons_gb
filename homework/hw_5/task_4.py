# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(s: str):
    counter = 1
    previous = ''
    encoded_str = ''
    for current in s:
        if current == previous:
            counter +=1
        else:
            if previous != '':
                encoded_str += str(counter) + previous
            counter = 1
            previous = current
    encoded_str += str(counter) + previous
    return encoded_str

def rle_decode(s: str):
    counter = ''
    decoded_str = ''
    for i in s:
        if i.isdigit():
            counter += i
        else:
            decoded_str += i * int(counter)
            counter = ''
    return decoded_str

string = 'AAAAABBBBBCCCCDDDDDDDEEEFGGHIIIII'
print(string)
encoded = rle_encode(string)
print(encoded)
decoded = rle_decode(encoded)
print(decoded)