from turtle import color, shape

class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################
        self.__offsets__ =  {   "up": (0, 20),\
                                "down": (0, -20),\
                                "left": (-20, 0),\
                                "right": (20, 0)
                             }
        self.shape = [[0,0],[0,1]] # initialisation with a two element lenght
        self.direction = "up"
        self.color = "red"
        self.window_size = window_size
        self.GAME_OVER = False




    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.direction != "down":
            self.direction = "up"
        return()
        ##########################################
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != "up":
            self.direction = "down"
        return()
        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != "right":
            self.direction = "left"
        return()
        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != "left":
            self.direction = "right"
        return()
        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        ############## WRITE BELOW ###############

        iffood_col = False
        current_snake_head = self.shape[0]
        # Function to compute the distance between the head and the food.
        def distance_cal (current_snake_head ,current_food_position ): 
            x_0 = current_snake_head[0]
            x_1 = current_food_position[0]
            y_0 = current_snake_head[1]
            y_1 = current_food_position[1]
            return(((x_0-x_1)**2+(y_0-y_1)**2)**0.5)
        #print(distance_cal(current_snake_head ,current_food_position))
        if distance_cal (current_snake_head ,current_food_position)< 20:
            iffood_col = True # Condition for Collided
            

        return (iffood_col)
        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """
        ############## WRITE BELOW ###############
        
        # Left and right restriction
        if self.shape[0][0]>self.window_size[0]/2: # seeing it head of snake is greater than the window size
            self.shape[0][0] = -self.window_size[0]/2
        if self.shape[0][0]<-self.window_size[0]/2:
            self.shape[0][0] = self.window_size[0]/2

        # Top and bottom restrictions
        if self.shape[0][1]>self.window_size[1]/2:
            self.shape[0][1] = -self.window_size[1]/2
        if self.shape[0][1]<-self.window_size[1]/2:
            self.shape[0][1] = self.window_size[1]/2
        return()
        ##########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """
        
        # Call to draw the whole snake
        
        
        ############## WRITE BELOW ###############
        current_snake_head = self.shape[0]
        new_head_list = [current_snake_head[0]+self.__offsets__[self.direction][0],\
            current_snake_head[1]+self.__offsets__[self.direction][1]] # computation of new head location
        self.shape.insert(0,new_head_list) # The new head is added into the shape of snake
        self.shape.pop() # the last element is poped out since the snake moves
        
        # Testing if GAME OVER (If Snake bites itself)
        if (self.shape[0] in self.shape[1:]):
            print("Ate itself")
            self.GAME_OVER =True
        return()
        ##########################################









