Mitmer provides intuitive and error-proof way to intercept and redirect network connections.
It operates on Layer-2 taking care not upset 802.1x-enabled switches.

+ sudo iptables -t mangle -A OUTPUT -o <IFACE> -j DROP
+ sudo sysctl -w net.ipv4.conf.all.rp _ filter=0
+ check the link status, duplex,

~~~~~~~~~~~~~~~~
PM: Port Manager
~~~~~~~~~~~~~~~~

* The purpose of this module is to configure OS and network interfaces used for MITM and
continuously monitor them to make sure they remain in the correct state.
* The names of the network interfaces are specified during the initialization of the module.
* All action taken by the module and identified configuration deviations are logged.


* The user provides two network interface names for use for MITM.
* The system analyzes the configuration of these interfaces, checks
 for conditions which may potentially have an undesired effect.
* When a problem is detected the system runs a corrective action.
* The system displays a list of ports along with information about encountered problems
 and suggestions on how to fix them.
* The user fixes the problems and asks the system to rerun checks.
* The user selects two network interfaces to use for MITM exercise and asks the system
 to start bridging.
* The system starts bridging. The system periodically checks configuration of selected
 network interfaces and reports potential problems to the user.

By default the system acts as a normal L2 bridge between selected network interfaces,
except it will forward all frames, even link-local ones (to pass 802.1x messages).

Options:
* Idle timeout, in seconds (or disabled)
* Hard timeout, in seconds (or disabled)

Step 2: Enable redirection of TCP connections to sslcaudit

When this mode is activated, all TCP connections will be routed to sslcaudit.

Wanted sslcaudit features:
* determine real destination of connection and use it to distinguish between clients
* automatically fetch the certificate of the server from the real connection
* if all tests are done or it is impossible to fetch server certificate, relay traffic transparently


