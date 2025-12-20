from encoding import encode_file
from decoding import decode_file

encode_file("origin_file.txt", "encoding_file.txt")
decode_file("encoding_file.txt", "decoding_file.txt")

def make_file(str):
    with open(str, 'w', encoding = 'utf-8') as file:
        file.write('Hello, World!')

def test_unit():
    make_file('origin_file.txt')
    origin_file = open('origin_file.txt').read()
    decoding_file = open('decoding_file.txt').read()
    assert origin_file == decoding_file

