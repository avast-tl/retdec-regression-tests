from regression_tests import *

class busybox(Test):
    settings = TestSettings(
        input='busybox',
        args='-k'
    )

    def test_for_some_functions(self):
        assert self.out_c.has_func( '_init' )
        assert self.out_c.has_func( 'common_exit' )
        assert self.out_c.has_func( 'del_line_matching' )
        assert self.out_c.has_func( 'chomp' )
        assert self.out_c.has_func( 'bb_parse_mode' )
        assert self.out_c.has_func( 'bb_printf' )
        assert self.out_c.has_func( 'cmsMsg_receive' )
        assert self.out_c.has_func( 'cmsMsg_send' )
        assert self.out_c.has_func( '__deregister_frame_info' )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal(r"ignoring all arguments")
        assert self.out_c.has_string_literal(r"?pc?d?b?-?l?s???rwxSTst")
        assert self.out_c.has_string_literal(r"%s: ")
        assert self.out_c.has_string_literal(r"warning: no inet socket available")
        assert self.out_c.has_string_literal(r"/proc/net")
        assert self.out_c.has_string_literal(r"No such user")
        assert self.out_c.has_string_literal(r"getnameinfo failed")
        assert self.out_c.has_string_literal(r"first time, get config file from smd")
        assert self.out_c.has_string_literal(r"myRead")
        assert self.out_c.has_string_literal(r"linuxrc")
        assert self.out_c.has_string_literal(r"getaddrinfo: %s: %d")
        assert self.out_c.has_string_literal(r"-/bin/sh")
        assert self.out_c.has_string_literal(r"pppd")
        assert self.out_c.has_string_literal(r"Cannot %s directory `%s'")
        assert self.out_c.has_string_literal(r"abfnrtv\\")
        assert self.out_c.has_string_literal(r"10baseT")
        assert self.out_c.has_string_literal(r"POINTOPOINT ")
        assert self.out_c.has_string_literal(r"--help")
        assert self.out_c.has_string_literal(r"Image could not fit into %u byte buffer.\n")
        assert self.out_c.has_string_literal(r"ugo")
        assert self.out_c.has_string_literal(r"could not stat '/'")
        assert self.out_c.has_string_literal(r"standard input")
        assert self.out_c.has_string_literal(r"select failed")
        assert self.out_c.has_string_literal(r"10base2")
        assert self.out_c.has_string_literal(r"Unable to read all data")
        assert self.out_c.has_string_literal(r"%s\n\nUsage: busybox [function] [arguments]...\n   or: [function] [arguments]...\n\n\tBusyBox is a multi-call binary that combines many common Unix\n\tutilities into a single executable.  Most people will create a\n\tlink to busybox for each function they wish to use, and BusyBox\n\twill act like whatever it was invoked as.\n\nCurrently defined functions:\n")
        assert self.out_c.has_string_literal(r"busybox")
        assert self.out_c.has_string_literal(r"%-15.15s Link encap:%s  ")
        assert self.out_c.has_string_literal(r"%5d %-5d %6d %s\n")
        assert self.out_c.has_string_literal(r"RX packets:%Lu errors:%lu dropped:%lu overruns:%lu frame:%lu\n")
        assert self.out_c.has_string_literal(r"unknown %cid %ld")
        assert self.out_c.has_string_literal(r"%Lu%Lu%u%u%u%u%n%n%Lu%Lu%u%u%u%u%u")
        assert self.out_c.has_string_literal(r"                collisions:%lu ")
        assert self.out_c.has_string_literal(r"unable to preserve ownership of `%s'")
        assert self.out_c.has_string_literal(r"ALLMULTI ")
        assert self.out_c.has_string_literal(r"%*[^\n]\n")
        assert self.out_c.has_string_literal(r"icmp")
        assert self.out_c.has_string_literal(r"no process killed")
        assert self.out_c.has_string_literal(r"%s: omitting directory")
        assert self.out_c.has_string_literal(r"Put not supported")
        assert self.out_c.has_string_literal(r"%-16s%-16s%-16s%-6s")
        assert self.out_c.has_string_literal(r"Weird! Can't find the terminator token from the beginning??? ")
        assert self.out_c.has_string_literal(r"\n\n")
        assert self.out_c.has_string_literal(r" Bcast:%s ")
        assert self.out_c.has_string_literal(r"RUNNING ")
        assert self.out_c.has_string_literal(r"EXIT")
        assert self.out_c.has_string_literal(r"MULTICAST ")
        assert self.out_c.has_string_literal(r"Tftp Image failed: Illegal image.")
        assert self.out_c.has_string_literal(r": ")
        assert self.out_c.has_string_literal(r"semop[SMwdn]")
        assert self.out_c.has_string_literal(r"can`t create raw socket")
        assert self.out_c.has_string_literal(r"shmat")
        assert self.out_c.has_string_literal(r"/proc/net/if_inet6")
        assert self.out_c.has_string_literal(r"m:")
        assert self.out_c.has_string_literal(r"`%s' and `%s' are the same file")
        assert self.out_c.has_string_literal(r"standard output")
        assert self.out_c.has_string_literal(r"%s: remove directory `%s'? ")
        assert self.out_c.has_string_literal(r"default")
        assert self.out_c.has_string_literal(r"unable to remove `%s'")
        assert self.out_c.has_string_literal(r"memory exhausted")
        assert self.out_c.has_string_literal(r"unable to preserve permissions of `%s'")
        assert self.out_c.has_string_literal(r"%s: descend into directory `%s'? ")
        assert self.out_c.has_string_literal(r"/etc/group")
        assert self.out_c.has_string_literal(r"Memory:%lx-%lx ")
        assert self.out_c.has_string_literal(r"Warning: cannot open %s. Limited output.")
        assert self.out_c.has_string_literal(r"octet")
        assert self.out_c.has_string_literal(r"Complete")
        assert self.out_c.has_string_literal(r"%s%s")
        assert self.out_c.has_string_literal(r"Get not supported")
        assert self.out_c.has_string_literal(r"%s: remove `%s'? ")
        assert self.out_c.has_string_literal(r"Error_CannotResolveHostName")
        assert self.out_c.has_string_literal(r"/dev/root")
        assert self.out_c.has_string_literal(r"Weird! Can't find the terminator token??? ")
        assert self.out_c.has_string_literal(r"permission denied. (are you root?)")
        assert self.out_c.has_string_literal(r"sendEventMessage")
        assert self.out_c.has_string_literal(r"BROADCAST ")
        assert self.out_c.has_string_literal(r"/proc")
        assert self.out_c.has_string_literal(r"/proc/net/dev")
        assert self.out_c.has_string_literal(r"%s\n\nUsage: %s %s\n\n")
        assert self.out_c.has_string_literal(r"%Lu%Lu%u%u%u%u%u%u%Lu%Lu%u%u%u%u%u%u")
        assert self.out_c.has_string_literal(r"Disk full or allocation exceeded")
        assert self.out_c.has_string_literal(r"bb_xasprintf")
        assert self.out_c.has_string_literal(r"NOTRAILERS ")
        assert self.out_c.has_string_literal(r"compressed:%lu ")
        assert self.out_c.has_string_literal(r"Access violation")
        assert self.out_c.has_string_literal(r"100baseFX")
        assert self.out_c.has_string_literal(r"`%s' is not a directory")
        assert self.out_c.has_string_literal(r"             compressed:%lu\n")
        assert self.out_c.has_string_literal(r"Buffer already allocated just grab the semaphore?")
        assert self.out_c.has_string_literal(r"DMA chan:%x ")
        assert self.out_c.has_string_literal(r"Undefined error code")
        assert self.out_c.has_string_literal(r"%63s%lx%lx%X%d%d%d%lx%d%d%d\n")
        assert self.out_c.has_string_literal(r"LOOPBACK ")
        assert self.out_c.has_string_literal(r"%d bytes allocated for image\n")
        assert self.out_c.has_string_literal(r"handler_sigterm")
        assert self.out_c.has_string_literal(r"TMOUT")
        assert self.out_c.has_string_literal(r"Unknown transfer ID")
        assert self.out_c.has_string_literal(r" P-t-P:%s ")
        assert self.out_c.has_string_literal(r"TX packets:%Lu errors:%lu dropped:%lu overruns:%lu carrier:%lu\n")
        assert self.out_c.has_string_literal(r"tftpd_receive")
        assert self.out_c.has_string_literal(r"augo")
        assert self.out_c.has_string_literal(r"File not found")
        assert self.out_c.has_string_literal(r"received signal %d")
        assert self.out_c.has_string_literal(r"[NO FLAGS] ")
        assert self.out_c.has_string_literal(r"/proc/net/route")
        assert self.out_c.has_string_literal(r"tftpd_ack send")
        assert self.out_c.has_string_literal(r"HUP")
        assert self.out_c.has_string_literal(r"UP ")
        assert self.out_c.has_string_literal(r"%s")
        assert self.out_c.has_string_literal(r"unknown")
        assert self.out_c.has_string_literal(r" Mask:%s\n")
        assert self.out_c.has_string_literal(r"txqueuelen:%d ")
        assert self.out_c.has_string_literal(r"internal error: unrecognized file type")
        assert self.out_c.has_string_literal(r"100baseT")
        assert self.out_c.has_string_literal(r"rwxSTst")
        assert self.out_c.has_string_literal(r"DEBUG ")
        assert self.out_c.has_string_literal(r"AUI")
        assert self.out_c.has_string_literal(r"[UNKNOWN]")
        assert self.out_c.has_string_literal(r"[NONE SET]")
        assert self.out_c.has_string_literal(r"Device not found")
        assert self.out_c.has_string_literal(r"/etc/passwd")
        assert self.out_c.has_string_literal(r"  T")
        assert self.out_c.has_string_literal(r"Not enough memory error.  Could not allocate %u bytes.")
        assert self.out_c.has_string_literal(r"%-6d %-2d %7d %s\n")
        assert self.out_c.has_string_literal(r"shmget")
        assert self.out_c.has_string_literal(r"\n                R")
        assert self.out_c.has_string_literal(r"Illegal TFTP operation")
        assert self.out_c.has_string_literal(r"NOARP ")
        assert self.out_c.has_string_literal(r"rwxXst")
        assert self.out_c.has_string_literal(r"semget")
        assert self.out_c.has_string_literal(r"cannot get system information")
        assert self.out_c.has_string_literal(r"%s: error fetching interface information: %s\n")
        assert self.out_c.has_string_literal(r"fatal: %s\n")
        assert self.out_c.has_string_literal(r"SIG")
        assert self.out_c.has_string_literal(r"X bytes:%Lu (%Lu.%u %sB)%s")
        assert self.out_c.has_string_literal(r"Can't open /proc")
        assert self.out_c.has_string_literal(r"Memory allocated")
        assert self.out_c.has_string_literal(r"                %s addr:%s ")
        assert self.out_c.has_string_literal(r"No usable address families found.")
        assert self.out_c.has_string_literal(r"Interrupt:%d ")
        assert self.out_c.has_string_literal(r"MASTER ")
        assert self.out_c.has_string_literal(r", ")
        assert self.out_c.has_string_literal(r"create")
        assert self.out_c.has_string_literal(r"%s%s%s")
        assert self.out_c.has_string_literal(r"socket")
        #assert self.out_c.has_string_literal(r"getcwd()")
        assert self.out_c.has_string_literal(r"%s%s\n")
        assert self.out_c.has_string_literal(r"applet not found")
        assert self.out_c.has_string_literal(r"Failure to negotiate RFC2347 options")
        assert self.out_c.has_string_literal(r"ipv6-icmp")
        assert self.out_c.has_string_literal(r"unable to stat `%s'")
        assert self.out_c.has_string_literal(r"Unable to connect to remote host (%s)")
        assert self.out_c.has_string_literal(r"bb_xstrndup bug")
        assert self.out_c.has_string_literal(r"init")
        assert self.out_c.has_string_literal(r",\n")
        assert self.out_c.has_string_literal(r"fscanf")
        assert self.out_c.has_string_literal(r"%n%Lu%u%u%u%u%n%n%n%Lu%u%u%u%u%u")
        assert self.out_c.has_string_literal(r"Ping_InProgress")
        assert self.out_c.has_string_literal(r"GHRDMDAC")
        assert self.out_c.has_string_literal(r"(auto)")
        assert self.out_c.has_string_literal(r"%ld")
        assert self.out_c.has_string_literal(r"PROMISC ")
        assert self.out_c.has_string_literal(r"unable to open `%s'")
        assert self.out_c.has_string_literal(r"Media:%s")
        assert self.out_c.has_string_literal(r"Exiting Syslogd!")
        assert self.out_c.has_string_literal(r"SLAVE ")
        assert self.out_c.has_string_literal(r"File already exists")
        assert self.out_c.has_string_literal(r"/dev")
        assert self.out_c.has_string_literal(r"%s\n\nNo help available.\n\n")
        assert self.out_c.has_string_literal(r"HWaddr %s  ")
        assert self.out_c.has_string_literal(r"Base address:0x%lx ")
        assert self.out_c.has_string_literal(r"%s: is a directory")
        assert self.out_c.has_string_literal(r"100baseTX")
        assert self.out_c.has_string_literal(r"urrently defined functions:\n")
        assert self.out_c.has_string_literal(r"\n%s:")

