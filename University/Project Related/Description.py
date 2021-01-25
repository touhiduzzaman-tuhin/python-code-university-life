import cv2

"""
    import opencv
    which is one of the package that install manually in interpreter
    
"""

import numpy as np

"""
    import numpy and declare as np
    if next time need to call bumpy then just call it np
    
    numpy is also one of the package that install in manually interpreter

"""

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

"""

    read the main image as input image
    
    here,
    img = variable
    cv2 = opencv version
    imread = call opencv to read image as input
    F:\Final Project\Images = Folder directory
    ronaldo.jgp = main image name and image type
    
    
     when image is read it is mainly collect the n-dimensional array
     and it's colour image we also called it BGR
     
     BGR = means collection of Blue, Green and Red values
     Values Are start with 0 and
     and end with 255

"""

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""

    convert the main image into gray image with the help of cvtColor
    which takes two parameter sources image and code

    here,
    gary_img = variable
    cv2 = opencv version
    cvtColor = call opencv to convert image scale
    img = main image that we want to convert as gray image
    COLOR_BGR2GRAY = use this pre-define opencv resources to convert
    main image into gray image
    
    Gray image means black and white image
    
    BGR image value = 0
    Gray image value = 1

"""

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

"""

    read the face image as input Gray image 

    here,
    face = variable
    cv2 = opencv version
    imread = call opencv to read image as input
    F:\Final Project\Images = Folder directory
    ronaldo_face.jgp = face image name and image type


     After read the image insert 0
     when 0 insert then the image automatic convert into gray image

"""

w, h = face.shape[::-1]

"""

    select the rectangle height and width which is
    same size of face image where detect
    
    w = width of the rectangle
    h = height of the rectangle
    face.shape = is the size of the image return n-dimensional array
    
    like = (128, 128) ===gray
    like = (128, 128, 3) === colour
    
    for gray image it gives two value and
    colour image it gives three value
    
    here we also give the index [::-1]
    that gives the rectangle like
    
      ......
      .    . 
      .    .
      .    .
      ......
      
      
    if we set the index like [::1]
    then the rectangle looks like
    
    ............
    .          .
    .          .
    ............ 
    

"""

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)



"""

    match the main image and face image and
    it returns all n-dimensional array value for all match point

    create a variable as res
    matchTemplate = to match the image its pre-define function of opencv
    it takes three parameter main image, template image, method
    
    gray_image = main
    face = template image
    TM_CCOEFF_NORMED = Template match method
    
    There are mainly six method for template match
    1)TM_CCOEFF_NORMED
    2)TM_CCOEFF
    3)TM_SQDIFF_NORMED
    4)TM_SQDIFF
    5)TM_CCORR_NORMED
    6)TM_CCORR
    
    
    All the Normed Method are useful so here we can use any of them
    1)TM_CCOEFF_NORMED
    2)TM_SQDIFF_NORMED
    3)TM_CCORR_NORMED
    
    Description of all these method sent into another link
     
    
    it returns thousand of n-dimensional array value
    these values range (-infinity to +infinity )
    
    Highest value of the array is brightest point int the image
    and we need the highest value
    

"""

print(res)

"""

    Print is the pre-define function of python that print anything 

    Here print the res value

"""

value = 0.95

"""

    create a variable call value
    
    set the value and check loc value and change to find the highest value

"""

loc = np.where(res >= value)

"""

    find the highest value to help of the numpy 
    
    Here,
    
    loc is a variable
    
    np = numpy
    where = is the condition as like if
    
    if(res >= value) == np.where(res >= value)
    
    when condition true it store the value otherwise ignore
    
    

"""

print(loc)


"""

    Print is the pre-define function of python that print anything 
    
    Here print all the loc value

"""


font = cv2.FONT_HERSHEY_SIMPLEX

"""

    use the font Style help of opencv pre-define function
    Here we use FONT_HERSHEY_SIMPLEX this font style

"""


for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)




"""

    Draw the Rectangle with help of rectangle function or 
    method which takes few arguments or parameter like 
    
    sources image === img
    
    starting point of x axis   ...
    starting point of y axis   ...
    ending point of x axis     ... (i[0] + w, i[1] + h)
    ending point of y axis     ... 
    
    colour of rectangle ====(0, 0, 255)
    thickness of rectangle === 2
    

"""
cv2.putText(img, "Ronaldo", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)


"""

    print name of the match object in the image with the help of
    putText function which takes few parameter like
    
    
    sources image ===img
    
    Text = Ronaldo   
    object name
    
    location = (i[0] + w, i[1] + h)
    where rectangle create
    
    font-style = font
    which declare above the for loop
    
    
    font-scale = 0.8
    which means font pixel in percentage
    
    color = Text Color
    
    thickness = 2
    which means density of every character 
    
    Line-type = Line_AA
    

"""

cv2.imshow("Main Image", img)

"""

    show the output final image
    
    here,
    
    imshow = call opencv to show image as output
    
    Main Image = window name of the output image

"""

cv2.waitKey(0)


"""

    waitKey() is the function or method 
    that wait for a key that press by user
    here when output show, if the user press 0 then 
    close the output window

"""

cv2.destroyAllWindows()

"""

    destroyAllWindows() is the function or method 
    that close the output window and destroy the output temporary

"""