

<h2>Network Scanner</h2>
<h3>Goal: Discover clients on a Network:</h3>

<h4>Network Scanner Algorithm:</h4>
<ol>
<li>Create ARP request directed to broadcast MAC asking for IP.
<p>/24 shows clients in the full range</p>
</li>
<li>Send packet and receive result.</li>
<li>Parse the response</li>
<li>Print Result</li>
</ol>

<h4>ISSUE:  ARP requests are logged. </h4>
<h4>Solution (Needs to be implemented)</h4>
<p>import logging</p>
<p>logging.getLogger("scapy").setLevel(logging.CRITICAL)</p>
<p>This ensures Scapy does not print warnings or informational messages.</p>
<p>Use before running scapy functions like sniff() or sent()</p>