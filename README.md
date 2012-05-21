Mitmer provides intuitive and error-proof way to intercept and redirect network connections.
It operates on Layer-2 taking care not upset 802.1x-enabled switches.
It provides:

Step 1: Port configuration

* The system analyzes the configuration of all available network interfaces and checks
 for conditions which may potentially have an undesired effect on MITM exercise.
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

# Additional sslcaudit features:
# 1) determine real destination of connection and use it to distinguish between clients
# 2) automatically fetch the certificate of the server from the real connection
# 3) if all tests are done or it is impossible to fetch server certificate, relay traffic transparently
