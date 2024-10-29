# Applying Booth's Algorithm using Python in classical Computer

- This week, we focused on implementing Booth's Algorithm in Python, which is a method for finding the lexicographically smallest rotation of a string. 
- The implementation is found in the booth.py file. 

## Overview of booth.py
The booth.py script reads a list of words from the words_109583.txt file, processes each word using Booth's Algorithm, and outputs the results to a file named booth.txt. 
The algorithm works by concatenating the string with itself and using a failure function to efficiently find the smallest rotation.

## Key Features of booth.py
- **Input Handling**: The script reads words from a text file and strips any whitespace.
- **Booth's Algorithm**: The core function, `booth`, computes the smallest rotation of each word.
- **Output**: The results are sorted and written to an output file.

## Makefile
To streamline the execution of our scripts, we created a Makefile. This file automates the process of running booth.py and managing dependencies. 
It includes targets for running the scripts and cleaning up output files.

### Key Targets in the Makefile
- **run**: Executes both booth.py and lydon.py in sequence.
- **clean**: Removes generated output files to keep the workspace tidy.
- **help**: Provides usage instructions for the Makefile.

## Conclusion
This week’s work has enhanced our understanding of string manipulation algorithms and the importance of automation in software development through the use of Makefiles. 
We look forward to applying these concepts in future projects and exploring more advanced algorithms.
