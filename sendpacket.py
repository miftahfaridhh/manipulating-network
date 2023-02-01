#! /usr/bin/env python

from scapy.all import send, IP, ICMP

send(IP(src="10.0.99.100",dst="10.1.99.100")/ICMP()/"Hello World")