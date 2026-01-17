# Shellcode XOR Encryptor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)

> A small Python CLI tool that XOR-encrypts shellcode and outputs it as raw bytes, a Python array, or a C array.

## Usage examples

**Raw output:**

```bash
python3 xorencryptor.py --in raw.bin --out encrypted.bin --key test --format raw
```

**C output:**
```bash
python3 xorencryptor.py --in raw.bin --out encrypted.c --key 0x42 --format c
```

| Argument | Description |
| :--- | :--- |
| `--in` | Input file containing raw shellcode. |
| `--out` | Output file for the encrypted payload. |
| `--key` | XOR key (string or hex, e.g. 0x42). |
| `--format` | Output format: raw, python, or c. |

| Output format | Code Example |
| :--- | :--- |
| **C** | `unsigned char buf[] = { 0x12, 0xa1, 0x4f };` |
| **Python** | `buf = [0x12, 0xa1, 0x4f]` |