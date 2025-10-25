# Enhanced Security Using ECC Combined with Hill Cipher 🔐  

This project implements a **hybrid encryption system** that combines **Elliptic Curve Cryptography (ECC)** and the **Hill Cipher** to achieve both strong public-key encryption and fast symmetric block encryption.  
The hybrid approach enhances security while maintaining computational efficiency, making it suitable for secure data transmission in resource-constrained environments.

> 🧾 **Published Research Paper:**  
> [Enhanced Security using Elliptic Curve Cryptography Combined with Hill Cipher](https://www.scribd.com/document/672185461/Enhanced-Security-using-Elliptic-Curve-Cryptography-Combined-with-Hill-Cipher)

---

## 📘 Overview

Traditional cryptographic systems often trade off between **speed** and **security**.  
This project proposes a **hybrid encryption model** that:
- Uses **ECC** for secure key exchange and asymmetric encryption.  
- Uses the **Hill Cipher** for fast symmetric data encryption.  
- Integrates both mechanisms to strengthen resistance against brute-force and linear attacks.  

---

## 🧠 Key Concepts

- **Elliptic Curve Cryptography (ECC):**  
  Provides high-level security with smaller key sizes compared to RSA.  

- **Hill Cipher:**  
  A matrix-based symmetric cipher used for fast block encryption.  

- **Hybrid Encryption:**  
  Combines ECC’s key-exchange security with Hill Cipher’s computational efficiency.  

---

## ⚙️ Features

- Key generation using ECC domain parameters.  
- Secure session key exchange through ECC.  
- Message encryption/decryption using Hill Cipher matrices.  
- Integration of ECC-derived keys for Hill Cipher encryption.  
- Protection against brute-force attacks with improved key variability.  

---

## 🧩 Project Structure

```bash
CRYPTOGRAPHY_USING_ECC-_AND_HILLCIPHER/
│
├── ecc_hill_cipher.py        # Main hybrid encryption implementation
├── ecc_module.py             # ECC key generation and encryption functions
├── hill_cipher_module.py     # Hill cipher encryption/decryption functions
├── utils.py                  # Helper functions for matrix ops and mod arithmetic
├── requirements.txt          # Dependencies
└── README.md
