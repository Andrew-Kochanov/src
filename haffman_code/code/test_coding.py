from encoding import encode_file
from decoding import decode_file

encode_file("origin_file.txt", "encoding_file.txt")
decode_file("encoding_file.txt", "decoding_file.txt")

def test_unit():
    origin_file = open('origin_file.txt').read()
    decoding_file = open('decoding_file.txt').read()
    assert origin_file == decoding_file

