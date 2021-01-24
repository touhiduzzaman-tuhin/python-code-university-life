from ftplib import FTP, error_perm

import os

def ftp_Downloader(stationId, start_year, end_year, host = "ftp.pyclass.com", user = "student@pyclass.com", pas
                   = "student123"):

    ftp = FTP(host)

    ftp.login(user, pas)

    ftp.cwd("Data")

    os.chdir("F:\CODE\Python\Data processing with python")

    for year in range(start_year, end_year+1):

        fullpath = "/Data/%s/%s-%s.gz"% (year, stationId, year)

        filename = os.path.basename(fullpath)

        try:

            with open(filename, "wb") as file:

                ftp.retrbinary("RETR %s" % fullpath, file.write)

                print("%s is Downloaded"%filename)

        except error_perm:

            print("%s is not found" %filename)


ftp_Downloader("010010-99999", 2010, 2014)