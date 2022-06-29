import PIL.ImageGrab

PPI = 100.7
CONTROL_LOCATION = (1 * PPI, 8 * PPI)
SHARE_LOCATION = (1.5 * PPI, 5.75 * PPI)
HOME_LOCATION = (0.5 * PPI, 0.75 * PPI)
UPLOAD_LOCATION = (6 * PPI, 0.75 * PPI)
YELLOW_LOCATION = (10 * PPI, 4.5 * PPI)
GREY_BACK_LOCATION = (3 * PPI, 2.5 * PPI)

def write_color(location):
    with open('colors.txt', 'w+') as f:
        f.write(PIL.ImageGrab.grab().load()[location])

for loc in [SHARE_LOCATION, YELLOW_LOCATION, GREY_BACK_LOCATION]:
    write_color(loc)

