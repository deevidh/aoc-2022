from aocd import data, get, submit  # https://github.com/wimglenn/advent-of-code-data

class puzzle:
    '''
    A class to represent an Advent of Code puzzle. Includes functions to retrieve puzzle input from the server,
    test solutions against example/test input, and submit answers to the server.
    '''
    def __init__(self):
        '''
        Constructs a puzzle instance by automatically retrieving the puzzle input data from the server, and retrieving
        the test input data from a local txt file.

        The puzzle input data is retrieved directly from the server using the aocd module.

        The test input data comes from the AOC puzzle description and it is not retrieved automatically. A local text
        file containing the test input data must be created manually at `./test_data/dayN.py`
        The expected answer for the test data must also be retrieved manually from the puzzle description and should
        be passed as an argument to the test or test_and_submit functions.

        NOTE: The retrieval of both the puzzle input data and test input data require file path introspection to figure out
        what day's data to retrieve. This means that in the name of the file where you are implementing this class must
        clearly contain a number (eg day3.py).

        Parameters
        ----------
            None
        '''
        # Get test input from local file
        self.test_input_filename = f"./test_data/day{get.get_day_and_year()[0]}.txt"
        with open(self.test_input_filename) as f:
                self.test_input = f.read().splitlines()

        # Get puzzle input from server using aocd
        # "Note that aocd will cache puzzle inputs and answers (including incorrect guesses) clientside, to save unnecessary requests to the server."
        self.puzzle_input = data.splitlines()

    def test(self, solution: callable, expected_answer: int) -> bool:
        '''
        Tests the supplied solution by running it using this puzzle's test input data, and evaluating the result against the supplied expected answer

        Parameters
        ----------
        test_solution : function
            The solution which should be run using the test input data
        expected_answer: int
            The answer which we expect our solution to yield when run using the test input data

        Returns
        -------
        result: bool
            Whether the result from the solution matched the supplied expected answer
        '''
        print(f"Testing solution using test input from {self.test_input_filename}...")
        result = solution(self.test_input)
        if result == expected_answer:
            print(f"Result: {result} (PASS)")
            return True
        else:
            print(f"Result: {result} (FAIL: expected {expected_answer})")
            return False

    def submit(self, solution: callable):
        '''
        Runs the supplied solution using this puzzle's test input data, and submits the answer to the server.

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
        submit(result)

        '''
        Tests the supplied solution using the test input data, and if it is successful then runs the solution
        with the real puzzle input and submits the result. This function combines the test and submit functions
        from this class, please see the documentation for those functions for more information.

        Parameters
        ----------
        solution : function
            The solution which should be tested and then used to submit an answer
        expected_answer: int
            The answer which we expect our solution to yield when run using the test input data

        Returns
        -------
        result: bool
            Whether the result from the solution matched the supplied expected answer
        '''
    def test_and_submit(self, solution: callable, expected_answer: int) -> bool:
        if self.test(solution, expected_answer):
            self.submit(solution)
            return True
        else:
            print(f"Test failed, not proceeding with puzzle data")
            return False
