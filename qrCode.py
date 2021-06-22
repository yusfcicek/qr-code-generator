import pyqrcode
import pandas as pd
import os
import sys


def preliminary():

    global urls
    urls = pd.read_csv(sys.argv[1])
    myFolder = "QR Codes"

    if not os.path.exists(myFolder):
        os.mkdir(myFolder)

    myPath = os.getcwd()
    os.chdir("{}/{}/".format(myPath, myFolder))


def createQR():

    for index in range(len(urls)):
        s = urls.iloc[index][0]
        url = pyqrcode.create(s)
        url.png("{}.png".format(str(s)), scale=6)


def main():

    print("Process is starting may take a while...")
    preliminary()
    print("A folder has been created to contain the Qr Codes...")
    createQR()
    print("Process completed...")


if __name__ == "__main__":
    main()
