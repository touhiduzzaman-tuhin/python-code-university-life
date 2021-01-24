f = open('tuhin.jpg', 'rb')

f1 = open('tuhin_img.jpg', 'wb')


for i in f:

    f1.write(i)

f.close()