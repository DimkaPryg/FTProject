#!/bin/sh
iptables -A INPUT -i lo -j ACCEPT
# External access
iptables -A INPUT -p tcp -i enp0s3 -m multiport --dport 25,80,443 -j ACCEPT
# Node-exporter access
iptables -A INPUT -p tcp -i enp0s8 -m tcp --dport 9100 -j ACCEPT
# Manage network access
iptables -A INPUT -p udp -i enp0s9 -m multiport --dport 53,67 -j ACCEPT
iptables -A INPUT -p tcp -i enp0s9 -m multiport --dport 53,22,3000 -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -P INPUT DROP