# Shellcode XOR Encryptor

A small Python CLI tool that XOR-encrypts shellcode and outputs it as raw bytes, a Python array, or a C array.

## Usage

python xorcrypt.py --in raw.bin --out encrypted.bin --key test --format raw

Example using a hex key and C output:

python xorcrypt.py --in raw.bin --out encrypted.c --key 0x42 --format c

## Arguments

--in            input file containing raw shellcode  
--out           output file  
--key           XOR key (string or hex, e.g. 0x42)  
--format        output format: raw, python, or c  

## Example output

C:
unsigned char buf[] = { 0x12, 0xa1, 0x4f };

Python:
buf = [0x12, 0xa1, 0x4f]