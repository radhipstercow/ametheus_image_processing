import paint
import process


# Runs entire program
def main(name, new_image):
    if (new_image):
        process.importImage(name, new_image)
    paint.create(name)


# (image name, is new image?)
main("gecko", False)
