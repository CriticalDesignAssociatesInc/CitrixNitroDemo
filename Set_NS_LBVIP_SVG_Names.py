import random
import string
import time

def set_random_svg(length):
    svg_characters = string.digits
    svg_name = ''.join(random.choice(svg_characters) for p in range(length))
    svg_name = 'svg-' + svg_name
    #print(time.time())
    print(svg_name)
    return svg_name

set_random_svg(5)

def set_random_lbvip(length):
    lbvip_characters = string.digits
    lbvip_name = ''.join(random.choice(lbvip_characters) for p in range(length))
    lbvip_name = 'lbvip-' + lbvip_name
    print(lbvip_name)
    return lbvip_name

set_random_lbvip(5)
