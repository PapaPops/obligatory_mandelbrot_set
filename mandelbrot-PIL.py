from PIL import Image
from sys import exit
from math import floor

height = 1000
width = 1000
z = [0,0]
maxiterations = 100
treshold = 20

def isMandelbrot(c):

    """z = z*z + c
        where z starts as 0"""
    """z*z = a*a - b*b + 2ab"""
    realz = z[0]
    imaginaryz = z[1]
    real = c[0]
    imaginary = c[1]
    for i in range(maxiterations):
        previous_realz = realz
        previous_imaginaryz = imaginaryz
        realz = (previous_realz ** 2 - previous_imaginaryz ** 2) + real
        imaginaryz = (2 * previous_imaginaryz * previous_realz) + imaginary
        if abs(realz + imaginaryz) > treshold:
            return i


        
    
    return maxiterations
        

    


def mapto(x,mina,maxa,minb,maxb):

    x -= mina


    intervalA = maxa-mina
    intervalB = maxb-minb

    x /= intervalA
    x *= intervalB
    x += minb
    ## - minb
    return x
    

def main():
    mandelbrot =  Image.new("RGB",(width,height))

    arr = []

    for i in range(height):
        print(mapto(i,0,height,-2,2))
        for j in range(width):
            c = (mapto(j,0,width,-2,2), mapto(i,0,height,-2,2))
            result = floor(mapto(isMandelbrot(c),0,maxiterations,0,255))
            arr.append((result,result,result))

    mandelbrot.putdata(arr)
    mandelbrot.show()
    mandelbrot.save("mandelbrot.png")




if __name__ == "__main__":
    main()
else:
    print("file must be ran as main")
    exit(0)