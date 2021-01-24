from ftplib import FTP

ftp1 = FTP("ftp.pyclass.com")

ftp1.login("student@pyclass.com", "student123")

l = ftp1.nlst()

print(l)

n = ftp1.nlst("Data")

print(n)

print(ftp1.cwd("Data"))

print(ftp1.cwd(".."))

ftp1.close()