import st7789
from fri3d import BADGE
import uasyncio as asyncio
import random

BLACK = st7789.BLACK
BLUE = st7789.BLUE
RED = st7789.RED
GREEN = st7789.GREEN
CYAN = st7789.CYAN
MAGENTA = st7789.MAGENTA
YELLOW = st7789.YELLOW
WHITE = st7789.WHITE


class Eye:
    def __init__(self):
        self.x = 120
        self.y = 120
        self.radius = 100
        self.pupil = 0.5
        self.color = GREEN

        self._task = None

    def render(self):
        # -- overwrite the current eye location
        # BADGE.display().fill_circle(self.x, self.y, self.radius, BLACK)

        center_x = 120 - self.x
        center_y = 120 - self.y
        iris = int (self.radius * 0.6)

        offset_factor = 1.5

        iris_factor_x = int(self.x * offset_factor)
        iris_factor_y = int(self.y * offset_factor)

        pupil_factor_x = int(iris_factor_x * offset_factor)
        pupil_factor_y = int(iris_factor_y * offset_factor)

        BADGE.display().fill(BLACK)
        BADGE.display().fill_circle(center_x, center_y, self.radius, WHITE)
        BADGE.display().fill_circle(int(120 - iris_factor_x), int(120 - iris_factor_y), iris, self.color)
        BADGE.display().fill_circle(int(120 - pupil_factor_x), int(120 - pupil_factor_y), int(iris * self.pupil), BLACK)

    def auto(self, enable=True):
        if enable:
            self.task = asyncio.create_task(self._run())
        elif self.task:
            self.task.cancel()

    async def _run(self):
        while True:
            self.x = random.randint(-20, 20)
            self.y = random.randint(-20, 20)
            # self.pupil = random.randint(30, 50) / 100
            self.render()

            await asyncio.sleep_ms(random.randint(3000, 10000))