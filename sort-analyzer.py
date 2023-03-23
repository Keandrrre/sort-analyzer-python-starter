# SORT ANALYZER STARTER CODE

import time
import os

loop = True
while loop == True:
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
    # print(randomData[0:50])
    # print(reversedData[0:50])
    # print(nearlySortedData[0:50])
    # print(fewUniqueData[0:50])

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
    selection = int(input(
        "1=BubbleSort 2=SelectionSort 3=InsertionSort 4=Exit\nSelect: "))
    if selection == 1:
        print("[Running Tests for Bubble Sort]")
        # Random Data (Bubble Sort)
        startTime_RandomData = time.time()
        bubbleSort(randomData)
        endTime_RandomData = time.time()
        print("\tRUNTIME (Random Data): " +
              str(endTime_RandomData - startTime_RandomData) + " Seconds")
        # Reversed Data (Bubble Sort)
        startTime_ReversedData = time.time()
        bubbleSort(reversedData)
        endTime_ReversedData = time.time()
        print("\tRUNTIME (Reversed Data): " +
              str(endTime_ReversedData - startTime_ReversedData) + " Seconds")
        # Nearly Sorted Data (Bubble Sort)
        startTime_NearlySortedData = time.time()
        bubbleSort(nearlySortedData)
        endTime_NearlySortedData = time.time()
        print("\tRUNTIME (Nearly Sorted Data): " +
              str(endTime_NearlySortedData - startTime_NearlySortedData) + " Seconds")
        # Few Unique Data (Bubble Sort)
        startTime_FewUniqueData = time.time()
        bubbleSort(fewUniqueData)
        endTime_FewUniqueData = time.time()
        print("\tRUNTIME (few Unique Data): " +
              str(endTime_FewUniqueData - startTime_FewUniqueData) + " Seconds")
        print("[Test Finished]\n")
    elif selection == 2:
        print("[Running Tests for Selection Sort]")
        # Random Data (Selection Sort)
        startTime_RandomData = time.time()
        selectionSort(randomData)
        endTime_RandomData = time.time()
        print("\tRUNTIME (Random Data): " +
              str(endTime_RandomData - startTime_RandomData) + " Seconds")
        # Reversed Data (Selection Sort)
        startTime_ReversedData = time.time()
        selectionSort(reversedData)
        endTime_ReversedData = time.time()
        print("\tRUNTIME (Reversed Data): " +
              str(endTime_ReversedData - startTime_ReversedData) + " Seconds")
        # Nearly Sorted Data (Selection Sort)
        startTime_NearlySortedData = time.time()
        selectionSort(nearlySortedData)
        endTime_NearlySortedData = time.time()
        print("\tRUNTIME (Nearly Sorted Data): " +
              str(endTime_NearlySortedData - startTime_NearlySortedData) + " Seconds")
        # Few Unique Data (Selection Sort)
        startTime_FewUniqueData = time.time()
        selectionSort(fewUniqueData)
        endTime_FewUniqueData = time.time()
        print("\tRUNTIME (few Unique Data): " +
              str(endTime_FewUniqueData - startTime_FewUniqueData) + " Seconds")
        print("[Test Finished]\n")
    elif selection == 3:
        print("[Running Tests for Insertion Sort]")
        # Random Data (Insertion Sort)
        startTime_RandomData = time.time()
        insertionSort(randomData)
        endTime_RandomData = time.time()
        print("\tRUNTIME (Random Data): " +
              str(endTime_RandomData - startTime_RandomData) + " Seconds")
        # Reversed Data (Insertion Sort)
        startTime_ReversedData = time.time()
        insertionSort(reversedData)
        endTime_ReversedData = time.time()
        print("\tRUNTIME (Reversed Data): " +
              str(endTime_ReversedData - startTime_ReversedData) + " Seconds")
        # Nearly Sorted Data (Insertion Sort)
        startTime_NearlySortedData = time.time()
        insertionSort(nearlySortedData)
        endTime_NearlySortedData = time.time()
        print("\tRUNTIME (Nearly Sorted Data): " +
              str(endTime_NearlySortedData - startTime_NearlySortedData) + " Seconds")
        # Few Unique Data (Insertion Sort)
        startTime_FewUniqueData = time.time()
        insertionSort(fewUniqueData)
        endTime_FewUniqueData = time.time()
        print("\tRUNTIME (few Unique Data): " +
              str(endTime_FewUniqueData - startTime_FewUniqueData) + " Seconds")
        print("[Test Finished]\n")
    elif selection == 4:
        os.system('cls')
        loop = False
