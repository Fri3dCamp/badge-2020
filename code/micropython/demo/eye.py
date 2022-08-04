import st7789
from fri3d import display
import random
import time

def draw_eye(x, y, radius=100, pupil=0.4, color=st7789.BLUE):
    center_x = 120 - x
    center_y = 120 - y
    iris = int (radius * 0.6)

    offset_factor = 1.5

    iris_factor_x = int(x * offset_factor)
    iris_factor_y = int(y * offset_factor)

    pupil_factor_x = int(iris_factor_x * offset_factor)
    pupil_factor_y = int(iris_factor_y * offset_factor)

    display.fill(st7789.BLACK)
    display.fill_circle(center_x, center_y, radius, st7789.WHITE)
    display.fill_circle(int(120 - iris_factor_x), int(120 - iris_factor_y), iris, color)
    display.fill_circle(int(120 - pupil_factor_x), int(120 - pupil_factor_y), int(iris * pupil), st7789.BLACK)

def run():
    while (True):
        x = random.randint(-30, 30)
        y = random.randint(-30, 30)
        draw_eye(x, y)

        time.sleep_ms(random.randint(1000, 4000))
