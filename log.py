
class Log:
    duration        = 0.0       #Length (in seconds) of connection
    protocol        = ""        #Protocol name (tcp, udp)
    service         = ""        #Service on destination (http, telnet)
    flag            = ""        #normal or error status
    src_bytes       = 0         #number of bytes from source to destination
    dst_bytes       = 0         #number of bytes from destination to source
    land            = False     #True if connection is to / from the same host / port
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
    is_host_login    = False     #True if the login belongs to the host list
    is_guest_login  = False     #True if the login is a guest login
    
    conn_count          = 0     # number of connections to the same host in the last 2 seconds
    
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
    srv_diff_host_rate  = 0.0   # % of connections to different hosts  
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

