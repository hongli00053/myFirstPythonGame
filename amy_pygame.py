import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")
screenWidth = 500

width = 40
height = 60
vel = 10
x = 50
y = screenWidth - height
isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 -width - 5:
        x += vel
    if not(isJump):    
        if keys[pygame.K_UP] and y > 5:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500-height - 5:    
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False    
            jumpCount = 10        



    win.fill((255, 182,193))

    pygame.draw.rect(win, (255, 51, 106), (x, y, width, height))        
    pygame.display.update()


pygame.quit()            