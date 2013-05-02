from csv import reader
import Log
    
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
                #declare a Log called dataForRow
                dataForRow = Log.Log()

                #now, here is the "constructor"
                dataForRow.duration = float(row[0])
                dataForRow.protocol = row[1]
                dataForRow.service = row[2]
                dataForRow.flag = row[3]
                dataForRow.src_bytes = int(row[4])
                dataForRow.dst_bytes = int(row[5])
                dataForRow.land = bool(row[6])
                dataForRow.wrong_format = int(row[7])
                dataForRow.urgent = int(row[8])
                dataForRow.hot = int(row[9])
                dataForRow.failed_logins = int(row[10])
                dataForRow.logged_in = bool(row[11])
                dataForRow.compromised = int(row[12])
                dataForRow.root_shell = bool(row[13])
                dataForRow.su_attempted = bool(row[14])
                dataForRow.roots = int(row[15])
                dataForRow.files_created = int(row[16])
                dataForRow.shells = int(row[17])
                dataForRow.access_files = int(row[18])
                dataForRow.outbound_cmds = int(row[19])
                dataForRow.is_host_login = bool(row[20])
                dataForRow.is_guest_login = bool(row[21])
                dataForRow.conn_count = int(row[22])
                dataForRow.srv_count = int(row[23])
                dataForRow.s_error_rate = float(row[24])
                dataForRow.srv_s_error_rate = float(row[25])
                dataForRow.r_error_rate = float(row[26])
                dataForRow.srv_r_error_rate = float(row[27])
                dataForRow.same_srv_rate = float(row[28])
                dataForRow.diff_srv_rate = float(row[29])
                dataForRow.srv_diff_host_rate = float(row[30])
                dataForRow.dst_host_count = int(row[31])
                dataForRow.dst_host_srv_count = int(row[32])
                dataForRow.dst_host_same_srv_rate = float(row[33])
                dataForRow.dst_host_diff_srv_rate = float(row[34])
                dataForRow.dst_host_same_src_port_rate = float(row[35])
                dataForRow.dst_host_srv_diff_host_rate = float(row[36])
                dataForRow.dst_host_s_error_rate = float(row[37])
                dataForRow.dst_host_srv_s_error_rate = float(row[38])
                dataForRow.dst_host_r_error_rate = float(row[39])
                dataForRow.dst_host_srv_r_error_rate = float(row[40])

                #an if/else statement that checks whether it is training data
                #or test data that is being parsed based on the length of row
                if len(row) < 42:
                    #if the length of row is less than 42, then a dummy action
                    #is performed
                    dummyAction = 0
                else:
                    #else, the 42nd item in row (which has an index of 41 due to
                    #the fact that the 1st item has an index of 0) is parsed into
                    #the attack_type field
                    dataForRow.attack_type = row[41]

                #now, append the dataForRow list into the listOfData list
                listOfData.append(dataForRow)

        #once all the parsing is done, we can return the list of data
        return listOfData

if __name__ == 'main':
    fileName = "Dataset/kddcup.data_10_percent"
    dataSet = []
    dataSet = parseDataFile(fileName)
