import pygame, random, time
from snake_class import Snake
from square_class import Square

# A few important variables that won't change
screen_width = 495
screen_height = 544

cols = 15
rows = 17

bg_color_1 = (120, 193, 62)
bg_color_2 = (106, 171, 55)

snake_color = (72, 116, 236)
apple_color = (172, 13, 0)

home_page_blue = (47, 0, 219)

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake!')


def drawBackground():
    # This function draws the background of the game
    col_width = screen_width//cols
    row_width = screen_height//rows

    for row in range(rows):
        first_color = True if (row%2 == 0) else False
        for col in range(cols):
            if first_color:
                pygame.draw.rect(window, bg_color_1,
                            pygame.Rect(col*col_width, row*row_width,
                                    col_width, row_width))
            else:
                pygame.draw.rect(window, bg_color_2,
                            pygame.Rect(col*col_width, row*row_width,
                                    col_width, row_width))

            first_color = not first_color


def appleCoordinates(snake):
    # This function finds coordinates for the apple/food and makes sure the
    # coordinates are on the board and not the same as the snake or any
    # other apple
    while True:
        temp = [random.randint(0, cols-1), random.randint(0, rows-1)]
        if temp not in [x.pos for x in snake.body] and \
            temp not in [apple.pos for apple in apples]:
            break
    return temp


def runGame():
    # This function calls a lot of other functions to run the game
    global running, apples, snake, screen, latest_try, best_try
    time.sleep(sleep_time)

    if snake.move() == True:
        if snake.collision(apples, cols, rows) == 1:
            # Goes in here if the snake has hit an apple/food
            apple = Square(appleCoordinates(snake))
            apples.append(apple)
        elif snake.collision(apples, cols, rows) == 0:
            # Goes in here if the snake hits the edge or hits another part of
            # the snake
            latest_try = len(snake.body) - 2
            if best_try < latest_try:
                best_try = latest_try

            screen = 'home'

            title_font = pygame.font.Font("VT323-Regular.ttf", 120)
            title = title_font.render('Game', True, (0, 0, 0))
            window.blit(title, (screen_width/2-87, screen_height/2-130))

            title2 = title_font.render('Over', True, (0, 0, 0))
            window.blit(title2, (screen_width/2-87, screen_height/2-30))

            pygame.display.flip()

            time.sleep(2)
            return

    # This part draws everything
    drawBackground()
    for apple in apples:
        apple.draw(window, screen_width, screen_height, cols, rows, apple_color)
    snake.draw(window, screen_width, screen_height, cols, rows, snake_color)


