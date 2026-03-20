# 🛡️ Password Generator Pro

[EN] A simple, secure password generator in Python
[PL] Prosty i bezpieczny generator haseł w Pythonie

---

## ✨ Features / Funkcje

### 🇬🇧 English
* **Dynamic Length:** Choose between 8 and 20 characters.
* **Smart Validation:** Prevents invalid input using a `while` loop.
* **Docker Support:** Runs in an isolated container.
* **GitHub Actions:** Automated build and test on every push.

### 🇵🇱 Polski
* **Dynamiczna długość:** Wybór od 8 do 20 znaków.
* **Inteligentna walidacja:** Pętla `while` blokuje błędne dane wejściowe.
* **Wsparcie Docker:** Działa w odizolowanym kontenerze.
* **GitHub Actions:** Automatyczne budowanie i testy przy każdym wypchnięciu kodu.

---

## 🚀 How to run? / Jak uruchomić?

### 1. Local / Lokalnie (Python)
```bash
python app.py
```

### 2. Docker (Interactive / Interaktywnie)
```bash
docker build -t pass-generator .
docker run -it pass-generator
```


### 3. Docker (Automated / Automatycznie)
```bash 
# Use environment variable to bypass manual input
# Użyj zmiennej środowiskowej, aby pominąć wpisywanie ręczne
docker run -e LENGTH_PASSWORD=15 pass-generator
```

## 🛠️ Tech Stack / Technologia
- Language: Python 3.x ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- DevOps: Docker, GitHub Actions
- Libraries: os, random, string