#!/bin/sh
iptables -A INPUT -i lo -j ACCEPT
# Manage network access (internet, ssh)
iptables -A INPUT -p udp -i enp0s3 -m multiport --dport 53,67 -j ACCEPT
iptables -A INPUT -p tcp -i enp0s3 -m multiport --dport 53,22,5432 -j ACCEPT
# DB, node-exporter access
iptables -A INPUT -p tcp -i enp0s8 -m multiport --dport 5432,9100,9090 -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -P INPUT DROP