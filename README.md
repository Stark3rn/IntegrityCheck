# IntegrityCheck
A project searching to analyse local files on a computer and check its integrity, detect its modifications and apply YARA rules to them.

----
## Prerequisites
To use this project, the following libraries are required:
### Linux systems
```bash
pip install pyssdeep six python-magic PyQt5 yara-python
```
### Windows systems
```bash
pip install pyssdeep six python-magic-bin PyQt5 yara-python
```
----
## Installation
1. Clone the repo
```bash
git clone https://github.com/Stark3rn/IntegrityCheck.git
cd IntegrityCheck
```
2. Install dependencies (see the prerequisites section)
3. Ensure your folder contains the `rules` folder and the `tests` folder to check the functionnality, also check it contains the `main.py` file to launch the program.
----
## Usage
From the terminal (depending on your python version) :

```
python3 main.py
```

or

```
python main.py
```
----

## Functionalities
- File analysis :
    - Exact hashing (MD5, SHA1, SHA256) and fuzzy hash (SSDEEP)
    - Entropy calculation to detect compressed or enciphered files
- Yara Detection :
    - Scans files with all rules in the `./rules` folder
    - Returns a dictionary mapping rule files to matching rule names
- GUI :
    - PyQt5 to upload and analyse files easily
