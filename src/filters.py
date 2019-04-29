""" SYSC 1005 A Fall 2017.

Filters for a photo-editing application.
"""

from Cimpl import *

def grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def solarize(image, threshold):
    """ (Cimpl.Image, int) -> None
    
    Solarize image.
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image, 128)
    >>> show(image)     
    """
    for x, y, (red, green, blue) in image:

        # Invert the values of all RGB components that are less than threshold,
        # leaving components with higher values unchanged.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        solarized = create_color(red, green, blue)
        set_color(image, x, y, solarized)


def black_and_white(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3      
        
        if brightness < 128:
            set_color(image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(image, x, y, white)


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white-and-gray (three-tone) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:      
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)
            
def weighted_grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> weighted_grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color. but weighted based off of how the human eye perceives
        # color
        
        brightness = (r * 0.299) + (g * 0.587) + (b * 0.114)
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)

def negative(image):
    """ (Cimpl.Image) -> None
    
    Convert image into negative image.
    
    >>> image = load_image(choose_file())
    >>> negative(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        
        # Calculate the negative value of r, g, b and create new color 
        # with those values. 
        new_color = create_color(255 - r, 255 - g, 255 - b)
        set_color(image, x, y, new_color)
        
def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    
    Modify image, maximizing the contrast between the light and dark pixels.
    
    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    show(image)
    """
    for x, y, (r, g, b) in image:
        if r < 128:
            r = 0
        else:
            r = 255
        if g < 128:
            g = 0
        else:
            g = 255    
        if b < 128:
            b = 0
        else:
            b = 255
        new_color = create_color(r, g, b)
        set_color(image, x, y, new_color)
        
def sepia_tint(image):
    """ (Cimpl.Image) -> None
    
    Convert image to sepia tones.
    
    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """
    grayscale(image)
    for x, y, (r, g, b) in image:
        if r < 63:
            b *= 0.9
            r *= 1.1
        elif g < 192:
            b *= 0.85
            r *= 1.15
        else:
            b *= 0.93
            r *= 1.08
        new_color = create_color(r, g, b)
        set_color(image, x, y, new_color)
            
def _adjust_component(amount):
    """ (int) -> int
    
    Divide the range 0..255 into 4 equal-size quadrants, and return the midpoint of the quadrant in which the specified amount lies.
    
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    if amount < 64:
        return 31
    elif amount < 128:
        return 95
    elif amount < 192:
        return 159
    else:
        return 223
    
def posterize(img):
    """ (Cimpl.Image) -> None
    
    "Posterize" the specified image.
    
    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        
        new_color = create_color(r, g, b,)
        set_color(image, x, y, new_color)
        
def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(source)):
    #     for x in range(0, get_width(source)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)
            top_left_red, top_left_green, top_left_blue = get_color(source, x-1, y-1)
            top_right_red, top_right_green, top_right_blue = get_color(source, x+1, y-1)
            bottom_left_red, bottom_left_green, bottom_left_blue = get_color(source, x-1, y+1)
            bottom_right_red, bottom_right_green, bottom_right_blue = get_color(source, x+1, y+1)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + top_left_red + top_right_red + bottom_left_red + bottom_right_red) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green  + top_left_green + top_right_green + bottom_left_green + bottom_right_green) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue  + top_left_blue + top_right_blue + bottom_right_blue + bottom_right_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target

def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> None
    
    Modify image using edge detection.
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image, 10.0)
    >>> show(image)
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            r, g, b = get_color(image, x, y)
            curr_average = (r + g + b) / 3
            r1, g1, b1 = get_color(image, x, y+1)
            below_average = (r1 + g1 + b1) / 3
            if abs(curr_average - below_average) > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)
def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> None
    
    Modify image using edge detection.
    
    >>> image = load_image(choose_file())
    >>> detect_edges_better(image, 10.0)
    >>> show(image)
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            r, g, b = get_color(image, x, y)
            curr_average = (r + g + b) / 3
            r1, g1, b1 = get_color(image, x, y+1)
            below_average = (r1 + g1 + b1) / 3
            r2, g2, b2 = get_color(image, x+1, y)
            right_average = (r2 + g2 + b2) / 3
            if abs(curr_average - below_average) > threshold or abs(curr_average - right_average) > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)
                
def flip_vertical(image):
    """ (Cimpl.Image) -> None
    
    Flip image around an imaginary vertical line drawn through its midpoint.
    
    >>> image = load_image(choose_file())
    >>> flip_vertical(image)
    >>> show(image)
    """
    target = copy(image)
    for y in range(0, get_height(image)):
        for x in range(0, get_width(image)):
                set_color(target, get_width(image) - 1 - x, y, get_color(image, x, y))
    return target
                
def flip_horizontal(image):
    """ (Cimpl.Image) -> None
    
    Flip image around an imaginary vertical line drawn through its midpoint.
    
    >>> image = load_image(choose_file())
    >>> flip_horizontal(image)
    >>> show(image)
    """
    target = copy(image)
    for x in range(0, get_width(image)):
        for y in range(0, get_height(image)):
                set_color(target, x, get_height(image) - 1 - y, get_color(image, x, y))
    return target