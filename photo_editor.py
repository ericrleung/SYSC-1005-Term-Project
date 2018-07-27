# SYSC 1005 A Fall 2017 Lab 7

import sys  # get_image calls exit
from Cimpl import *
import filters

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

def show_menu():
    return "L)oad image\nN)egative G)rayscale X)treme contrast S)epia tint E)dge detect\nQ)uit ?"

# A bit of code to demonstrate how to use get_image().

if __name__ == "__main__":
    
    image_loaded = False
    
    print(show_menu())
    while True:
        user_input = input(": ")
        if user_input == "L":
            img = get_image()
            show(img)
            image_loaded = True
        elif user_input == "N":
            if not image_loaded:
                print("No image loaded")
                continue
            filters.negative(img)
            show(img)
        elif user_input == "G":
            if not image_loaded:
                print("No image loaded")
                continue           
            filters.weighted_grayscale(img)
            show(img)
        elif user_input == "X":
            if not image_loaded:
                print("No image loaded")
                continue         
            filters.extreme_contrast(img)
            show(img)
        elif user_input == "S":
            if not image_loaded:
                print("No image loaded")
                continue        
            filters.sepia_tint(img)
            show(img)
        elif user_input == "E":
            if not image_loaded:
                print("No image loaded")
                continue        
            threshold = float(input("Threshold? : "))
            filters.detect_edges_better(img, threshold)
            show(img)
        elif user_input == "Q":
            break
        elif not user_input in ["L", "Q", "N", "G", "X", "S", "E"]:
            print("No such command")
            continue
        else:
            pass
        
