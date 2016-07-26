from PIL import Image

darkBlue = (0, 51, 76) # dark: < 182
red = (217, 26, 33) # medium dark > 182, < 364
lightBlue = (112, 150, 158) #medium light: > 364, < 546
yellow = (252, 227, 166) # light > 546

lemon = (236, 232, 26)
aquamarine = (110, 206, 178)
navy = (1, 66, 106)
pink = (244, 54, 76)

im = Image.open("4_image.jpg")
width, height = im.size
print("Width: {} \nHeight: {}".format(width, height))

data = im.getdata() #Returns PIL sequence object containing pixel values.
data_list = list(data) 
print("Data length: {}".format(len(data_list)))

def colorize(image_data):
    new_pic = []

    for pixel in image_data:
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        total = red + green + blue
        if total < 182:
            new_pic.append(navy)
        elif total < 364:
            new_pic.append(pink)
        elif total < 546:
            new_pic.append(aquamarine)
        else:
            new_pic.append(lemon)
    return new_pic

data_colorized = colorize(data_list)
print("Colorized data length: {}".format(len(data_colorized)))

new_image = Image.new(im.mode, im.size) #make them read the documentation group activity to understand that documentation literacy
new_image.putdata(data_colorized)
new_image.show()
new_image.save("output", "jpeg")
