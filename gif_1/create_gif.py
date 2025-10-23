import imageio.v3 as iio

filenames=['img1.PNG','img2.PNG']
images=[]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('mickeymouse.gif', images, duration=500, loop=0)


