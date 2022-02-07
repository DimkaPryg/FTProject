#!/bin/sh
iptables -A INPUT -i lo -j ACCEPT
# Manage network access (internet, ssh)
iptables -A INPUT -p udp -i enp0s3 -m multiport --dport 53,67 -j ACCEPT
iptables -A INPUT -p tcp -i enp0s3 -m multiport --dport 53,22 -j ACCEPT
#DB, node-exporter forward
iptables -A FORWARD -p tcp -m multiport --dport 5432,9100,9090 -j ACCEPT
iptables -A FORWARD -p tcp -m multiport --sport 5432,9100,9090 -j ACCEPT
# Node-exporter access
iptables -A INPUT -p tcp -i enp0s9 -m multiport --dport 9100 -j ACCEPT
iptables -P INPUT DROP
iptables -P FORWARD DROP