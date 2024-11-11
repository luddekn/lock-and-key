
![Lock&Key](https://dl.dropboxusercontent.com/scl/fi/9oqp3mumdabuqertleppn/lock-and-key-github.png?rlkey=9b07vfcyqgtausavnn5r190nt&st=yhoy6udx&dl=0)
- Created by: [@luddekn](https://github.com/luddekn)
- Powered by Python, MySQL, and Customtkinter
- Current OS support: **Windows**, **Linux**
- [MIT License](https://github.com/luddekn/lock-and-key/blob/main/license.md)

# Appendix
1. **[About Lock&Key](#about-lockkey)**
    - [Features](#features)
2. **[Installation and Set Up](#installation-and-set-up)**
    - [MySQL Server Set Up](#mysql-server-set-up)
    - [Installation](#installation)
        - [Executable Installation](#executable-installation)
        - [Manual Installation Linux](#manual-installation-linux)
        - [Manual Installation Windows](#manual-installation-windows)
    - [Usage](#usage)
        - [Login](#login)
        - [Sign Up](#sign-up)
# About Lock&Key

Lock&Key is a self-hosted, self-managed, open-source password manager. It provides everything you need to store and manage your accounts securely!

Lock&Key is built using Python as its main language with MySQL integrated to help store and manage password entries, it's self-hosted and open-source meaning you as the consumer have full control over everything. The master password for each user is used to encrypt and decrypt all user data with strong encryption to provide secure storage.
## Features
- **Adding account entries**: Create new or add existing account entries.
- **Updating account entries**: Modify account entries with new information.
- **Deleting account entries**: Remove unwanted account entries.
- **Listing account entries**: Display a list of all or specified account entries.
- **Password generation**: Generate random, complex passwords.
- **Encryption**: All data is securely stored with encryption.

# Installation and Set Up
## MySQL Server Set Up
The user needs to have a local MySQL server set up and running, here is how to set up a MySQL server locally:

**IMPORTANT!** - When creating a MySQL user account, remember these credentials, these credentials will be used to establish a database connection when running the application.
- [Windows MySQL server installation (workbench not needed)](https://www.youtube.com/watch?v=u96rVINbAUI)
- [Linux MySQL server installation (Debian)](https://www.youtube.com/watch?v=3qD6zv7thdE)
## Installation
### Executable Installation
The Lock&Key password manager has been packaged as an executable for both Windows and Linux using the "pyinstaller" tool. Downloading the executable for your operating system eliminates the need to install any dependencies. It’s designed to work seamlessly right out of the box!
- [Download Windows executable here.](https://github.com/luddekn/lock-and-key/releases/tag/Lock%26Key-Windows)
- [Download Linux executable here.](https://github.com/luddekn/lock-and-key/releases/tag/Lock%26Key-Linux)
```
Download and launch the executable file.
```
### Manual Installation Linux
Change directory to the /opt directory:
```
cd /opt
```
Clone repository (requires git to be installed):
```
sudo git clone https://github.com/luddekn/lock-and-key
```
Change the directory to the 'lock-and-key' directory:
```
cd lock-and-key
```
Install the required libraries:
```
pip install -r requirements.txt
```
Install and fix the Pillow library:
```
pip install --upgrade --force-reinstall Pillow
```
Now start the password manager from the command line:
```
python3 lock-and-key.py
```
### Manual Installation Windows
Clone repository (requires git to be installed):
```
git clone https://github.com/luddekn/lock-and-key
```
Change the directory to the 'lock-and-key' directory:
```
cd lock-and-key
```
Install the required libraries:
```
pip install -r requirements.txt
```
Install and fix the Pillow library:
```
pip install --upgrade --force-reinstall Pillow
```
Now start the password manager from the command line:
```
python3 lock-and-key.py
```
## Usage
### Login
1. First, log in by providing your MySQL server IP, port, and MySQL user credentials.
2. If you have created a user account, log in as that user to start using the password manager.
### Sign Up
If this is your first time using the password manager you need to create a user account after logging into the MySQL server. Make sure to create a strong password, but you need to remember it or write it down in a safe spot!
