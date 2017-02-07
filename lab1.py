# +-------------------------------------------------------------------------------+
# |
# | Filename:              lab1.py
# |
# | Student Developer:     Christian Turner
# |
# | Course:                University of San Francisco
# |                        HS 611
# |                        Professor Atterbury
# |                        Spring 2017
# |
# | Assignment:            HS 611:  Lab 1
# |
# | Date:                  February 5, 2017
# |
# +-------------------------------------------------------------------------------+
# |
# | Abstract:  This Python program converts data to JSON and XML formats.
# |            Additionally, this program adds the extra credit as well.  All
# |            requirements are defined in the README.md within Github
# |            specific to usf-hs-611 / turnercd2-lab-xml-json
# |
# +-------------------------------------------------------------------------------+

"""This script converts a CSV file with headers to XML or JSON, depending on
the command line argument supplied.

This script will be executed by calling:

    ```
    python src/lab1.py xml/json <filename>
    ```

Output of XML and JSON should be printed to stdout.
"""

# Use argparse or argv to parse command line arguments.

import argparse  # https://docs.python.org/2/library/argparse.html
from sys import argv  #https://docs.python.org/2/library/sys.html#sys.argv
import csv
import xml
import json
import string
import sys

def parse_csv(filename):
    """Parse a CSV file by separating it into headers and additional data.

    Parameters
    ----------
    filename : str
        A path to a CSV file.

    Returns
    -------
    (list, list)
        A tuple containing two lists: 
        
        1. The first list should contain the headers from the CSV file. If
           the headers are "first_name, last_name, dob" then this will be
           ["first_name", "last_name", "dob"].
        2. The second list should contain the data in the CSV file as a
           list of lists. For example, if there are two rows in the CSV
           file "1, 2, 3," and "4, 5, 6" then this list would look like
           [[1, 2, 3], [4, 5, 6]].
    """
    inFile = open(filename)
    csvFile = csv.reader(inFile)

    # read in the first row of the csv file

    csvHeader = next(csvFile)

    # create list and read in rows 2 through n

    csvData = []

    for row in csvFile:
        csvData.append(row)

    return csvHeader, csvData

def build_and_display_xml(list1, list2):

    # Hard coded values that are allowed per lecture on 2/2/2017

    outterElementOpen = "<records>\n"
    outterElementClose = "</records>\n"
    innerElementOpen = " <patient>\n"
    innerElementClose = " </patient>\n"

    # Setting up resultant string

    xmlString = ""
    xmlString += outterElementOpen

    # Outter and inner loops to iterate through the list values

    for rowData in list2:

        xmlString += innerElementOpen
        i = 0

        for columnData in list1:
            tempElement = "   <" + columnData + ">" +rowData[i]+ "</" + columnData + ">\n"
            xmlString += tempElement
            i += 1

        xmlString += innerElementClose

    xmlString += outterElementClose

    # Displaying data to stdout per development requirements

    sys.stdout.write(xmlString)

    return

def build_and_display_json(list1, list2):

    # Hard coded values that are allowed per lecture on 2/2/2017

    outterResource = "{  \"records\":[\n"
    innerResource = "     \"patient\":{\n"

    # Other syntax specific punctuation

    outterCurleyLeftBrace = "   {\n"
    innerCurleyRightBrace = "     }\n"
    outterCurleyRightBraceComma = "   },\n"
    outterCurleyRightBraceNoComma = "   }\n"
    outterRightBracket = " ]\n"
    termLeftCurleyBracket = "}\n"

    # Setting up resultant string

    jsonString = ""
    jsonString += outterResource
    jsonString += outterCurleyLeftBrace

    # Outter and inner loops to iterate through the list values

    j = 0
    for rowData in list2:

        jsonString += innerResource
        i = 0

        for columnData in list1:
            tempElement = "       \"" + columnData + "\":\"" + rowData[i] + "\"\n"
            jsonString += tempElement
            i += 1

        jsonString += innerCurleyRightBrace

        j += 1
        if (j != len(list2)):
            jsonString += outterCurleyRightBraceComma
            jsonString += outterCurleyLeftBrace

    jsonString += outterCurleyRightBraceNoComma
    jsonString += outterRightBracket
    jsonString += termLeftCurleyBracket

    # Displaying data to stdout per development requirements

    sys.stdout.write(jsonString)

    return

def readin_json(filename):

    jsonFile = open(filename, "r")

    jsonFileText = jsonFile.read()

    return jsonFileText

def json_to_xml(jsonFileText):

    jsonData = json.loads(jsonFileText)


    print

    return

# main

if __name__ == "__main__":
    # Parse command line arguments to convert CSV to either XML or JSON.

    validConversionFlag = False
    validCSVextension = False

    # upper casing the argv values for consistency

    typeConversion = argv[1].upper()
    filename = argv[2].upper()

    # checking for valid conversion types

    if (typeConversion == "JSON" or typeConversion == "XML"):
        validConversionFlag = True

    # checking for valid file extensions (*.CSV and *.JSON)  The *.JSON extension test is for the
    # extra credit module of this assignment

    csvExtension = ".CSV"
    validCSVextension = False

    csvLoc = filename.find(csvExtension)
    if csvLoc > -1:
        validCSVextension = True

    jsonExtension = ".JSON"
    validJSONextension = False

    jsonLoc = filename.find(jsonExtension)
    if jsonLoc > -1:
        validJSONextension = True

    # given the different permutations, call specific task for conversion

    if (validConversionFlag and typeConversion == "JSON" and validCSVextension):
        # .csv to json conversion
        list1, list2 = parse_csv(filename)
        build_and_display_json(list1, list2)

    if (validConversionFlag and typeConversion == "XML" and validCSVextension):
        # .csv to xml conversion
        list1, list2 = parse_csv(filename)
        build_and_display_xml(list1, list2)

    if (validConversionFlag and typeConversion == "XML" and validJSONextension):
        jsonData = readin_json(filename)
        json_to_xml(jsonData)


    # at this time, all invalid permutations should fall though
