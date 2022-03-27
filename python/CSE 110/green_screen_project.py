
from PIL import Image

background_image_is_in_list = False
overlay_image_is_in_list = False

while background_image_is_in_list == False and overlay_image_is_in_list == False:

    image_background = input("Please pick one of these images to be the background: beach, snowscape, sunset, earth, field, forest, or desert: ")
    
    image_overlay = input("Please pick one of these images to overlay the background: boat, cactus, cat_small, cat, harvester, hiker, penguin, spaceshuttle: ")


    image_background_list = ["beach", "snowscape", "sunset", "earth", "field", "forest", "desert"]
    image_overlay_list = ["boat", "cactus", "cat_small", "cat", "harvester", "hiker", "penguin", "spaceshuttle"]

    

    for image in image_background_list:
        if image == image_background:
            background_image_is_in_list = True

    

    for image in image_overlay_list:
        if image == image_overlay:
            overlay_image_is_in_list = True


    if background_image_is_in_list == True and overlay_image_is_in_list == True:
        background_image_file_name = "assets" + "\\" + image_background + ".jpg"
        overlay_image_file_name = "assets" + "\\" + image_overlay + ".jpg"
    else:
        print("incorrect input. Please input again.")
        background_image_is_in_list = False
        overlay_image_is_in_list = False




new_image_background = image_background
new_image_overlay = image_overlay

image_background = Image.open(background_image_file_name)
image_overlay = Image.open(overlay_image_file_name)

width, height = image_background.size

image_new = Image.new("RGB", image_background.size)


pixels_background = image_background.load()
r, g, b = pixels_background[100, 200]
pixels_background[100, 200] = (r, g, b)

image_background.save("the_file_goes_here.jpg")

pixels_background = image_background.load()
pixels_overlay = image_overlay.load()
pixels_new = image_new.load()


for i in range(0, width):
        for j in range(0, height):
            (r, g, b) = pixels_overlay[i, j]
            if (r <=70 and g >= 170 and b <=90):
                (r, g, b) = pixels_background[i ,j]
            pixels_new[i, j] = (r, g, b)


image_new.show()



image_new.save("new_assets" + "\\" + new_image_background + "_" + new_image_overlay + ".jpg")
