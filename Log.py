#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
class Log:
    duration        = 0.0       #Length (in seconds) of connection
    protocol        = ""        #Protocol name (tcp, udp)
    service         = ""        #Service on destination (http, telnet)
    flag            = ""        #normal or error status
    src_bytes       = 0         #number of bytes from source to destination
    dst_bytes       = 0         #number of bytes from destination to source
    land            = False     #True if connection is to/from the same host/port
    wrong_format    = 0         #number of "wrong" fragments
    urgent          = 0         #number of urgent packets
    hot             = 0         #number of "hot" indicators
    failed_logins   = 0         #number of failed login attempts
    logged_in       = False     #true if successfully loged in
    compromised     = 0         #number of "compromised" conditions
    root_shell      = False     #True if root shell was obtained
    su_attempted    = False     #True if "su root" was attempted
    roots           = 0         #number of "root" accesses
    files_created   = 0         #number of file creation operations
    shells          = 0         #number of shell prompts
    access_files    = 0         #number of operations on access control files
    outbound_cmds   = 0         #number of outbound commands in an ftp session
    is_host_login   = False     #True if the login belongs to the host list
    is_guest_login  = False     #True if the login is a guest login
    conn_count      = 0         #Number of connections to the same host in the 
                                #last 2 seconds

    #The following features refer to the same host connections
    srv_count           = 0     # number of connections to the same service
                                 #as the current connection in the past 2 secs
    s_error_rate        = 0.0   # % of connections that have SYN errors
    srv_s_error_rate    = 0.0   # % of connections that have SYN errors
    r_error_rate        = 0.0   # % of connections that have REJ errors
    srv_r_error_rate    = 0.0   # % of connections that have REJ errors
    same_srv_rate       = 0.0   # % of the connections to the same service
    diff_srv_rate       = 0.0   # % of connections to different services

    #The following features refer to the same service connections
    srv_diff_host_rate          = 0.0   # % of connections to different hosts
    dst_host_count              = 0
    dst_host_srv_count          = 0
    dst_host_same_srv_rate      = 0.0
    dst_host_diff_srv_rate      = 0.0
    dst_host_same_src_port_rate = 0.0
    dst_host_srv_diff_host_rate = 0.0
    dst_host_s_error_rate       = 0.0
    dst_host_srv_s_error_rate   = 0.0
    dst_host_r_error_rate       = 0.0
    dst_host_srv_r_error_rate   = 0.0
    attack_type                 = ""

    #--------------------------------------------------------------------------
    def __init__(self, row):
        self.duration                       = float(row[0])
        self.protocol                       = row[1]
        self.service                        = row[2]
        self.flag                           = row[3]
        self.src_bytes                      = int(row[4])
        self.dst_bytes                      = int(row[5])
        self.land                           = bool(row[6])
        self.wrong_format                   = int(row[7])
        self.urgent                         = int(row[8])
        self.hot                            = int(row[9])
        self.failed_logins                  = int(row[10])
        self.logged_in                      = bool(row[11])
        self.compromised                    = int(row[12])
        self.root_shell                     = bool(row[13])
        self.su_attempted                   = bool(row[14])
        self.roots                          = int(row[15])
        self.files_created                  = int(row[16])
        self.shells                         = int(row[17])
        self.access_files                   = int(row[18])
        self.outbound_cmds                  = int(row[19])
        self.is_host_login                  = bool(row[20])
        self.is_guest_login                 = bool(row[21])
        self.conn_count                     = int(row[22])
        self.srv_count                      = int(row[23])
        self.s_error_rate                   = float(row[24])
        self.srv_s_error_rate               = float(row[25])
        self.r_error_rate                   = float(row[26])
        self.srv_r_error_rate               = float(row[27])
        self.same_srv_rate                  = float(row[28])
        self.diff_srv_rate                  = float(row[29])
        self.srv_diff_host_rate             = float(row[30])
        self.dst_host_count                 = int(row[31])
        self.dst_host_srv_count             = int(row[32])
        self.dst_host_same_srv_rate         = float(row[33])
        self.dst_host_diff_srv_rate         = float(row[34])
        self.dst_host_same_src_port_rate    = float(row[35])
        self.dst_host_srv_diff_host_rate    = float(row[36])
        self.dst_host_s_error_rate          = float(row[37])
        self.dst_host_srv_s_error_rate      = float(row[38])
        self.dst_host_r_error_rate          = float(row[39])
        self.dst_host_srv_r_error_rate      = float(row[40]) 

        #Check if data is identified.
        if len(row) >= 42:
            self.attack_type = row[41] 
