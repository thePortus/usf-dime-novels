# -*- coding: utf-8 -*-
"""common/printer.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

The custom Printer object, a more flexible way to print to screen than print()
"""
import sys
import os


class Printer:
    """
    Custom terminal printer object automatically flushes to screen, unlike
    print(), allowing updates on screen during code blocks (especially loops).
    You can also specify if you want output to end in a newline, or if you want
    to clear previous input from the screen.

    Like print(), Printer can take multiple arguments to print, of different
    types, provided they are separated by commas, e.g. Printer(var1, var2)
    """
    newline = True
    clear = False
    silent = False

    def __init__(self, output, *args, **kwargs):
        """
        Receives list of args to print and keyword options. Outputs args to
        screen according to options.

        kwargs
        newline     boolean     output with a \n (defaults True)
        clear       boolean     clear prior output (defaults False)
        silent      boolean     flag for silent (testing) mode
        """
        output = str(output)
        keys = kwargs.keys()
        if 'newline' in keys:
            self.newline = kwargs['newline']
        if 'clear' in keys:
            self.clear = kwargs['clear']
        if 'silent' in keys:
            self.silent = kwargs['silent']
        if self.clear:
            self.clear_screen()
        # Loop through passed arguments, convert to string and add to output
        for arg in args:
            output += ' ' + str(arg)
        # If newline option passed, add endline char
        if self.newline:
            output += '\n'
        # Ensuring 'silent' mode (for testing) has not been set
        if not self.silent:
            # Write the output to the terminal and flush
            sys.stdout.write(output)
            sys.stdout.flush()

    def clear_screen(self):
        """
        Clears the terminal of previous output. Uses system clear function
        unless system is Windows NT, in that case it calls cls
        """
        # Call different system clear methods
        os.system('cls' if os.name == 'nt' else 'clear')
