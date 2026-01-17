import os
import sys
import argparse

def parse_key(key):
    """
    Allows hex XORkeys.
    """
    if key.startswith("0x"):
        return bytes.fromhex(key[2:])
    return key.encode()


def xor_data(data, key):
    """
    Encrypts data using XOR with the given key.
    """
    key_bytes = parse_key(key)
    key_len = len(key_bytes)

    
    encrypted_data = bytearray()
    
    # Loop through data and XOR with key
    for i in range(len(data)):
        current_byte = data[i]
        key_byte = key_bytes[i % key_len]
        encrypted_data.append(current_byte ^ key_byte)
        
    return encrypted_data

def format_output(data, output_format):
    """
    Formats the encrypted bytes into C or Python style strings.
    """
    # Create hex strings
    hex_values = [f"0x{b:02x}" for b in data]
    
    if output_format == 'c':
        payload = ", ".join(hex_values)
        return f"unsigned char buf[] = {{ {payload} }};"
        
    elif output_format == 'python':
        payload = ", ".join(hex_values)
        return f"buf = [{payload}]"
        
    return data

def main():
    parser = argparse.ArgumentParser(description="Shellcode XOR Encryptor")
    
    parser.add_argument("--in", dest="infile", required=True, help="Input binary file")
    parser.add_argument("--out", required=True, help="Output file")
    parser.add_argument("--key", required=True, help="Encryption key")
    parser.add_argument("--format", choices=['raw', 'c', 'python'], default='raw', help="Output format")

    args = parser.parse_args()

    # Check input file
    if not os.path.exists(args.infile):
        print(f"[-] Error: Input file '{args.infile}' not found.")
        sys.exit(1)

    # Read input file
    try:
        with open(args.infile, "rb") as f:
            shellcode_data = f.read()
            print(f"[*] Loaded {len(shellcode_data)} bytes from {args.infile}")
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        sys.exit(1)

    #  Encrypt payload
    print(f"[*] Encrypting with key: {args.key}")
    encrypted_payload = xor_data(shellcode_data, args.key)

    # Format Output
    output_content = format_output(encrypted_payload, args.format)

    # Write to file
    try:
        # Use 'wb' for raw, 'w' for text
        mode = "wb" if args.format == 'raw' else "w"
        
        with open(args.out, mode) as f:
            f.write(output_content)
            
        print(f"[+] Successfully wrote {args.format} output to {args.out}")
        
        # Preview for non-raw formats
        if args.format != 'raw':
            print("\n--- Preview ---")
            print(output_content[:100] + ("..." if len(output_content) > 100 else ""))
            print("---------------")

    except Exception as e:
        print(f"[-] Error writing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()