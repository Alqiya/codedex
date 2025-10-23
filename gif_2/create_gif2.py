import imageio.v3 as iio

imgnames=['1.png','2.png','3.png']
images=[]

for name in imgnames:
    images.append(iio.imread(name))

iio.imwrite('nyan-cat.gif', images, duration=500, loop=0)