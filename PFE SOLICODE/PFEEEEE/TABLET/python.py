import pymysql
import cv2
import qrcode
import numpy as np
from pyzbar.pyzbar import decode
import serial, time
conn = pymysql.connect(host="localhost", user="root", passwd="", db="demo")
mydb = pymysql.connect(host="localhost", user="root", password="", database="client")
mycursor = mydb.cursor()
sqlY = "DROP TABLE customers"
mycursor.execute(sqlY)
sqlYY = "DROP TABLE fct"
mycursor.execute(sqlYY)
sqlYYi = "DROP TABLE payeed"
mycursor.execute(sqlYYi)
mycursor.execute("CREATE TABLE customers (produit VARCHAR(255), prix VARCHAR(255), cid VARCHAR(255))")
mycursor.execute("CREATE TABLE fct (Total VARCHAR(255), cid VARCHAR(255))")
mycursor.execute("CREATE TABLE payeed (naame VARCHAR(255))")
mycursor.execute("SHOW TABLES")
myr = mycursor.fetchall()
STT = str(len(myr))
pp = 'customers' + STT
print(pp)
mycursor.execute("CREATE TABLE " + pp + " (produit VARCHAR(255), prix VARCHAR(255))")
p = 'product'
myCursor = conn.cursor()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 1024)
cap.set(15, 0.1)
font = cv2.FONT_HERSHEY_DUPLEX
org = (20, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2
mafacture = 0
dash = 'PAIMENT EFFECTUER'
sql0 = "INSERT INTO fct (Total, cid) VALUES (%s, %s)"
val0 = (0, pp)
mycursor.execute(sql0, val0)
mydb.commit()
while True:
    logo = cv2.imread('MyQRCode1.png')
    size = 100
    logo = cv2.resize(logo, (size, size))
    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    success, img2 = cap.read()
    cv2.line(img2, (0, 350), (1300, 350), (0, 0, 255), 40)
    cv2.rectangle(img2, (1250, 655), (1250, 690), (0, 0, 0), 150)
    for barcode in decode(img2):
        myData = barcode.data.decode('utf-8')
        sql = "SELECT price FROM " + p + " WHERE product = '" + myData + "'"
        myCursor.execute(sql)
        myResult = myCursor.fetchone()
        if myResult == None:
            print('Sorry change this product')
        else:
            sql1 = "SELECT name FROM " + p + " WHERE product = '" + myData + "'"
            myCursor.execute(sql1)
            myResult1 = myCursor.fetchone()
            # print(myResult)
            EE = myResult1[0]
            E = myResult[0]
            a = int(E)
            # print(a)
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            pts2 = barcode.rect
            pts22 = barcode.rect.top
            # print(pts2)
            if pts22 < 250:
                myOutput = 'Produit Ajouté'
                myColor = (239, 12, 2)
                # arduino.write(b'1')
                time.sleep(2)
                mafacture += a
                up = str(mafacture)
                sql2 = "INSERT INTO customers (produit, prix ,cid) VALUES (%s, %s, %s)"
                val2 = (EE, a, pp)
                mycursor.execute(sql2, val2)
                sql3 = "INSERT INTO " + pp + " (produit, prix) VALUES (%s, %s)"
                val3 = (EE, a)
                mycursor.execute(sql3, val3)
                mydb.commit()
                mydb.commit()
                sqlll = "UPDATE fct SET Total = '"+up+"'"
                mycursor.execute(sqlll)
                mydb.commit()
                # print(mafacture)
                # arduino.write(b'0') and arduino.write([mafacture])
            elif pts22 > 350:
                myOutput = 'Produit Eliminé'
                myColor = (0, 122, 222)
                # arduino.write(b'1')
                time.sleep(2)
                mafacture -= a
                up = str(mafacture)
                # arduino.write(b'0') and arduino.write([mafacture])
                # print(mafacture)
                sql3 = "DELETE  FROM customers WHERE produit = '" + EE + "'"
                mycursor.execute(sql3)
                mydb.commit()
                sqlll = "UPDATE fct SET Total = '" + up + "'"
                mycursor.execute(sqlll)
                mydb.commit()
            else:
                myOutput = 'Zone morte'
                myColor = (120, 122, 22)
                cv2.polylines(img2, [pts], True, myColor, 5)
                cv2.putText(img2, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, myColor,2)
    roi = img2[-size - 10:-10, -size - 10:-10]
    roi[np.where(mask)] = 0
    roi += logo
    data = (mafacture, pp)
    img1 = qrcode.make(data)
    img1.save('MyQRCode1.png')
    cv2.imshow("video", img2)
    cv2.waitKey(1)