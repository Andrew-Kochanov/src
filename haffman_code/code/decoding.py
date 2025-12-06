import pickle
import struct

def decode(encoding: str, dictionary: dict[str, str]) -> str:
    reverse_dict = {value: key for key, value in dictionary.items()}
    
    decoded_letters = []
    current_letter = ""
    
    for bit in encoding:
        current_letter += bit
        if current_letter in reverse_dict:
            decoded_letters.append(reverse_dict[current_letter])
            current_letter = ""
    
    return ''.join(decoded_letters)



def decode_file(input_file: str, output_file: str):
    with open(input_file, 'rb') as f:
        padding = struct.unpack('B', f.read(1))[0]
            
        table_len = struct.unpack('I', f.read(4))[0]
        table = f.read(table_len)
        codes_table = pickle.loads(table)

        encoded_bytes = f.read()
        
    code = ''.join(f'{byte:08b}' for byte in encoded_bytes)
        
    if padding > 0:
        code = code[:-padding]
        
    decoded_text = decode(code, codes_table)
        
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(decoded_text)

