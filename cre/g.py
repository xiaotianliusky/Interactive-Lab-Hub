# rocket
# joystick control of rocket in space
"""
WHS
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]

screen_x = 1280
screen_y = 720
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Rockets in Space!")
 
# Loop until the user clicks the close button .
done = False 
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
    done = True
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

speed_x = 0.0
speed_y = 0.0
default_x = 640.5
default_y = 360.5
radius = 20

x = default_x
y = default_y
max_speed_x = 3.0
max_speed_y = 3.0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    """
    axes = joystick.get_numaxes()
       
    for i in range( axes ):
        axis = joystick.get_axis( i )
        textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
    """

             
    # --- Game logic should go here

    pygame.draw.circle(screen, BLACK, (int(x), int(y)), 20, 5) 
    # This gets the position of the axis on the game controller
    # It returns a number between -1.0 and +1.0
    horiz_axis_pos = my_joystick.get_axis(0)
    vert_axis_pos = my_joystick.get_axis(1)
    button_reset = my_joystick.get_button(0)
    if button_reset == 1:
        x = default_x
        y = default_y
        speed_x = 0
        speed_y = 0


    button_exit = my_joystick.get_button(4)
    if button_exit == 1:
        done = True
    # the axis. We multiply by 10 to speed up the movement.
    # Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
    """
    if abs(speed_x) > abs(max_speed_x):
        speed_x = max_speed_x * (speed_x/speed_x)
    """    
    speed_x = speed_x + horiz_axis_pos
    """
    if abs(speed_y) > abs(max_speed_y):
        speed_y = max_speed_y * (speed_y/speed_y)
    """    
    speed_y = speed_y + vert_axis_pos
    
    #Bounce
    if x < 0 or x > screen_x - radius/2:
        speed_x = -speed_x
    if y < 0 or y > screen_y - radius/2:
        speed_y = -speed_y
    x = x + speed_x
    y = y + speed_y
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), radius, 5) 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(240)
 
# Close the window and quit.
pygame.quit()
