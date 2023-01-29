import pygame

# Create window
WIDTH  = 448
HEIGHT = 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FPS
FPS = 60

# Image loading
ICON = pygame.image.load("Space Invaders/Sprites/Icon.png")
PLAYER_IMAGE = pygame.image.load("Space Invaders/Sprites/Player.png")
SMALL_ALIEN_IMAGE = pygame.image.load("Space Invaders/Sprites/Small Alien.png")
SMALL_ALIEN_IMAGE_ANIM = pygame.image.load("Space Invaders/Sprites/Small Alien Anim.png")
MEDIUM_ALIEN_IMAGE = pygame.image.load("Space Invaders/Sprites/Medium Alien.png")
MEDIUM_ALIEN_IMAGE_ANIM = pygame.image.load("Space Invaders/Sprites/Medium Alien Anim.png")
LARGE_ALIEN_IMAGE = pygame.image.load("Space Invaders/Sprites/Large Alien.png")
LARGE_ALIEN_IMAGE_ANIM = pygame.image.load("Space Invaders/Sprites/Large Alien Anim.png")
ALIEN_IMAGE = SMALL_ALIEN_IMAGE

# Set window icon
pygame.display.set_icon(ICON)

PLAYER_WIDTH = 26
PLAYER_HEIGHT = 16
PLAYER_SPEED = 3

BULLET_SPEED = 10

ALIEN_WIDTH = 24
ALIEN_HEIGHT = 16

menu = True
lives = 3
bulletFired = False
start = 0

alienAnimation = 0
alienSpeed = 3
alienSpeedMult = 1
alienMoveDelay = 650
alienWaiting = False
alienEdge = False
alienGoDown = False

enemies = []
bullets = []

