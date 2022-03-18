# This line imports or includes the library we will need
from PIL import Image

# # # This line opens the image and loads it into a variable called "image_background"
# # image_background = Image.open("python/CSE 110/assets/cse110_images/sunset.jpg")

# # # This line attempts to open a new window to display the image.
# # image_background.show()


# # width, height = image_background.size
# # pixels_original = image_background.load()
# # r, g, b = pixels_original[100, 200]
# # Don't forget to use parentheses around your (r, g, b)
# # pixels_original[100, 200] = (r, g, b)

# # image_background.save("the_file_goes_here.jpg")


# # # Create a new image in RGB format that is the same size as image_background
# # image_new = Image.new("RGB", image_background.size)
# # pixels_new = image_new.load()


# # pixels_new[x, y] = (r, g, b)

# # image_new.show()

# # image_new.save("the_new_image.jpg")

# def load_image():
#     # This line opens the image and loads it into a variable called "image_background"
#     image_background = Image.open("python/CSE 110/assets/cse110_images/sunset.jpg")
#     image_forground = Image.open("python/CSE 110/assets/cse110_images/spaceshuttle.jpg")
#     # This line attempts to open a new window to display the image.
#     image_background.show()
#     create_new_img(image_background)

# def create_new_img(image_background):
#     width, height = image_background.size
#     pixels_original = image_background.load()
#     r, g, b = pixels_original[100, 200]
#     # Don't forget to use parentheses around your (r, g, b)
#     pixels_original[100, 200] = (r, g, b)

#     image_background.save("the_file_goes_here.jpg")


#     # Create a new image in RGB format that is the same size as image_background
#     image_new = Image.new("RGB", image_background.size)
#     pixels_new = image_new.load()
#     iterating_through_the_pixels(width, height)
# # PRODUCING AND SAVING A NEW IMAGE
# #     pixels_new[x, y] = (r, g, b)

# #     image_new.show()

# #     image_new.save("the_new_image.jpg")
# #ITERATING THROUGH THE PIXELS
# def iterating_through_the_pixels(width, height):
#     for x in range(0,width):
#         for y in range(0,height):
            
    














def main():
    
    image_background = Image.open("python/CSE 110/assets/cse110_images/sunset.jpg")
    image_forground = Image.open("python/CSE 110/assets/cse110_images/spaceshuttle.jpg")
    
    pixels_new = image_new.load()
    image_background.show()
    width, height = image_background.size
    pixels_original = image_background.load()
    r, g, b = pixels_original[100, 200]
   
    pixels_original[100, 200] = (r, g, b)
    pixels_forgound 

    image_background.save("the_file_goes_here.jpg")


    
    for x in range(0,width):
        for y in range(0,height):
            (r, g, b) = pixels_original


    

main()