import paint
import process


# Runs entire program
def main(name, new_image):
    if (new_image):
        process.importImage(name)
    paint.create(name)


main("dragon", False)
