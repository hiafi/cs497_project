#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project

class Log:
    self.duration        = 0.0       #Length (in seconds) of connection
    self.protocol        = ""        #Protocol name (tcp, udp)
    self.service         = ""        #Service on destination (http, telnet)
    self.flag            = ""        #normal or error status
    self.src_bytes       = 0         #number of bytes from source to destination
    self.dst_bytes       = 0         #number of bytes from destination to source
    self.land            = False     #True if connection is to / from the same host / port
    self.wrong_format    = 0         #number of "wrong" fragments
    self.urgent          = 0         #number of urgent packets
    self.hot             = 0         #number of "hot" indicators
    self.failed_logins   = 0         #number of failed login attempts
    self.logged_in       = False     #true if successfully loged in
    self.compromised     = 0         #number of "compromised" conditions
    self.root_shell      = False     #True if root shell was obtained
    self.su_attempted    = False     #True if "su root" was attempted
    self.roots           = 0         #number of "root" accesses
    self.files_created   = 0         #number of file creation operations
    self.shells          = 0         #number of shell prompts
    self.access_files    = 0         #number of operations on access control files
    self.outbound_cmds   = 0         #number of outbound commands in an ftp session
    self.is_host_login   = False     #True if the login belongs to the host list
    self.is_guest_login  = False     #True if the login is a guest login
    self.conn_count      = 0         #number of connections to the same host in the last 2 seconds
    
    #The following features refer to the same host connections
    self.srv_count           = 0     # number of connections to the same service
                                    #as the current connection in the past 2 secs
    s_error_rate        = 0.0   # % of connections that have SYN errors
    self.srv_s_error_rate    = 0.0   # % of connections that have SYN errors
    self.r_error_rate        = 0.0   # % of connections that have REJ errors
    self.srv_r_error_rate    = 0.0   # % of connections that have REJ errors
    self.same_srv_rate       = 0.0   # % of the connections to the same service
    self.diff_srv_rate       = 0.0   # % of connections to different services
    
    #The following features refer to the same service connections
    self.srv_diff_host_rate  = 0.0   # % of connections to different hosts
    self.dst_host_count              = 0
    self.dst_host_srv_count          = 0
    self.dst_host_same_srv_rate      = 0.0
    self.dst_host_diff_srv_rate      = 0.0
    self.dst_host_same_src_port_rate = 0.0
    self.dst_host_srv_diff_host_rate = 0.0
    self.dst_host_s_error_rate       = 0.0
    self.dst_host_srv_s_error_rate   = 0.0
    self.dst_host_r_error_rate       = 0.0
    self.dst_host_srv_r_error_rate   = 0.0
    self.attack_type                 = ""
