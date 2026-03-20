# 🔐 Cipher Decoder

A Python tool that lets you encrypt, decrypt, and crack the Caesar Cipher.
Built for learning how basic cryptography works.

---

## What does it do?

- **Encrypt** -- Turn a normal message into a secret coded message
- **Decrypt** -- Turn a coded message back into normal text
- **Brute Force** -- Try all 26 possible keys to crack a coded message

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/Sarim78/Cipher-Decoder.git
cd Cipher-Decoder
```

**2. Run the script**
```bash
python caesar.py
```

**3. Pick an option from the menu**
```
=============================================
       Cipher Decoder - Caesar Cipher Tool
=============================================

What do you want to do?
  1. Encrypt a message
  2. Decrypt a message
  3. Brute force a ciphertext (unknown key)
```

---

## Try the Sample Ciphers

Sample ciphers are included in the `examples/` folder.
Use them to test the tool and practice cracking ciphers!
```bash
examples/sample_ciphers.txt

---

## How does the Caesar Cipher work?

Every letter in your message gets shifted forward or backward by a number called the key.

```
"HELLO" with key 3 -> "KHOOR"
H -> K
E -> H
L -> O
L -> O
O -> R
```

To decrypt, you just shift in the opposite direction.

Since there are only 26 possible keys, you can try all of them to crack it.
This is called a brute force attack.

---