def homePage():
    # This function draws/makes the home page
    global screen, snake, apples, apples_num, sleep_time

    # Checks if the mouse was clicked and if it was checks where. If it has
    # been clicked on a button, the code will do what the button said.
    left, middle, right = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if screen_width/2-100 <= mouse[0] <= screen_width/2+40 and \
       screen_height/2 + 30 <= mouse[1] <= screen_height/2 + 80 and \
       left:
        screen = 'game'
        if apples_num == 1:
            apples = [Square([12, 8])]
        elif apples_num == 3:
            apples = [Square([12, 8]), Square([12, 5]), Square([12, 11])]
        elif apples_num == 5:
            apples = [Square([10, 8]), Square([7, 5]), Square([7, 11]),
                                            Square([13, 5]), Square([13, 11])]
        snake = Snake([4, 8])
        snake.addPiece()

        return

    if screen_width/2+50 <= mouse[0] <= screen_width/2+100 and \
       screen_height/2 + 30 <= mouse[1] <= screen_height/2 + 80 and \
       left:
        screen = 'settings'
        time.sleep(0.12)
        return

    if apple_setting == 'Random':
        apples_num = random.choice([1, 3, 5])
    if speed_setting == 'Random':
        sleep_time = random.choice([0.15, 0.1, 0.075])

    # This part draws everything, inclduing all images, buttons, and words
    # for this page.
    bg_img = pygame.image.load('bg1.png')
    bg_img = pygame.transform.scale(bg_img,(screen_width, screen_height))
    window.blit(bg_img, (0, 0))

    pygame.font.init()
    title_font = pygame.font.Font("VT323-Regular.ttf", 100)
    title = title_font.render('Snake', True, (255, 255, 255))
    window.blit(title, (screen_width/2-95, 30))

    pygame.font.init()
    word_font = pygame.font.Font("Roboto-Regular.ttf", 15)
    latest_title = word_font.render('Latest Try', True,
                                                (255, 255, 255))
    window.blit(latest_title, (screen_width/2-75, screen_height/2 - 92))

    best_title = word_font.render('Best Try', True,
                                                (255, 255, 255))
    window.blit(best_title, (screen_width/2+33, screen_height/2 - 92))


    pygame.font.init()
    num_font = pygame.font.Font("Roboto-Regular.ttf", 80)
    latest = num_font.render(str(latest_try), True, (255, 255, 255))
    if latest_try > 9:
        window.blit(latest, (screen_width/2-90, screen_height/2 - 75))
    else:
        window.blit(latest, (screen_width/2-65, screen_height/2 - 75))

    best = num_font.render(str(best_try), True, (255, 255, 255))
    if best_try > 9:
        window.blit(best, (screen_width/2+10, screen_height/2 - 75))
    else:
        window.blit(best, (screen_width/2+35, screen_height/2 - 75))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-100,
                                                screen_height/2 + 30, 140, 50),
                                                border_radius = 4)

    font = pygame.font.Font("Roboto-Regular.ttf", 29)
    play = font.render('Play', True, (255, 255, 255))
    window.blit(play, (screen_width/2-57, screen_height/2 + 37))

    pygame.draw.rect(window, home_page_blue, (screen_width/2+50,
                                                screen_height/2 + 30, 50, 50),
                                                border_radius = 4)

    img_normal = pygame.image.load("settings_logo.png").convert()
    img = pygame.transform.scale(img_normal, (42, 42))
    window.blit(img, (screen_width/2+53, screen_height/2 + 32))


def button_click(x1, x2, y1, y2, mouse):
    # This function checks if the mouse was clicked between specfic
    # coordinates/pixels.
    if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
        return True
    return False


