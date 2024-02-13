#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sort."""
        print(sorted(self))
