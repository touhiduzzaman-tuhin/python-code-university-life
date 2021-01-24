from ftplib import FTP

import os

def ftp_Downloader(filename, host = "ftp.pyclass.com", user = "student@pyclass.com", pas
                   = "student123"):

    ftp = FTP(host)

    ftp.login(user, pas)

    ftp.cwd("Data")

    os.chdir("F:\CODE\Python\Data processing with python")

    with open(filename, "wb") as file:

        ftp.retrbinary("RETR %s" % filename, file.write)


ftp_Downloader("isd-lite-format.pdf")