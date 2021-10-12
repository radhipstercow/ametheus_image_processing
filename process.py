import numpy as np
import os
from PIL import Image
import constants
import pickle


def formatBaseAsset(arr):
    tint_color = arr[0, 0]
    base_color = arr[0, 1]
    shade_color = arr[0, 2]
    formattedArr = np.zeros(
        (constants.canvas_width, constants.canvas_height), dtype=np.uint8)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            tint_comp = arr[i, j] == tint_color
            base_comp = arr[i, j] == base_color
            shade_comp = arr[i, j] == shade_color
            if (tint_comp.all()):
                formattedArr[i, j] = 1
            elif (base_comp.all()):
                formattedArr[i, j] = 2
            elif (shade_comp.all()):
                formattedArr[i, j] = 3
            else:
                formattedArr[i, j] = 0
    formattedArr[0, 0] = 0
    formattedArr[0, 1] = 0
    formattedArr[0, 2] = 0
    return formattedArr


def formatStaticAsset(arr):
    # Comparators
    aComp = [0, 0, 0] == arr[0, 0]
    bComp = [0, 0, 0] == arr[0, 1]
    cComp = [0, 0, 0] == arr[0, 2]
    dComp = [0, 0, 0] == arr[0, 3]
    # NEED TO FIX
    if (not aComp.all()):
        tint_color = arr[0, 0]
    else:
        tint_color = [-1, -1, -1]
    if (not bComp.all()):
        base_color = arr[0, 1]
    else:
        base_color = [-1, -1, -1]
    if (not cComp.all()):
        white = arr[0, 2]
    else:
        white = [-1, -1, -1]
    if (not dComp.all()):
        black = arr[0, 3]
    else:
        black = [-1, -1, -1]
    print(tint_color)
    formattedArr = np.zeros(
        (constants.canvas_width, constants.canvas_height), dtype=np.uint8)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            tint_comp = arr[i, j] == tint_color
            base_comp = arr[i, j] == base_color
            white_comp = arr[i, j] == white
            black_comp = arr[i, j] == black

            if (tint_comp.all()):
                formattedArr[i, j] = 11
            elif (base_comp.all()):
                formattedArr[i, j] = 12
            elif (white_comp.all()):
                formattedArr[i, j] = 13
            elif (black_comp.all()):
                formattedArr[i, j] = 14
            else:
                formattedArr[i, j] = 0

    formattedArr[0, 0] = 0
    formattedArr[0, 1] = 0
    formattedArr[0, 2] = 0
    formattedArr[0, 3] = 0
    return formattedArr


def importImage(image_name, new_image):
    image_labels = []

    # Create directory for array storage
    script_path = "C:\\Users\\byron\\Documents\\Docs\\Programming\\L-Python\\algo-art\data\\" + image_name
    if not os.path.exists(script_path):
        os.mkdir(script_path)

    # Import base asset of the image
    base_asset = Image.open('images/' + image_name + '/base_asset.png')
    base_asset = np.asarray(base_asset)
    base_asset = base_asset[:constants.canvas_height]
    base_asset = np.delete(base_asset, 3, axis=2)       # Remove rgba to rgb
    base_asset = formatBaseAsset(base_asset)
    pickle.dump(base_asset, open(
        'data/' + image_name + '/base_asset.bin', "wb"))

    # Import static asset of the image
    static_asset = Image.open('images/' + image_name + '/static_asset.png')
    static_asset = np.asarray(static_asset)
    static_asset = static_asset[:constants.canvas_height]
    static_asset = np.delete(static_asset, 3, axis=2)
    static_asset = formatStaticAsset(static_asset)
    pickle.dump(static_asset, open(
        'data/' + image_name + '/static_asset.bin', "wb"))

    # Add names to list of stored data
    if not new_image:
        labels = pickle.load(open("data/labels.bin", "rb"))
        for item in labels:
            image_labels.append(item)
        image_labels.append(image_name)
    else:
        image_labels.append(image_name)
    pickle.dump(np.unique(image_labels), open('data/labels.bin', "wb"))

    """
    # Testing file input
    PIXEL_ART = Image.fromarray(base_asset)
    PIXEL_ART = PIXEL_ART.resize((256, 256), Image.NEAREST)

    # Save the image
    file_name = 'PIXEL_ART_TEST.png'
    PIXEL_ART.save(file_name)
    """