def settings():
    # This function draws/makes the settings page
    global screen, apples_num, sleep_time, apple_setting, speed_setting

    # Checks if the mouse was clicked and if it was checks where. If it has
    # been clicked on a button, the code will do what the button said.
    left, middle, right = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if left:
        if 10 <= mouse[0] <= 60 and 12 <= mouse[1] <= 62:
            screen = 'home'
            return

        elif button_click(screen_width/2-110, screen_width/2-30,
                            screen_height/2-150, screen_height/2-100, mouse):
           sleep_time = 0.15
           speed_setting = 'Slow'

        elif button_click(screen_width/2-20, screen_width/2+90,
                            screen_height/2-150, screen_height/2-100, mouse):
           sleep_time = 0.1
           speed_setting = 'Normal'

        elif button_click(screen_width/2-110, screen_width/2-30,
                            screen_height/2-90, screen_height/2-40, mouse):
           sleep_time = 0.075
           speed_setting = 'Fast'

        elif button_click(screen_width/2-20, screen_width/2+100,
                            screen_height/2-90, screen_height/2-40, mouse):
           sleep_time = random.choice([0.15, 0.1, 0.075])
           speed_setting = 'Random'

        elif button_click(screen_width/2-110, screen_width/2+10,
                            screen_height/2-10, screen_height/2+40, mouse):
            apples_num = 1
            apple_setting = '1'

        elif button_click(screen_width/2+20, screen_width/2+150,
                            screen_height/2-10, screen_height/2+40, mouse):
           apples_num = 3
           apple_setting = '3'

        elif button_click(screen_width/2-110, screen_width/2+20,
                            screen_height/2+50, screen_height/2+100, mouse):
           apples_num = 5
           apple_setting = '5'

        elif button_click(screen_width/2+30, screen_width/2+150,
                            screen_height/2+50, screen_height/2+100, mouse):
           apples_num = random.choice([1, 3, 5])
           apple_setting = 'Random'

    # This part draws everything, inclduing all images, buttons, and words
    # for this page.
    background_img = pygame.image.load('bg2.jpg')
    background_img = pygame.transform.scale(background_img, (screen_width,
                                                                screen_height))
    window.blit(background_img, (0, 0))

    pygame.draw.rect(window, home_page_blue, (10, 12, 50, 50), border_radius = 4)

    img_normal = pygame.image.load("back_button.png").convert()
    img = pygame.transform.scale(img_normal, (42, 42))
    window.blit(img, (14, 16))


    pygame.font.init()
    font_title = pygame.font.Font("Roboto-Regular.ttf", 30)
    font = pygame.font.Font("Roboto-Regular.ttf", 28)

    speed = font_title.render('Speed:', True, (255, 255, 255))
    window.blit(speed, (20, screen_height/2-140))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-110,
                                                screen_height/2-150, 80, 50),
                                                border_radius = 4)
    slow = font.render('Slow', True, (255, 255, 255))
    window.blit(slow, (screen_width/2-100, screen_height/2-140))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-20,
                                                screen_height/2-150, 110, 50),
                                                border_radius = 4)
    normal = font.render('Normal', True, (255, 255, 255))
    window.blit(normal, (screen_width/2-10, screen_height/2-140))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-110,
                                                screen_height/2-90, 80, 50),
                                                border_radius = 4)
    fast = font.render('Fast', True, (255, 255, 255))
    window.blit(fast, (screen_width/2-97, screen_height/2 - 80))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-20,
                                                screen_height/2-90, 120, 50),
                                                border_radius = 4)
    random1 = font.render('Random', True, (255, 255, 255))
    window.blit(random1, (screen_width/2-10, screen_height/2 - 80))



    num_apples = font_title.render('Apples:', True, (255, 255, 255))
    window.blit(num_apples, (20, screen_height/2))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-110,
                                                screen_height/2-10, 120, 50),
                                                border_radius = 4)
    one_app = font.render('1 Apple', True, (255, 255, 255))
    window.blit(one_app, (screen_width/2-100, screen_height/2))

    pygame.draw.rect(window, home_page_blue, (screen_width/2+20,
                                                screen_height/2-10, 130, 50),
                                                border_radius = 4)
    three_app = font.render('3 Apples', True, (255, 255, 255))
    window.blit(three_app, (screen_width/2+30, screen_height/2))

    pygame.draw.rect(window, home_page_blue, (screen_width/2-110,
                                                screen_height/2 + 50, 130, 50),
                                                border_radius = 4)
    five_app = font.render('5 Apples', True, (255, 255, 255))
    window.blit(five_app, (screen_width/2-100, screen_height/2 + 60))

    pygame.draw.rect(window, home_page_blue, (screen_width/2+30,
                                                screen_height/2 + 50, 120, 50),
                                                border_radius = 4)
    random2 = font.render('Random', True, (255, 255, 255))
    window.blit(random2, (screen_width/2+40, screen_height/2 + 60))


    set_to_app = font.render(f'Number of Apples: {apple_setting}', True, (255, 255, 255))
    window.blit(set_to_app, (100, screen_height/2 + 110))

    set_to_speed = font.render(f'Speed: {speed_setting}', True, (255, 255, 255))
    window.blit(set_to_speed, (100, screen_height/2 + 150))

# This part creates a few necessary variables
apples = [Square([12, 8])]
apples_num = 1
snake = Snake([4, 8])
snake.addPiece()

sleep_time = 0.1

latest_try = 0
best_try = 0

apple_setting = '1'
speed_setting = 'Normal'

running = True
screen = 'home'

# This while loop runs the game/program.
while running:
    # This part checks if the user has clicked the X button at the top right.
    if pygame.QUIT in [event.type for event in pygame.event.get()]:
        running = False

    # This part picks what page to display
    if screen == 'home':
        homePage()
    elif screen == 'game':
        runGame()
    elif screen == 'settings':
        settings()

    # This line updates the window
    pygame.display.flip()

# This line is to make sure the window closes.
pygame.quit()
