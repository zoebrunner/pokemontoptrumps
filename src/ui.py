from typing import List

class TerminalUI:

    def __init__(self):
        pass

    def ask_integer(self, question: str, min: int = None, max: int = None) -> str:
        """Ask for an integer on console

        Args:
            question (str): Question to ask
            min (int, optional): Minimum acceptable input. Defaults to None.
            max (int, optional): Maximum acceptable input. Defaults to None.

        Returns:
            str: User input
        """

        value = input(f"{question}: ")
        try:
            value = int(value)
            if (max is not None) and (value > max):
                self.display_single(f"Maximum value is {max}, please try again.\n")
                return self.ask_integer(question, min=min, max=max)
            if (min is not None) and (value < min):
                self.display_single(f"Minimum value is {min}, please try again.\n")
                return self.ask_integer(question, min=min, max=max)

            return value
        except Exception:
            self.display_single("Value must be integer, please try again.\n")
            return self.ask_integer(question, min=min, max=max)

    def ask_choices(self, choices: List[str]) -> int:
        """Given a list of choices, ask for user input

        Args:
            choices (List[str]): Available choices

        Returns:
            int: Index of choice
        """

        for i in range(len(choices)):
            self.display_single(f"{i+1}: {choices[i]}")

        res = self.ask_integer("Please input your choice", 1, len(choices))
        return res - 1

    def display_single(self, value: str):
        print(value)

    def display_multiple(self, values: List[str]):
        for value in values:
            print(value)
