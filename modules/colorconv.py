def hextorgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def rgbtohex(rgb: tuple):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])