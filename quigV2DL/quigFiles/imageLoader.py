
import os
res = []

for path in os.listdir():
    if path[-3:] == "png":
        # check if current path is a file
        if os.path.isfile((path)):
            res.append(path)
prev = ""
after = ""
for filename in res:#filename is the name of the file and res is the list of images
    dimensions = "0,0"
    if filename[:2] == "bg":#background is 1200,700 pixels
        dimensions = "1200,700"
    if filename[:2] == "ch":#characters
        dimensions = "50,50"
    if filename[:2] == "ob":#objects
        dimensions = "100,100"
    if filename[:2] == "tr":#tree
        dimensions = "75,150"
    
    
    prev = prev + (filename[3:-4]+",")#removes the .png bit and adds the remains as a variable 
    after = after + "pygame.transform.scale((pygame.image.load('"+filename+"').convert_alpha()),("+dimensions+")),"
imageLoadCode = (prev[:-1]+"="+after[:-1])