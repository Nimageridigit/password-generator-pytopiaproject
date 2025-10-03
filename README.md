# 🔐 Password Generator

This project contains a password generator application written in Python. The generator can create three types of passwords:

1. Random Passwords
2. Memorable Passwords
3. Pin Codes

---

## 🚀 Features
The password generator uses the Python `random` module to generate passwords based on user preferences. The generator is split into three classes, each representing a different type of password generation:

1. `RandomPasswordGenerator` generates a completely random password of a specified length, optional with numbers, and symbols.
2. `MemorablePasswordGenerator` creates a password made up of a set number of randomly chosen words from the NLTK English language corpus. It can optionally separate the words with a separator and use capitalized words.
3. `PinCodeGenerator` creates a numeric password of a specified length.

Each generator class inherits from a base `PasswordGenerator` class. They each override the base class's `generate()` method in order to provide their own unique password generation functionality.
---

## ⚙️ Tech Stack
- Language/Framework: `Python`  
- Tools: `Git`, `GitHub`  

---

## 📂 Installation & Usage

```bash
# 1. Clone the repository
git clone git@github.com:Nimageridigit/password-generator-pytopiaproject.git

# 2. Navigate to project folder
cd REPO-NAME
 # TODO
# 3. Install dependencies
pip install -r requirements.txt
 # TODO
# 4. Run the project
python app.py # TODO
```

---


## 👤 
- [Nimageridigit](https://github.com/Nimageridigit)  
- Email: nimageridi@gmail.com  

---


