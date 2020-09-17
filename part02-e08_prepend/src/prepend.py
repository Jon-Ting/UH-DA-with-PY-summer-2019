#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, initial_str):
        self.start = initial_str

    def write(self, prepend_str):
        print(self.start + prepend_str)

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
