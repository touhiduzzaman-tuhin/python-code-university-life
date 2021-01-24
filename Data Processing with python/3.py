from ftplib import FTP

def ftp_Downloader(host, user, pas):

    ftp = FTP(host)

    ftp.login(user, pas)

    print(ftp.nlst())


ftp_Downloader("ftp.pyclass.com", "student@pyclass.com", "student123")