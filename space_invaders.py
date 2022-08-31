import pygame
import sys
from pygame.locals import *
import os
import random

pygame.font.init()

width, height = 700, 700
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# GLOBAL VARIABLES
FPS = 60
VEL = 5
ALIEN_VEL = 7
SET = True
PUR_SET = True

# color values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BULLET_VEL = 10
MAX_BULLETS = 1
ALIEN_HIT = pygame.USEREVENT + 1
EARTH_HIT = pygame.USEREVENT + 2
WINNER_FONT = pygame.font.SysFont('Arial', 100)

# hits
LOW_HITS = 20
MEDIUM_HITS = 30
HIGH_HITS = 40

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 80
EARTHSHIP_WIDTH, EARTHSHIP_HEIGHT = 40, 60
BLOCKADE_WIDTH, BLOCKADE_HEIGHT = 170, 55

EARTH_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('static', 'earth rocket.png')
)

EARTH_SPACESHIP = pygame.transform.scale(EARTH_SPACESHIP_IMAGE,
                                         (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BLUE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('static', 'blue alien ship.png')
)

BLUE_SPACESHIP = pygame.transform.scale(BLUE_SPACESHIP_IMAGE,
                                        (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('static', 'yellow alien ship.png')
)

YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
                                          (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

DANGER_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('static', 'danger alien ship.png')
)

DANGER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(DANGER_SPACESHIP_IMAGE,
                                                                  (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)
PURPLE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('static', 'purple alien ship.png')
)

PURPLE_SPACESHIP = pygame.transform.scale(PURPLE_SPACESHIP_IMAGE,
                                          (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('static', 'space.png')
), (width, height))


def window(earth_ship, purple_alien_ship, blue_ships,
           yellow_ships, danger_ships, earth_bullets, alien_bullets, alien_ships,
           big_ship, big_ship_bullets, blockades, hits):

    WIN.blit(SPACE_BACKGROUND, (0, 0))
    WIN.blit(EARTH_SPACESHIP, (earth_ship.x, earth_ship.y))

    global PUR_SET
    if purple_alien_ship.x >= -99 and PUR_SET:
        purple_alien_ship.x += ALIEN_VEL
    if purple_alien_ship.x > 700:
        PUR_SET = False
        purple_alien_ship.x -= 750
    PUR_SET = True

    # drawing alien ships
    for ship in alien_ships:
        if ship in alien_ships and ship in blue_ships:
            WIN.blit(BLUE_SPACESHIP, (ship.x, ship.y))
        elif ship in alien_ships and ship in yellow_ships:
            WIN.blit(YELLOW_SPACESHIP, (ship.x, ship.y))
        elif ship in alien_ships and ship in danger_ships:
            WIN.blit(DANGER_SPACESHIP, (ship.x, ship.y))

    # drawing big alien ship
    for ship in big_ship:
        if ship in big_ship:
            WIN.blit(PURPLE_SPACESHIP, (purple_alien_ship.x, purple_alien_ship.y))

    global SET
    # CONTROL FOR TO AND FRO MOVEMENT OF ALIEN SHIPS... not perfect yet
    if blue_ships[0].x >= 0 and SET:
        blue_ships[0].x += ALIEN_VEL
        blue_ships[1].x += ALIEN_VEL
        blue_ships[2].x += ALIEN_VEL
        blue_ships[3].x += ALIEN_VEL

        yellow_ships[0].x += ALIEN_VEL
        yellow_ships[1].x += ALIEN_VEL
        yellow_ships[2].x += ALIEN_VEL
        yellow_ships[3].x += ALIEN_VEL

        danger_ships[0].x += ALIEN_VEL
        danger_ships[1].x += ALIEN_VEL
        danger_ships[2].x += ALIEN_VEL
        danger_ships[3].x += ALIEN_VEL

    if not SET or blue_ships[3].x > 650:
        SET = False
        if blue_ships[3].x > 300:
            blue_ships[0].x -= ALIEN_VEL
            blue_ships[1].x -= ALIEN_VEL
            blue_ships[2].x -= ALIEN_VEL
            blue_ships[3].x -= ALIEN_VEL

            yellow_ships[0].x -= ALIEN_VEL
            yellow_ships[1].x -= ALIEN_VEL
            yellow_ships[2].x -= ALIEN_VEL
            yellow_ships[3].x -= ALIEN_VEL

            danger_ships[0].x -= ALIEN_VEL
            danger_ships[1].x -= ALIEN_VEL
            danger_ships[2].x -= ALIEN_VEL
            danger_ships[3].x -= ALIEN_VEL

            if blue_ships[3].x <= 300:
                SET = True

    # CONTROL FOR BARRICADES' COLOR CHANGES
    try:
        if hits[0] > HIGH_HITS:
            blockades.remove(blockades[0])
        if MEDIUM_HITS < hits[0] <= HIGH_HITS:
            pygame.draw.rect(WIN, RED, blockades[0])
        if LOW_HITS < hits[0] <= MEDIUM_HITS:
            pygame.draw.rect(WIN, YELLOW, blockades[0])
        if hits[0] <= LOW_HITS:
            pygame.draw.rect(WIN, GREEN, blockades[0])
    except IndexError:
        pass

    try:
        if hits[1] > HIGH_HITS:
            blockades.remove(blockades[1])
        if MEDIUM_HITS < hits[1] <= HIGH_HITS:
            pygame.draw.rect(WIN, RED, blockades[1])
        if LOW_HITS < hits[1] <= MEDIUM_HITS:
            pygame.draw.rect(WIN, YELLOW, blockades[1])
        if hits[1] <= LOW_HITS:
            pygame.draw.rect(WIN, GREEN, blockades[1])
    except IndexError:
        pass

    try:
        if hits[2] > HIGH_HITS:
            blockades.remove(blockades[2])
        if MEDIUM_HITS < hits[2] <= HIGH_HITS:
            pygame.draw.rect(WIN, RED, blockades[2])
        if LOW_HITS < hits[2] <= MEDIUM_HITS:
            pygame.draw.rect(WIN, YELLOW, blockades[2])
        if hits[2] <= LOW_HITS:
            pygame.draw.rect(WIN, GREEN, blockades[2])
    except IndexError:
        pass

    for bullet in earth_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)

    for bullet in big_ship_bullets:
        if len(big_ship) > 0:
            pygame.draw.rect(WIN, YELLOW, bullet)
        else:
            big_ship_bullets.remove(bullet)

    pygame.display.update()


def draw_winner(text):
    """
    writes text in screen depending on if you win or loose
    :param text:
    :return:
    """
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(draw_text, (width//2 - draw_text.get_width() / 2, height//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def earth_ship_movements(keys_pressed, earth_ship):
    """
    controls earth's rocket movements
    :param keys_pressed: list of keys pressed by user
    :param earth_ship: earth's rocket
    :return:
    """
    if keys_pressed[pygame.K_LEFT] and earth_ship.x >= 0:
        earth_ship.x -= VEL
    elif keys_pressed[pygame.K_RIGHT] and earth_ship.x <= 650:
        earth_ship.x += VEL


def bullets_handler(earth_bullets, earth_ship, alien_bullets,
                    alien_ships, big_ship, big_ship_bullets, blockade, hits):
    """

    :param earth_bullets: list of bullets of earth's rocket
    :param earth_ship: earth;s rocket
    :param alien_bullets: list of bullets of all alien ships
    :param alien_ships: list of all alien ships excluding the big alien ship
    :param big_ship: list with one element, The big alien ship
    :param big_ship_bullets: list of bullets of big alien ship
    :param blockade: list of blockades (i.e 3)
    :param hits: list of number of times each blockade has been hit.
    this is to be used to track the blockade color change
    :return:
    """
    # checks if earth's bullets collide with a big ship
    for ship in big_ship:
        for bullet in earth_bullets:
            if bullet.colliderect(ship):
                pygame.event.post(pygame.event.Event(ALIEN_HIT))
                big_ship.remove(ship)
                earth_bullets.remove(bullet)
                big_ship_bullets = []
    for bullet in earth_bullets:
        bullet.y -= BULLET_VEL

        # checks if earth's bullets collide with a blockade
        for block in blockade:
            if block.colliderect(bullet):
                earth_bullets.remove(bullet)

        # checks if earth's bullets collide with an alien ship
        for ship in alien_ships:
            if bullet.colliderect(ship):
                pygame.event.post(pygame.event.Event(ALIEN_HIT))
                alien_ships.remove(ship)
                earth_bullets.remove(bullet)

        # checks if earth's bullets collide with an alien bullet
        for al_bullet in alien_bullets:
            if bullet.colliderect(al_bullet):
                earth_bullets.remove(bullet)
                alien_bullets.remove(al_bullet)

        # checks if bullet exits the screen
        if bullet.y < 0:
            earth_bullets.remove(bullet)

    for bullet in alien_bullets:
        bullet.y += BULLET_VEL

        # checks if alien bullet has hit a blockade
        for block in blockade:
            if bullet.colliderect(block):
                alien_bullets.remove(bullet)
                try:
                    if block == blockade[0]:
                        hits[0] += 1
                    if block == blockade[1]:
                        hits[1] += 1
                    if block == blockade[2]:
                        hits[2] += 1
                except IndexError:
                    pass

        # checks if earth's bullets collide with an alien bullet
        for er_bullet in earth_bullets:
            if bullet.colliderect(er_bullet):
                alien_bullets.remove(bullet)
                earth_bullets.remove(er_bullet)

        # checks if alien bullet has hit earth_ship
        if bullet.colliderect(earth_ship):
            pygame.event.post(pygame.event.Event(EARTH_HIT))
            alien_bullets.remove(bullet)
            winner_text = 'You loose'
            draw_winner(winner_text)
            pygame.quit()

        # checks if alien bullet has exit the screen
        if bullet.y > 700:
            alien_bullets.remove(bullet)

    for bullet in big_ship_bullets:
        if len(big_ship) > 0:
            bullet.y += BULLET_VEL

        # checks if big ships' bullet has collided with earth's bullet
        for er_bullet in earth_bullets:
            if bullet.colliderect(er_bullet):
                earth_bullets.remove(er_bullet)
                big_ship_bullets.remove(bullet)

        # checks if big ship bullet has collided with a barricade
        for block in blockade:
            if block.colliderect(bullet):
                big_ship_bullets.remove(bullet)
                try:
                    if block == blockade[0]:
                        hits[0] += 1
                    if block == blockade[1]:
                        hits[1] += 1
                    if block == blockade[2]:
                        hits[2] += 1
                except IndexError:
                    pass

        # checks if big ship bullet has collided with earth rocket
        if bullet.colliderect(earth_ship):
            big_ship_bullets.remove(bullet)
            winner_text = 'You loose'
            draw_winner(winner_text)
            pygame.quit()

        # checks if big ship bullet has exited the screen
        if bullet.y > 700:
            big_ship_bullets.remove(bullet)


def main():
    global select_ship
    earth_spaceship = pygame.Rect(300, 600, EARTHSHIP_WIDTH, EARTHSHIP_HEIGHT)

    # list initiations. please forgive me
    earth_spaceship_bullets = []
    alien_ships_bullets = []
    all_alien_ships = []
    blue_alien_ships = []
    yellow_alien_ships = []
    danger_alien_ships = []
    big_ship = []
    big_ship_bullets = []
    blockades = []
    hits = [0, 0, 0]

    # creating the 3 rows of alien ships
    width_x = 0
    for x in range(4):
        blue_alien_ship = pygame.Rect(width_x, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        yellow_alien_ship = pygame.Rect(width_x, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        danger_alien_ship = pygame.Rect(width_x, 150, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

        blue_alien_ships.append(blue_alien_ship)
        yellow_alien_ships.append(yellow_alien_ship)
        danger_alien_ships.append(danger_alien_ship)

        all_alien_ships.append(blue_alien_ship)
        all_alien_ships.append(yellow_alien_ship)
        all_alien_ships.append(danger_alien_ship)

        width_x += 100

    # creating the 3 barricades
    block_width = 100
    for x in range(3):
        block = pygame.Rect(block_width, 500, BLOCKADE_WIDTH, BLOCKADE_HEIGHT)
        blockades.append(block)
        block_width += 200

    purple_alien_ship = pygame.Rect(0, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    big_ship.append(purple_alien_ship)

    run = True
    clock = pygame.time.Clock()
    try:
        while run:
            """
            game's main loop
            """
            try:
                select_ship = random.choice(all_alien_ships)
            except IndexError:
                pass

            clock.tick(FPS)

            choice = random.randint(1, 20)
            if choice == 12:
                bullet = pygame.Rect(select_ship.x + 40, select_ship.y + 30, 5, 10)
                alien_ships_bullets.append(bullet)
            elif choice == 13 and len(big_ship) > 0:
                big_bullet = pygame.Rect(purple_alien_ship.x + 30,
                                         purple_alien_ship.y + 40, 10, 15)
                big_ship_bullets.append(big_bullet)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RCTRL and len(earth_spaceship_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(earth_spaceship.x + 30,
                                             earth_spaceship.y + 2, 5, 10)
                        earth_spaceship_bullets.append(bullet)

            if len(all_alien_ships) == 0 and len(big_ship) == 0:
                winner_text = 'You win'
                draw_winner(winner_text)
                global SET
                global ALIEN_VEL
                SET = True
                ALIEN_VEL += 3
                main()
            keys_pressed = pygame.key.get_pressed()

            # function calls
            earth_ship_movements(keys_pressed, earth_spaceship)

            bullets_handler(earth_spaceship_bullets, earth_spaceship,
                            alien_ships_bullets, all_alien_ships,
                            big_ship, big_ship_bullets, blockades, hits)

            window(earth_spaceship, purple_alien_ship, blue_alien_ships,
                   yellow_alien_ships, danger_alien_ships, earth_spaceship_bullets,
                   alien_ships_bullets, all_alien_ships, big_ship, big_ship_bullets, blockades, hits)
    except pygame.error:
        pass


main()
