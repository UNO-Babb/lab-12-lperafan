# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of nubmers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that it random.

import time
import random
import os
# Your current working directory needs to see the AllSorts.py
# If you have issues you should comment out this line.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import AllSorts

def main():
  random.seed(2020) # This makes sure that the random list will be the same every time.


  numberTerms = 10000

  orderedList = []
  reversedList = []
  randomList = []

  for i in range(numberTerms):
      orderedList.append(i)
      reversedList.insert(0, i)
      randomList.append(random.randint(1, numberTerms))  # Ensuring random values are within a reasonable range

  sorts = [
      ("Bubble Sort", AllSorts.bubbleSort),
      ("Bubble Sort (Early Exit)", AllSorts.bubbleSortEarlyExit),
      ("Selection Sort", AllSorts.selectionSort),
      ("Insertion Sort", AllSorts.insertionSort),
      ("Merge Sort", AllSorts.mergeSort)
    ]

  print(f"Begin Sorting {numberTerms} elements.")

  for sort_name, sort_function in sorts:
      for dataset_name, dataset in [("Ordered", orderedList), ("Reversed", reversedList), ("Random", randomList)]:
          startTime = time.time()
          sort_function(dataset.copy())  # Using `.copy()` to avoid modifying the original list
          endTime = time.time()
          elapsedTime = endTime - startTime
          print(f"{sort_name} - {dataset_name} List time: {elapsedTime:.5f} seconds")

  print("Sorting Complete")


if __name__ == '__main__':
  main()
