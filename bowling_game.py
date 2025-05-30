"""
Bowling Game Implementation
A module for calculating bowling game scores.

Classes:
    BowlingGame 

Functions:
    __init__(): Initialize a new game.
    roll( , pins): Records the rolls in the game.
    score(): Score calculation.
    _is_strike(): Check if the roll is a strike.
    _is_spare(): Check if the first and second roll added makes a spare.
    _strike_bonus(): Calculate the bonus when you got a strike.
    _spare_bonus(): Calculate the bonus when you get a spare.
    

""" 


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0
    

    def roll(self, pins):
        """
        Records a roll in the game. 

        Args:
            pins: Number of pins knocked down in this roll
        """
        MAX_PINS = 10
        MAX_FRAMES = 10
        
        if pins < 0 or pins > MAX_PINS:
            raise ValueError("Invalid number of pins: must be between 0 and 10.")

        roll_count = len(self.rolls) # Count how many rolls we've made
        frame = 0 # Counter for how many frames have been completed, which is different from frame_index which is used to find the starting position of frame.
        roll_index = 0 # This is a counter for self.roll list, so we know which roll we are at in the frame.

        
        while roll_index < roll_count: 
            if self.rolls[roll_index] == MAX_PINS:  #This is so that if it's a strike roll_index will increase by 1
                roll_index += 1
            else:
                roll_index += 2 # This is for a normal frame where it will take 2 rolls
            frame += 1
            
        
        # Validation: Only apply this check for non-strike frames and before 10th frame
        if frame < MAX_FRAMES:
            if roll_count > 0:
                # If previous roll was not a strike and part of the same frame
                if self.rolls[-1] != MAX_FRAMES and (roll_count - roll_index) % 2 == 1:
                    if self.rolls[-1] + pins > MAX_PINS:
                        raise ValueError("Frame cannot have more than 10 pins.")

        self.rolls.append(pins)


    def score(self):
        """
        Calculate the score for the current game.
        
        Returns:
            Score calculation according to rules.
        """
        score = 0
        frame_index = 0

        for frames in range(10): #Originally range(9) which is wrong because there are 10 frames
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
                score += self.rolls[frame_index] + self.rolls[frame_index + 1] #Originally it is score += self.rolls[frame_index] but is needed self.rolls[frame_index + 1] because in an open frame there's 2 rolls but the original code only counts the first roll therefore the change made it so that you will add the second roll as well when it's an open frame.
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
            
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the rolls at frame_index(first roll) and frame_index + 1(second roll) form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
            
        """
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """
        Calculate the bonus for a strike.

        Args:
            frame_index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
            
        """
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
            
        """ 
        
        
        return self.rolls[frame_index + 2]