from csv import reader
from log import Log
    
#define parsing function
def parseDataFile(dataFile):
    with open(dataFile, 'rb') as f:
        dataFromFile = csv.reader(f)
        listOfData = [] #initializes list that the data will be parsed into

        #commence parsing
        for row in dataFromFile:
            if row == []:
                #if the row is empty, do absolutely nothing
                #this way, we can parse the file as-is, without having to
                #go into an editor and remove the blank rows manually
                dummyAction = 0
            else:
                #initialize list for the specific row of data
                #each row will be its own list
                #listOfData overall will be a list of lists
                dataForRow = []

                #another for loop that goes through each entry in the row
                #and appends it into dataForRow
                #note, however, that ALL entries will be treated as strings
                for dataEntry in row:
                    dataForRow.append(dataEntry)

                #now, append the dataForRow list into the listOfData list
                listOfData.append(dataForRow)

        #once all the parsing is done, we can return the list of data
        return listOfData

def main():
    """Main entry into the program"""
    #TODO: Do parsing, then interpeting
    print "Now Running"



if __name__ == "__main__":
    main()
