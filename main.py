import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Snake properties
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for index, x in enumerate(snake_list):
        if index == 0:
            # Draw the head of the snake
            pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])
            # Draw the eyes of the snake
            pygame.draw.circle(screen, BLACK, [x[0] + snake_block // 4, x[1] + snake_block // 4], snake_block // 8)
            pygame.draw.circle(screen, BLACK, [x[0] + 3 * snake_block // 4, x[1] + snake_block // 4], snake_block // 8)
        else:
            # Draw a smaller rectangle for the body segments
            pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block - 4, snake_block - 4])
            # Draw the tongue of the snake
            pygame.draw.line(screen, BLACK, [x[0] + snake_block // 2, x[1] + snake_block], [x[0] + snake_block // 2, x[1] + 3 * snake_block // 2], snake_block // 8)

def our_snake(snake_block, snake_list):
    for index, x in enumerate(snake_list):
        if index == 0:
            # Draw the head of the snake
            pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])
            # Draw the eyes of the snake
            pygame.draw.circle(screen, BLACK, [x[0] + snake_block // 4, x[1] + snake_block // 4], snake_block // 8)
            pygame.draw.circle(screen, BLACK, [x[0] + 3 * snake_block // 4, x[1] + snake_block // 4], snake_block // 8)
        else:
            # Draw a smaller rectangle for the body segments
            pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block - 4, snake_block - 4])
            # Draw the tongue of the snake
            pygame.draw.line(screen, BLACK, [x[0] + snake_block // 2, x[1] + snake_block], [x[0] + snake_block // 2, x[1] + 3 * snake_block // 2], snake_block // 8)

            # Draw a smaller rectangle for the body segments
            pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block - 4, snake_block - 4])
            # Draw the tongue of the snake
            pygame.draw.line(screen, BLACK, [x[0] + snake_block // 2, x[1] + snake_block], [x[0] + snake_block // 2, x[1] + 3 * snake_block // 2], snake_block // 8)

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

    score = 0
    level = 1
    snake_speed = SNAKE_SPEED

    while not game_over:

        while game_close == True:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            # Display the score
            score_text = font.render("Score: " + str(score), True, WHITE)
            screen.blit(score_text, [50, 50])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Adjust snake's position when it hits the screen boundaries
        if x1 >= SCREEN_WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = SCREEN_WIDTH - SNAKE_BLOCK
        elif y1 >= SCREEN_HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = SCREEN_HEIGHT - SNAKE_BLOCK

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)

        # Display the score and level
        score_text = font.render("Score: " + str(score), True, WHITE)
        level_text = font.render("Level: " + str(level), True, WHITE)
        screen.blit(score_text, [50, 50])
        screen.blit(level_text, [50, 80])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
            Length_of_snake += 1
            score += 1

            # Increase the level and snake speed every 10 points
            if score % 10 == 0:
                level += 1
                snake_speed += 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()