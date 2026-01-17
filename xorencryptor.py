import argparse
import sys
import os

def xor_data(data, key):
    """
    Encrypts data using XOR with the given key.
    """
    key_bytes = key.encode()
    key_len = len(key_bytes)
    
    encrypted_data = bytearray()
    
    for i in range(len(data)):
        current_byte = data[i]
        key_byte = key_bytes[i % key_len]
        encrypted_data.append(current_byte ^ key_byte)
        
    return encrypted_data

def main():
    parser = argparse.ArgumentParser(description="Shellcode XOR Encryptor")
    
    parser.add_argument("--in", dest="infile", required=True, help="Input binary file")
    parser.add_argument("--out", required=True, help="Output file")
    parser.add_argument("--key", required=True, help="XOR encryption key")
    parser.add_argument("--format", choices=['raw', 'c', 'python'], default='raw', help="Output format")

    args = parser.parse_args()

    if not os.path.exists(args.infile):
        print(f"[-] Error: Input file '{args.infile}' not found.")
        sys.exit(1)

    try:
        with open(args.infile, "rb") as f:
            shellcode_data = f.read()
            print(f"[*] Loaded {len(shellcode_data)} bytes")
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        sys.exit(1)

    print(f"[*] Encrypting with key: {args.key}")
    encrypted_payload = xor_data(shellcode_data, args.key)

    # just raw ATM
    try:
        with open(args.out, "wb") as f:
            f.write(encrypted_payload)
        print(f"[+] Encrypted data written to {args.out}")
        
    except Exception as e:
        print(f"[-] Error writing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()