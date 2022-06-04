import pygame.time
from simpleasbreath.configs.fonts import font1
from simpleasbreath.configs.screens import screen


class Timer:
    def __init__(self):
        self.total_ticks = 0
        self.clock_time_ticks = 0
        self.clock_time_seconds = 0
        self.clock_time_minutes = 0
        self.time_ticks = 0
        self.time_seconds = 0
        self.time_minutes = 0
        self.time_getted = [0,0,0]
        self.show_timer = 0
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def get_time(self):
        self.time_getted = [self.clock_time_ticks, self.clock_time_seconds, self.clock_time_minutes]
        return [self.clock_time_ticks, self.clock_time_seconds, self.clock_time_minutes]

    def get_total_seconds(self):
        return  self.total_ticks/self.FPS

    def get_total_minutes(self):
        return self.total_ticks/self.FPS/60

    def total_seconds_passed(self):
        seconds = self.total_ticks_passed()/60
        return seconds

    def total_ticks_passed(self):
        ticks = self.get_time()[2]*self.FPS*self.FPS + self.get_time()[1]*self.FPS + self.get_time()[0]
        return ticks

    def reset(self):
        self.clock_time_ticks = 0
        self.clock_time_seconds = 0
        self.clock_time_minutes = 0
        self.time_getted = [0,0,0]

    def timer(self):
        self.total_ticks += 1
        self.clock_time_ticks += 1
        if self.clock_time_ticks == self.FPS:
            self.clock_time_ticks = 0
            self.clock_time_seconds += 1
        if self.clock_time_seconds == 60:
            self.clock_time_seconds = 0
            self.clock_time_minutes += 1

        if self.show_timer == 1 or self.show_timer == 2:
            time = font1.config.render(f"{self.clock_time_minutes:0>2}:{self.clock_time_seconds:0>2}:{self.clock_time_ticks:0>2}", True,
                                       (255, 255, 255))

            screen.blit(time, (890, 10))

        if self.show_timer == 2:
            time2 = font1.config.render(f"{self.time_getted[2]:0>2}:{self.time_getted[1]:0>2}:{self.time_getted[0]:0>2}",
                                        True, (105, 85, 115))
            screen.blit(time2, (10, 10))


timer = Timer()