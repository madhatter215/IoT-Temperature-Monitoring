# IoT-Temperature-Monitoring

I used instructions from Intel to install the Yocto binary image onto my Galileo Gen 2
xdk-daemon-0.0.38-ia32-node-0.10.x.tar

With the Grove sensor (v2) I noticed the MRAA package has the wrong resistor value so I created my own function to get temperature. 

Theory of Operation: 
=======================
On the client side (Galileo), by running udp_test.py, the client with sample the ambient temperature value and send a message (UDP packet) to the server. 

On the server side, by running udp_test_listening.py, a socket is created and listening on port 5005 for any incomming UDP packets. Once a packet has arrived over the network, the program stuffs the contents into a text file (for now, later a database such as MongoDB) for analysis later. 

On the server backend, I created a webhost running Apache and setup my configuration to tell the http daemon that any *.py file inside the directoty cgi-bin should call python interpreter. When a user goes to my webpage, the python scripts run to generate HTML and fill in the values (by parsing the text file with timestamp and temperature value) for graph display. 

The javascript for the graphs came from open source (google charts, see https://developers.google.com/chart/). 
