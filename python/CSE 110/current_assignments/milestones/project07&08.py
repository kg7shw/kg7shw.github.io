from PIL import Image


image_background = Image.open("python/CSE 110/assets/cse110_images/sunset.jpg")
image_overlay = Image.open("python/CSE 110/assets/cse110_images/spaceshuttle.jpg")

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

image_new.save("the_new_image.jpg")




