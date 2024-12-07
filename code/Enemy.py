#!/usr/bin/python
# -*- coding: utf-8 -*-


from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Enemy):
            def __init__(self, name: str, position: tuple):
                super().__init__(name, position)
                self.vertical_velocity = 1
                self.direction = -1

            def move(self):

                self.rect.centerx -= ENTITY_SPEED[self.name]


                self.rect.centery += self.vertical_velocity * self.direction


                if self.rect.top <= 0:
                    self.direction = 1
                    self.vertical_velocity *= 2
                elif self.rect.bottom >= WIN_HEIGHT:
                    self.direction = -1
                    self.vertical_velocity = 1

                self.rect.centery = max(0, min(WIN_HEIGHT, self.rect.centery))

def shoot(self):
           self.shot_delay -= 1
           if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
