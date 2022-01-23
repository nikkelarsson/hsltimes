"""Routines for reading in files."""


import abc


class Reader(abc.ABC):
    """Defines an interface all the Reader subclasses should adhere to."""

    @abc.abstractmethod
    def read_data(self, filename: str) -> object:
        pass


class TextFileReader(Reader):
    """Reader for reading data from a text file."""

    def __init__(self) -> None:
        """Initializes TextFileReader for reading."""
        self.encoding: str = "utf-8"

    def read_data(self, filename: str, start: int=0) -> object:
        """
        Reads in a text file.

        Parameters:
            filename.... File to read from.
            start....... The row number from which to start reading.
                         By default, start reading from the first row.

        Returns:
            The contents of the text file as a generator object.
        """
        with open(filename, "r", encoding=self.encoding) as f:
            return (
                i for idx, i in enumerate(f.read().split("\n"))
                if idx >= start
            )