player = pygame.Rect(0, HEIGHT-64-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
bullet = pygame.Rect(-10, 0, 2, 8)

# Creates enemies
for y in range(5):
    enemies.append([])
    for x in range(11):
        enemies[y].append(pygame.Rect(x * 34 + 40, y * 34 + 50, ALIEN_WIDTH, ALIEN_HEIGHT))

# FUNCTIONS
# Returns the number of enemies on screen
def countEnemies():
    count = 0

    for y in range(len(enemies)):
        for x in range(len(enemies[y])):
            count += 1
    
    return count

# Handles what happens after all enemies are killed
def leveling():
    global alienSpeed
    global alienSpeedMult

    if countEnemies() == 0:
        pygame.time.delay(1000)
        alienSpeedMult -= 0.25
        if alienSpeedMult <= 0:
            alienSpeedMult = 0.17
        for y in range(5):
            enemies.append([])
            for x in range(11):
                enemies[y].append(pygame.Rect(x * 34 + 40, y * 34 + 50, ALIEN_WIDTH, ALIEN_HEIGHT))

# Changes enemy speed if there are less enemies
def enemySpeed():
    global alienMoveDelay
    global alienSpeed

    if countEnemies() == 55:
        alienMoveDelay = 650*alienSpeedMult
        if alienSpeed > 0:
            alienSpeed = 3
        else:
            alienSpeed = -3
    if countEnemies() == 45:
        alienMoveDelay = 500*alienSpeedMult
        if alienSpeed > 0:
            alienSpeed = 4
        else:
            alienSpeed = -4
    if countEnemies() == 30:
        alienMoveDelay = 350*alienSpeedMult
        if alienSpeed > 0:
            alienSpeed = 5
        else:
            alienSpeed = -5
    if countEnemies() == 20:
        alienMoveDelay = 225*alienSpeedMult
    if countEnemies() == 5:
        alienMoveDelay = 150*alienSpeedMult
        if alienSpeed > 0:
            alienSpeed = 7
        else:
            alienSpeed = -7

# Wait function for enemies that allows the game to run while waiting for the enemies to move
def enemyWait(start):
    global alienMoveDelay
    global alienWaiting

    elapsed = pygame.time.get_ticks() - start

    if elapsed >= alienMoveDelay:
        alienWaiting = False

# Moves enemies
def moveEnemies():
    global alienAnimation
    global alienWaiting
    global alienSpeed
    global alienGoDown
    global start

    for y in range(len(enemies)):
        for x in range(len(enemies[y])):
            if not alienWaiting:
                if alienGoDown == True:
                    enemies[y][x].y += 25
                enemies[y][x].x += alienSpeed
    
    if not alienWaiting:
        if alienAnimation == 1:
            alienAnimation = 0
        else:
            alienAnimation = 1

    if not alienWaiting:
        alienWaiting = True
        start = pygame.time.get_ticks()
    else:
        enemyWait(start)
        alienGoDown = False
    
    for y in range(len(enemies)):
        for x in range(len(enemies[y])):
            if enemies[y][x].x >= WIDTH-ALIEN_WIDTH-10:
                alienSpeed = abs(alienSpeed)*-1
                alienGoDown = True
            if enemies[y][x].x <= 10:
                alienSpeed = abs(alienSpeed)
                alienGoDown = True

# Handles collitions
def collitions():
    global bulletFired

    for y in range(len(enemies)):
        for x in range(len(enemies[y])):
            if pygame.Rect.colliderect(bullet, enemies[y][x-1]):
                enemies[y][x-1].x = -100
                enemies[y].remove(enemies[y][x-1])

                bulletFired = False

# Sets player bouderies
def playerBounds():
    global player
    
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - PLAYER_WIDTH:
        player.x = WIDTH - PLAYER_WIDTH

# Handles bullet logic
def bulletLogic(keys_pressed):
    global bulletFired

    if not bulletFired:
        bullet.y = player.y
        bullet.x = player.x + PLAYER_WIDTH/2-1 
    else:
        bullet.y -= BULLET_SPEED

    if keys_pressed[pygame.K_UP] and bulletFired == False:
        bulletFired = True
    
    if bullet.y < -8:
        bulletFired = False
    
# Render stuff to the screen and update it
def render():
    global ALIEN_IMAGE
    global SMALL_ALIEN_IMAGE
    global SMALL_ALIEN_IMAGE_ANIM
    global MEDIUM_ALIEN_IMAGE
    global MEDIUM_ALIEN_IMAGE_ANIM
    global LARGE_ALIEN_IMAGE
    global LARGE_ALIEN_IMAGE_ANIM
    global alienAnimation

    WIN.fill(BLACK)

    if bulletFired:
        pygame.draw.rect(WIN, WHITE, bullet)
    
    for i in range(len(enemies)):
        if alienAnimation == 0:
            if i == 0:
                ALIEN_IMAGE = SMALL_ALIEN_IMAGE
            elif i == 1 or i == 2:
                ALIEN_IMAGE = MEDIUM_ALIEN_IMAGE
            else:
                ALIEN_IMAGE = LARGE_ALIEN_IMAGE
        if alienAnimation == 1:
            if i == 0:
                ALIEN_IMAGE = SMALL_ALIEN_IMAGE_ANIM
            elif i == 1 or i == 2:
                ALIEN_IMAGE = MEDIUM_ALIEN_IMAGE_ANIM
            else:
                ALIEN_IMAGE = LARGE_ALIEN_IMAGE_ANIM
        for j in range(len(enemies[i])):
            WIN.blit(ALIEN_IMAGE, (enemies[i][j].x, enemies[i][j].y))

    # Drawing life icons
    for i in range(lives - 1):
        WIN.blit(PLAYER_IMAGE, (6 + i*32, HEIGHT-24))
    
    WIN.blit(PLAYER_IMAGE, (player.x, player.y))

    pygame.display.update()

# Main game loop and logic
def main():
    clock = pygame.time.Clock()
    
    run = True
    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Input
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            player.x -= PLAYER_SPEED
        if keys_pressed[pygame.K_RIGHT]:
            player.x += PLAYER_SPEED
        
        collitions()
        moveEnemies()
        enemySpeed()
        playerBounds()
        bulletLogic(keys_pressed)
        leveling()
        render()

    pygame.quit()

if __name__ == "__main__":
    main()