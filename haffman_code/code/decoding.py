import pickle
import struct

def decode(encoding: str, dictionary: dict[str, str]) -> str:
    decoding = ''

    i = 0
    while i < len(encoding):
        for key in dictionary:
            value = dictionary[key]
            if value == encoding[i:len(value) + i]:
                i += len(value)
                decoding += key
                break
    return decoding

# print(decode('001101', {'1': '00', '3': '01', '2': '1'}))

def decode_file(input_file: str, output_file: str):
    try:
        with open(input_file, 'rb') as f:
            padding = struct.unpack('B', f.read(1))[0]
            
            table_len = struct.unpack('I', f.read(4))[0]
            table = f.read(table_length)
            codes_table = pickle.loads(table_data)

            encoded_bytes = f.read()
        
        # Преобразование байтов в битовую строку
        code = ''.join(f'{byte:08b}' for byte in encoded_bytes)
        
        # Удаление дополнения
        if padding > 0:
            code = code[:-padding]
        
        # Декодирование
        decoded_text = decode(code, codes_table)
        
        # Сохранение декодированного текста
        with open(output_file, 'w') as f:
            f.write(decoded_text)
