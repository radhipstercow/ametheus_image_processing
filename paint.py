import numpy as np
from PIL import Image
import constants
import pickle


# Create rand int
def getRandInt(min, max):
    integer = np.random.randint(min, max)
    return integer


# Create random color
def getRandColor():
    min = 40
    max = 216
    return [getRandInt(min, max), getRandInt(min, max), getRandInt(min, max)]


# Random Pastel Color
def getRandPastel():
    min = 150
    max = 256
    return [getRandInt(min, max), getRandInt(min, max), getRandInt(min, max)]


# Fill Background Color for the Canvas
def fillBackground(arr):
    cols = len(arr[1])
    rows = len(arr)
    rand_background = getRandColor()
    pastel_background = getRandPastel()

    if (constants.bkg_type == 1):
        bkg_fill = pastel_background
    else:
        bkg_fill = rand_background

    for i in range(cols):
        for j in range(rows):
            arr[j, i] = bkg_fill
    return arr


# Add base asset to the canvas
def createBaseAsset(canvas, base_asset):
    base_color = getRandColor()
    light_color = createTint(base_color)
    dark_color = createShade(base_color)

    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            if (base_asset[i, j] != 0):
                if (base_asset[i, j] == 1):
                    canvas[i, j] = light_color
                if (base_asset[i, j] == 2):
                    canvas[i, j] = base_color
                if (base_asset[i, j] == 3):
                    canvas[i, j] = dark_color
    return canvas


# Add static asset to canvas
def createStaticAsset(canvas, static_asset):
    base_color = getRandColor()
    light_color = createTint(base_color)
    print(static_asset)
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            if (static_asset[i, j] != 0):
                if (static_asset[i, j] == 11):
                    canvas[i, j] = base_color
                elif (static_asset[i, j] == 12):
                    canvas[i, j] = light_color
                elif (static_asset[i, j] == 13):
                    canvas[i, j] = [255, 255, 255]
                elif (static_asset[i, j] == 14):
                    canvas[i, j] = [0, 0, 0]
    return canvas


# Create color tint from random base
def createTint(color):
    return [color[0]+constants.color_variant, color[1]+constants.color_variant, color[2]+constants.color_variant]


# Generate color shade from random base
def createShade(color):
    return [color[0]-constants.color_variant, color[1]-constants.color_variant, color[2]-constants.color_variant]


# Gets the base asset from pickle storage
def getBaseAsset(asset_name):
    asset = pickle.load(open("data/" + asset_name + "/base_asset.bin", "rb"))
    return asset


# Gets static asset from pickle storage
def getStaticAsset(asset_name):
    asset = pickle.load(open("data/" + asset_name + "/static_asset.bin", "rb"))
    return asset


# Randomly select asset type (NOT IMPLEMENTED)
def getAssetType():
    labels = pickle.load(open("data/labels.bin", "rb"))
    print(labels)


# Main function of program
def create(assetName):
    print_number = 1
    while print_number <= constants.print_total:
        # Create and fill empty array
        canvas = np.empty((constants.canvas_height, constants.canvas_width,
                           constants.color_values), dtype=np.uint8)
        canvas = fillBackground(canvas)

        # Select asset to create
        # assetName = 'dragon2'

        # Add base asset to canvas
        canvas = createBaseAsset(canvas, getBaseAsset(assetName))

        # Add eye
        canvas = createStaticAsset(canvas, getStaticAsset(assetName))

        # Create a PIL image from the NumPy array
        PIXEL_ART = Image.fromarray(canvas)
        PIXEL_ART = PIXEL_ART.resize((256, 256), Image.NEAREST)

        # Save the image
        file_name = 'export/PIXEL_ART_' + str(print_number) + '.png'
        PIXEL_ART.save(file_name)
        print_number += 1
