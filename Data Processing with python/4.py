from ftplib import FTP

import os

def ftp_Downloader(host, user, pas):

    ftp = FTP(host)

    ftp.login(user, pas)

    ftp.cwd("Data")

    os.chdir("F:\CODE\Python\Data processing with python")

    with open("isd-lite-format.pdf", "wb") as file:

        ftp.retrbinary("RETR isd-lite-format.pdf", file.write)


ftp_Downloader("ftp.pyclass.com", "student@pyclass.com", "student123")