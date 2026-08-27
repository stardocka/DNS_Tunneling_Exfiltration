# DNS Exfiltration

Simple Python script that encodes the content of a text file with Base32, splits it into chunks, and sends the chunks through DNS TXT queries.

> For educational purposes, CTFs, labs, and authorized security testing only.

## Requirements

* Python 3
* `pydig`

Install the dependency:

```bash
pip install pydig
```

## Setup

Put the file you want to process in the project directory and name it:

```text
texte.txt
```

The script also requires one or more domains that you control or are authorized to use.

## Usage

Run the script:

```bash
python script.py
```

You will get the following menu:

```text
===== MENU =====
1. Define number of domain names
2. Define delay between DNS requests
3. Enable or disable random domain order
4. Start DNS exfiltration
5. Quit
```

### 1. Domain names

Choose `1` and enter the number of domains:

```text
Number of domain names: 2
Domain name #1: example.com
Domain name #2: example.net
```

The domains are used alternately for the generated DNS queries.

### 2. Request delay

Choose `2` to set the delay between requests:

```text
Delay between requests (seconds): 1
```

Use `0` to disable the delay.

### 3. Random order

Choose `3` to enable or disable random domain order:

```text
Random order (yes/no): yes
```

If enabled, the domain list is shuffled before sending the requests.

### 4. Start

Choose `4` to start the process.

Generated domain names are printed to the terminal:

```text
0_JBSWY3DPEBLW64TMMQ.example.com
1_KRSXG5A.example.net
```

The script sends a DNS `TXT` query for each generated domain.

## How it works

The file content is first encoded using Base32:

```python
base64.b32encode(content.encode())
```

The `=` padding is removed and the encoded data is split into smaller chunks.

Each chunk receives a sequence number:

```text
0_<chunk>
1_<chunk>
2_<chunk>
```

The chunks are then added as DNS labels:

```text
0_<chunk>.example.com
```

## Project structure

```text
.
├── script.py
├── texte.txt
└── README.md
```

## Notes

* The input file is currently hardcoded as `texte.txt`.
* DNS errors are ignored by the script.
* The script does not process DNS responses.
* There is no automatic reconstruction of the original file.
* Only use domains and systems you are authorized to test.

## Disclaimer

This project is intended for security research, education, and authorized testing. Do not use it to transfer data from systems without permission.
