

<h2>Network Scanner</h2>
<h3>Goal: Discover all clients on the same Network:</h3>
<h4>This script requires root privileges.</h4>

<p>Run ifconfig locally and select the ip you want to test range for</p>
<p></p>

<p>To run the script please provide arguments in the following format. 
From the command line, inside the "Change_Mac" Project Folder, run.</p>
<h3>
python[#] network_scanner.py -i [IPRANGE] [IPRANGE/SUBNET]
</h3>
<p>
eg, $ python network_scanner.py -i 192.168.1.254/24 
</p>
<p>
OR, $ python network_scanner.py --iprange 192.168.1.254/24 
</p>

<h4>Network Scanner Algorithm:</h4>
<ol>
<li>Create ARP request directed to broadcast MAC asking for IP.
<p>/24 shows clients in the full range</p>
</li>
<li>Send packet and receive result.</li>
<li>Parse the response</li>
<li>Print Result</li>
</ol>

<h4>Script Versions</h4>
<p>There are three versions of the script</p>
<ol>
<li>utils: contains separate functions, executed in network_scanner.py, to 
demonstrate the relationships, and reduce a single outcome to a functional components. </li>
<li>network_scanner_single_function: what it says on the box</li>
<li>network_scanner_uncommented: the bare bones, what you should use if 
you want to make this script part of your project.</li>
</ol>

<h4>ISSUE 1:  This script has to be run by sudo. </h4>
<h4>Because srp makes socket access requests only a root user can do</h4>
<p>$ sudo python(#) network_scanner.py </p>
<h4>SOLUTION: Introduced code snippet to cancel script if sudo is not used. </h4>

<h4>ISSUE 2:  ARP requests are logged. </h4>
<h4>Solution (Needs to be implemented)</h4>
<p>import logging</p>
<p>logging.getLogger("scapy").setLevel(logging.CRITICAL)</p>
<p>## This ensures Scapy does not print warnings or informational messages.</p>
<p>Use before running scapy functions like sniff() or sent() ##</p>

<h3>Python Dictionaries</h3>
<p>Are JavaScript JSON </p>