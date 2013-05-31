#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------

attack_types = ['normal', 'buffer_overflow', 'ftp_write', 'back', 
'guess_passwd', 'imap', 'ipsweep', 'land', 'loadmodule', 'multihop',
'neptune', 'nmap', 'perl' 'phf', 'pod', 'portsweep', 'rootkit', 'satan', 
'smurf', 'spy', 'teardrop', 'warezclient', 'warezmaster']

protocol_type = {'tcp': 1, 'udp': 2, 'icmp': 3}

service_type = {'IRC': 31,
 'X11': 61,
 'Z39_50': 57,
 'auth': 5,
 'bgp': 56,
 'courier': 37,
 'csnet_ns': 47,
 'ctf': 28,
 'daytime': 27,
 'discard': 42,
 'domain': 24,
 'domain_u': 4,
 'echo': 41,
 'eco_i': 8,
 'ecr_i': 10,
 'efs': 36,
 'exec': 34,
 'finger': 3,
 'ftp': 7,
 'ftp_data': 14,
 'gopher': 20,
 'hostnames': 46,
 'http': 1,
 'http_443': 33,
 'imap4': 26,
 'iso_tsap': 45,
 'klogin': 39,
 'kshell': 40,
 'ldap': 58,
 'link': 18,
 'login': 25,
 'mtp': 17,
 'name': 22,
 'netbios_dgm': 53,
 'netbios_ns': 51,
 'netbios_ssn': 52,
 'netstat': 59,
 'nnsp': 32,
 'nntp': 29,
 'ntp_u': 9,
 'other': 11,
 'pm_dump': 63,
 'pop_2': 48,
 'pop_3': 13,
 'printer': 35,
 'private': 12,
 'red_i': 66,
 'remote_job': 19,
 'rje': 15,
 'shell': 30,
 'smtp': 2,
 'sql_net': 54,
 'ssh': 21,
 'sunrpc': 49,
 'supdup': 44,
 'systat': 43,
 'telnet': 6,
 'tftp_u': 64,
 'tim_i': 65,
 'time': 16,
 'urh_i': 60,
 'urp_i': 62,
 'uucp': 38,
 'uucp_path': 50,
 'vmnet': 55,
 'whois': 23}

flags = {'OTH': 10,
 'REJ': 3,
 'RSTO': 7,
 'RSTOS0': 9,
 'RSTR': 8,
 'S0': 5,
 'S1': 2,
 'S2': 4,
 'S3': 6,
 'SF': 1,
 'SH': 11}

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
        if len(row) >= 41:
            self.attack_type = row[41][:-1]
            #A problem with the CSV, it has a . after the name, so skip

    #--------------------------------------------------------------------------
    def get_coords(self):
        """
            Returns all dataset as a coordinate.  Note that the return coords
            will alwys be the same order but not necessarily in the order of
            the init.
        """
        return [value[1] for value in self.__dict__.iteritems()]

    def get_discrete_value(self, attr):
        if attr == "protocol":
            return protocol_type[self.protocol]
        elif attr == "service":
            return service_type[self.service]
        elif attr == "flag":
            return flags[self.flag]
        else:
            return getattr(self, attr, 0)

