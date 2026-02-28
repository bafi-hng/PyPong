import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()

clock = pygame.time.Clock()
running = True

speed = 400
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

    if player_rect.left <= screen_rect.left:
        player_rect.left = screen_rect.left
    if player_rect.right >= screen_rect.right:
        player_rect.right = screen_rect.right
    if player_rect.top <= screen_rect.top:
        player_rect.top = screen_rect.top
    if player_rect.bottom >= screen_rect.bottom:
        player_rect.bottom = screen_rect.bottom

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()