class libndmComponents(Test):
    settings = TestSettings(
        input='libndmComponents.so',
        args='-k'
    )

    def test_for_some_functions(self):
        assert self.out_c.has_func( '_ftext' ) # entry_point
        assert self.out_c.has_func( '_ZNK7Command7RequestixERK7CString' )
        assert self.out_c.has_func( '_ZN4HTTP2IO8DirectFd8WriteAllEPKvj' )
        assert self.out_c.has_func( '_ZN3Xml8Document12AllocateNodeENS_4Node5TypeTERK7CStringS5_' )
        assert self.out_c.has_func( '_ZN4HTTP2IO8DirectFd7ReadAllEPvj' )
        assert self.out_c.has_func( '_ZN5Event8ProgressC1ERK7CStringm7RebootT' )
        assert self.out_c.has_func( '_ZN6Thread9SetStatusEP6Status' )
        assert self.out_c.has_func( '_ZN9StatusLogC1E7ReturnTN3Log6LevelTEPKcS4_P6Status' )
        assert self.out_c.has_func( '_ZNK3Xml4Node9FirstNodeERK7CString' )
        assert self.out_c.has_func( '_ZNK7Command4Base12ConfiguratorEv' )
        assert self.out_c.has_func( '_ZNK9StringMap4SizeEv' )

class x86_elf_60b7c56f174faf4b617af4d724fda88d(Test):
    settings = TestSettings(
        input='x86-elf-60b7c56f174faf4b617af4d724fda88d',
        args='-k'
    )

    def test_for_all_functions(self):
        assert self.out_c.has_func( 'function_8048074' )
        assert self.out_c.has_func( 'entry_point' )
        assert self.out_c.has_func( 'function_8048115' )
        assert self.out_c.has_func( 'function_8048122' )
        assert self.out_c.has_func( 'function_8048185' )
