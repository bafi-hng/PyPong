import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

speed = 300
dt = 0

# player object
player_surf = pygame.Surface((30, 30))
pygame.draw.circle(player_surf, "white", (15, 15), 15)
player_rect = player_surf.get_rect()

# start position
player_rect.x = screen.get_width() / 2
player_rect.y = screen.get_height() / 2


while running:

    screen.fill((0,0,0))
    screen.blit(player_surf, player_rect)

    dist = speed * dt
    keys = pygame.key.get_pressed()

    # control movement
    if keys[pygame.K_UP]:
        player_rect.y -= dist
    if keys[pygame.K_DOWN]:
        player_rect.y += dist
    if keys[pygame.K_LEFT]:
        player_rect.x -= dist
    if keys[pygame.K_RIGHT]:
        player_rect.x += dist

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

    