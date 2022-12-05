from aocd.models import Puzzle # https://github.com/wimglenn/advent-of-code-data
from aocd import get, submit

class puzzle:
    '''
    A class to represent an Advent of Code puzzle. Includes functions to retrieve puzzle input from the server,
    test solutions against example/test input, and submit answers to the server.
    '''
    def __init__(self):
        '''
        Constructs a puzzle instance by automatically retrieving the puzzle input data and example input.

        The puzzle input data and the example/test input are retrieved directly from the server using the aocd module.
        The expected answer for the example input must be retrieved manually from the puzzle description and should be passed
        as an argument to the test or test_and_submit functions.

        NOTE: The retrieval of both the puzzle input data and example input uses file path introspection to figure out
        what day's data to retrieve. This means that in the name of the file where you are implementing this class must
        clearly contain a number (eg day3.py).

        Parameters
        ----------
            None
        '''
        # Get day using filename introspection
        self.aocd_year=get.get_day_and_year()[1]
        self.aocd_day=get.get_day_and_year()[0]

        # Get puzzle input and example input from server using aocd
        # "Note that aocd will cache puzzle inputs and answers (including incorrect guesses) clientside, to save unnecessary requests to the server."
        self.aocd_puzzle = Puzzle(year=self.aocd_year, day=self.aocd_day)
        self.test_input = self.aocd_puzzle.example_data.splitlines()
        self.puzzle_input = self.aocd_puzzle.input_data.splitlines()

        print(f"Welcome to Advent of Code day {self.aocd_day}: {self.aocd_puzzle.title}\n{self.aocd_puzzle.url}\n")

    def test(self, solution: callable, expected_answer: int or str) -> bool:
        '''
        Tests the supplied solution by running it using this puzzle's example input, and evaluating the result against the supplied example answer

        Parameters
        ----------
        test_solution : function
            The solution which should be run using the example input
        example_answer: int or str
            The answer which we expect our solution to yield when run using the example input

        Returns
        -------
        result: bool
            Whether the result from the solution matched the supplied example answer
        '''
        print(f"Testing solution using example input...")
        result = solution(self.test_input)
        if result == expected_answer:
            print(f"Result: {result} (PASS)")
            return True
        else:
            print(f"Result: {result} (FAIL: expected {expected_answer})")
            return False

    def submit(self, solution: callable):
        '''
        Runs the supplied solution using this puzzle's input data, and submits the answer to the server.

        Parameters
        ----------
        solution : function
            The solution which should be run using the puzzle input data

        Returns
        -------
        Nothing
        '''
        print(f"Running solution using puzzle input...")
        result = solution(self.puzzle_input)
        print(f"Result: {result}")
        print(f"Submitting...")
        #self.aocd_puzzle.submit(result)
        submit(result)

        '''
        Tests the supplied solution using the example input, and if it is successful then runs the solution
        with the real puzzle input and submits the result. This function combines the test and submit functions
        from this class, please see the documentation for those functions for more information.

        Parameters
        ----------
        solution : function
            The solution which should be tested and then used to submit an answer
        expected_answer: int or str
            The answer which we expect our solution to yield when run using the example input

        Returns
        -------
        result: bool
            Whether the result from the solution matched the supplied example answer
        '''
    def test_and_submit(self, solution: callable, expected_answer: int or str) -> bool:
        if self.test(solution, expected_answer):
            self.submit(solution)
            return True
        else:
            print(f"Test failed, not proceeding with puzzle data")
            return False
