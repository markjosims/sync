'''
HTTP Protocols:
	* client - entity that requests info
	* server - entity that provides info
	* protocols
		** TCP
			- two-way byte-steam
			- looks like a file
			- like a phone call
			- slow but robust
		** UDP
			- transferred in unreliable chunks
			- can be lost or arrive out of order
			- like surface mail
			- faster but less robust
		** IP
			- like postal addresses
			- can route messages to all destinations in internet
			- multiple applications from the same machine use different ports
				e.g. 123.32.43.1:8080 - 8080 is a port for IP address 123.32.43
			- IP address 127.0.0.1 is 'localhost'
		** HTTP (hypertext transfer protocol)
			- client tells servers what they want using an HTTP method
			- e.g. 'GET' and 'POST' (PUT, HEAD, DELETE, PATCH, OPTIONS)
			- four operations of data-driven website : 'create', 'read', 'update', 'delete'
'''