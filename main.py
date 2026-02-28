import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()

clock = pygame.time.Clock()
running = True

speed_x = 300
speed_y = 400
dt = 0

# pong object
pong_surf = pygame.Surface((30, 30))
pygame.draw.circle(pong_surf, "white", (15, 15), 15)
pong_rect = pong_surf.get_rect()

# start position
pong_rect.x = screen.get_width() / 2
pong_rect.y = screen.get_height() / 2


while running:

    screen.fill((0,0,0))
    screen.blit(pong_surf, pong_rect)

    pong_rect.x += speed_x * dt
    pong_rect.y += speed_y * dt

    if pong_rect.left <= screen_rect.left or pong_rect.right >= screen_rect.right:
        speed_x *= -1
    if pong_rect.top <= screen_rect.top or pong_rect.bottom >= screen_rect.bottom:
        speed_y *= -1


    pygame.display.flip()

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()