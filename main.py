import os
path = os.listdir("./Dicom")
count =0
for dicoms in path:
    #image1 = path[count]
    image1 = os.stat("./Dicom/"+path[count]).st_size
    next = 1
    print("Image 1",image1)
    count+=1
    for next in range(3):
        #image2=path[next]
        image2 = os.stat("./Dicom/"+path[next]).st_size
        next+=1
        print("Image 2",image2)
        if count==next:
            print("Not possible")
        elif image1==image2:
            os.remove("./Dicom/"+path[next])

   