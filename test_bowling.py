"""
Unit tests for the Bowling Game

This module contains basic unit tests for the BowlingGame class.
Students should expand these tests to cover all functionality and edge cases.
"""

import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for roll in range(n):
            self.game.roll(pins)    
            
    def roll_strike(self):
        """Helper to roll a strike(10 pins)"""
        self.game.roll(10)
        
    def test_open_frame_score_calculation(self):
        """Test the calculation of an open frame game"""
        self.game.roll(3)
        self.game.roll(2)
        self.game.roll(6)
        self.game.roll(3)
        self.roll_many(16, 0)
        # Expected score: 14 (3+2+6+3+16*0)
        self.assertEqual(14, self.game.score())
        
    def test_spare_score_calculation(self):
        """Test the calculation of a game that contains one spare"""
        self.game.roll(3)
        self.game.roll(7)
        self.game.roll(9)
        self.game.roll(1)
        self.roll_many(16, 0)
        #Expected score: 29 (3+7+9+9+1+0+0*16)
        self.assertEqual(29, self.game.score())
        
    def test_strike_score_calculation(self):
        """Test the calculation of a game that contains at least one strike"""
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(2)
        self.roll_strike()
        self.roll_many(16, 0)
        #Expected score: 30 (10+3+2+3+2+10+0+0+0*16)
        self.assertEqual(30, self.game.score())
        
    def test_perfect_game(self):
        """Test a perfect game, where you roll all strike"""
        self.roll_many(12,10) #You get extra rolls on the 10th frame
        # Expected score: 300 (10*10*3) 10 for the strike, another 10 for the amount of frames, 3 for the amount of rolls in each frames
        self.assertEqual(300, self.game.score())
        
    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())
        
    def test_all_spares(self):
        """Test a game where you get all spare"""
        for frame in range(10):
            self.game.roll(5)
            self.game.roll(5)
        self.game.roll(5) #Bonus rolls
        # Expected score: 150 [(5+5+5)*10], 5 points scored from one roll, another 5 from the second which makes it a spare, add another 5 score as the bonus from the roll on the next frame, multiply by 10 for the amount of frames played.
        self.assertEqual(150, self.game.score())

    def test_multiple_strike(self):
        """Test a game where you roll multiple strikes"""
        self.roll_strike()  
        self.roll_strike()  
        self.game.roll(7)
        self.game.roll(3) # Using the validation tells us that this roll which was originally 8 would up up to be over 10. Therefore, we're dropping it down to 3 making the third frame a spare.
        self.game.roll(2)
        self.game.roll(5)
        self.roll_many(12, 0)
        # Expected score: 66 (10+10+7+10+7+3+7+3+2+2+5+0*12)
        self.assertEqual(66, self.game.score())
    

    
    # def test_all_ones(self):
    #     """Test a game where one pin is knocked down on each roll."""
    #     self.roll_many(20, 1)   
    #     # Expected score: 20 (1 pin × 20 rolls)
    #     self.assertEqual(20, self.game.score())


if __name__ == "__main__":
    unittest.main()