def rgb_hex():
    invalid_msg = "invalid values being entered"
    red = int(input('please enter Red value: '))
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input('please enter Green value: '))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input('please enter Blue value: '))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return
    val = (red << 16) + (green << 8) + blue
    print("%s" % (hex(val)[2:]).upper())

def hex_rgb():
    hex_val = input('Enter the color(six hexadecimal digits): ')
    if len(hex_val) != 6:
        print('invalid value being entered')
        return
    else:
        hex_val = int(hex_val,16)
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print("Red: %s Green: %s Blue: %s") % (red,green,blue)

def convert():
    while True:
        option = input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ')
        if option == '1':
            print('RGB to HEX...')
            rgb_hex()
        elif option == '2':
            print('HEX to RGB...')
            hex_rgb()
        elif option == 'X' or option == 'x':
            break
        else:
            print('wrong value entered')
            return

convert()
