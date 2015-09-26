import unittest
from game_of_life import GameOfLife


class TestGameOfLife(unittest.TestCase):
    gol = GameOfLife()

    #Live Cells
    def test_live_cell_with_zero_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 0))

    def test_live_cell_with_one_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 1))

    def test_live_cell_with_two_live_neighbours_stays_alive(self):
        self.assertTrue(self.gol.will_be_alive_in_next_generation(True, 2))

    def test_live_cell_with_three_live_neighbours_stays_alive(self):
        self.assertTrue(self.gol.will_be_alive_in_next_generation(True, 3))

    def test_live_cell_with_four_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 4))

    def test_live_cell_with_five_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 5))

    def test_live_cell_with_six_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 6))

    def test_live_cell_with_seven_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 7))

    def test_live_cell_with_eight_live_neighbours_dies(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(True, 8))

    #Dead Cells
    def test_dead_cells_with_zero_live_neighbours_stay_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 0))

    def test_dead_cells_with_one_live_neighbour_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 1))

    def test_dead_cells_with_two_live_neighbours_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 2))

    def test_dead_cell_with_three_live_neighbours_comes_to_life(self):
        self.assertTrue(self.gol.will_be_alive_in_next_generation(True, 3))

    def test_dead_cell_with_four_live_neighbours_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 4))

    def test_dead_cell_with_five_live_neighbours_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 5))

    def test_dead_cell_with_six_live_neighbours_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 6))

    def test_dead_cell_with_seven_live_neighbours_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 7))

    def test_dead_cell_with_three_live_neighbours_stays_dead(self):
        self.assertFalse(self.gol.will_be_alive_in_next_generation(False, 8))


class LiveNeighbourCounterTests(unittest.TestCase):
    gol = GameOfLife()

    def test_dead_grid(self):
        grid = [[0,0,0],
                [0,0,0],
                [0,0,0]]
        self.assertEquals(0, self.gol.count_neighbours(grid, (0,0)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (0,1)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (0,2)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (1,0)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (1,1)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (1,2)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (2,0)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (2,1)))
        self.assertEquals(0, self.gol.count_neighbours(grid, (2,2)))

    def test_zero_zero_has_eight_live_neighbours(self):
        grid = [[1,1,1],
                [1,1,1],
                [1,1,1]]
        self.assertEquals(8, self.gol.count_neighbours(grid, (0,0)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (0,1)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (0,2)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (1,0)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (1,1)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (1,2)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (2,0)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (2,1)))
        self.assertEquals(8, self.gol.count_neighbours(grid, (2,2)))


if __name__ == '__main__':
    unittest.main()