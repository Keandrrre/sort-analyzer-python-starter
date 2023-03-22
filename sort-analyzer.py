# SORT ANALYZER STARTER CODE

import time
import os

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS


def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])

# Algorithms


def bubbleSort(anArray):
    # Get Number of Passes
    for i in range(len(anArray) - 1):
        # Get adjacent number for comparison
        for a in range(len(anArray) - i - 1):
            if anArray[a] > anArray[a + 1]:
                firstPos = anArray[a]
                anArray[a] = anArray[a + 1]
                anArray[a + 1] = firstPos


def selectionSort(anArray):
    for i in range(len(anArray) - 1):
        min = i
        for e in range(i + 1, len(anArray)):
            if anArray[e] < anArray[min]:
                min = e
        anArray[min], anArray[i] = anArray[i], anArray[min]


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insert_val = anArray[i]
        insert_pos = i - 1

        while insert_pos >= 0 and insert_val < anArray[insert_pos]:
            anArray[insert_pos + 1] = anArray[insert_pos]
            insert_pos = insert_pos - 1

            anArray[insert_pos + 1] = insert_val


# Run Test
loop = True
while loop == True:
    selection = input("1=Bubble 2=Selection 3=Insertion 4=Exit\nSelect: ")
    if selection == 1:
        print("Running Tests for Bubble Sort\n")
        # Random Data (Bubble Sort)
        startTime_RandomData = time.time()
        bubbleSort(randomData)
        endTime_RandomData = time.time()
        print("RUTIME (Random Data): " +
              {endTime_RandomData - startTime_RandomData} + " Seconds")
        # Reversed Data (Bubble Sort)
        startTime_ReversedData = time.time()
        bubbleSort(reversedData)
        endTime_ReversedData = time.time()
        print("RUTIME (Reversed Data): " +
              {endTime_ReversedData - startTime_ReversedData} + " Seconds")
        # Nearly Sorted Data (Bubble Sort)
        startTime_NearlySortedData = time.time()
        bubbleSort(nearlySortedData)
        endTime_NearlySortedData = time.time()
        print("RUTIME (Nearly Sorted Data): " +
              {endTime_NearlySortedData - startTime_NearlySortedData} + " Seconds")
        # Few Unique Data (Bubble Sort)
        startTime_FewUniqueData = time.time()
        bubbleSort(fewUniqueData)
        endTime_FewUniqueData = time.time()
        print("RUTIME (few Unique Data): " +
              {endTime_FewUniqueData - startTime_FewUniqueData} + " Seconds")
    elif selection == 4:
        loop = False
        os.system('cls')

        # EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
        # startTime = time.time()
        # bubbleSort(randomData)
        # endTime = time.time()
        # print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
