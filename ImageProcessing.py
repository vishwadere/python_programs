from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

initial_image = Image.open("Tajmahal.jpeg")
image = np.array(Image.open('Tajmahal.jpeg'))

def display():
    initial_image.show()

def brightness():
    b=int(input("Enter the value for brightness: "))
    bright = image + b
    Image.fromarray(bright).save('Tajmahal_b.jpeg')
    brightImage = Image.open("Tajmahal_b.jpeg")
    brightImage.show()

def diffence():
    orImage = np.array(Image.open("Tajmahal.jpeg"))
    brightened = orImage + 100
    Image.fromarray(brightened).save('Tajmahal_brightened.jpeg')
    brArray = np.array(Image.open('Tajmahal_brightened.jpeg'))
    diffArr = brightened - orImage
    Image.fromarray(diffArr).show()
    #imageDifference.show()

def negative():
    bright = 255 - image
    Image.fromarray(bright).save('Tajmahal_i.jpeg')
    negativeImage = Image.open("Tajmahal_i.jpeg")
    negativeImage.show()

def threshold():
    th=int(input("Enter Threshold Value"))
    im = np.array(Image.open('Tajmahal.jpeg').resize((200,200)))
    w=im
    for i in range(0,200):
        for j in range(0, 200):
            for k in range(0,3):
                if(im[i][j][k] > th):
                    w[i][j][k] = 1
                else:
                    w[i][j][k] = 0
    Image.fromarray(w).save('Tajmahal_t.jpeg')
    t= Image.open("Tajmahal_t.jpeg")
    t.show()

def histogram():
    histo= np.array(Image.open('Tajmahal.jpeg').convert('L'))
    plt.hist(histo)
    plt.show()
   
def image_processing():
    choice=0
   
    while(choice!=7):
        print("Menu:")
        print("1.Display Image")
        print("2.Change Brightness ")
        print("3.Difference between two images")
        print("4.Negative Image")
        print("5.Histogram")
        print("6.Threshold")
        print("7.Exit")
        choice=int(input("Enter your choice: "))
        if(choice==1):
            display()
        elif(choice==2):
            brightness()
        elif(choice==3):
            diffence()
        elif(choice==4):
            negative()
        elif(choice==5):
            histogram()
        elif(choice==6):
            threshold()
        elif(choice==7):
            print("Terminating..")
        else:
            print("\nInvalid choice")
       
image_processing()
