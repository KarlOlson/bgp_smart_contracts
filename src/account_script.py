#!/usr/bin/python3.8                                                                                            Proxy_c>
#To Run:
#Install scapy: $sudo pip install scapy
#Run Proxy Sniffer $sudo python3.8 <filename.py>
#Must run from sudo for packet processing privileges.

from Classes.Account import Account
from Utils.Utils import *
from ipaddress import IPv4Address
import os, sys

def cycle (contract_file):

    with open(r"accounts.txt", 'r') as fp:
    
        asn_numbers=[5,7] #Enter the ASNs you want to have running the blockchain and proxy code
        lines =[]
    
        for i, line in enumerate(fp):
            if i in asn_numbers:
                account=line.split(' ')
                os.system('python3 add_asn.py ACCOUNT0 '+ 'ACCOUNT'+str(int(account[0])+1)+' '+ str(account[0])+' '+str(account[1]))
                print('python3 add_asn.py ACCOUNT0 '+ 'ACCOUNT'+str(int(account[0])+1)+' '+ str(account[0])+' '+str(account[1]))  #add asn to smart contract #python add_asn.py <account0> <account1> <ASN1> <account1_address>
                os.system('python3 add_prefix.py ACCOUNT0 '+ 'ACCOUNT'+str(int(account[0])+1)+' '+ str(account[0])+' '+'10.'+str(account[0])+'.0.0'+' 24 '+str(account[1]))
                print('python3 add_prefix.py ACCOUNT0 '+ 'ACCOUNT'+str(int(account[0])+1)+' '+ str(account[0])+' '+'10.'+str(account[0])+'.0.0'+' 24 '+str(account[1]))  #add prefix to smart contract #python add_prefix.py <account0> <account1> <ASN1> <ip1> <subnet1> <account1_address>
            elif i > 7: #enter ASN where to stop so it doesn't keep running
            # don't read after line 7 to save time
                break
	
		
if __name__=='__main__':
    print("generating ASN Accounts on Chain")
    cycle(open('accounts.txt'))   		

#python add_asn.py <account0> <account1> <ASN1> <account1_address>
#python add_prefix.py <account0> <account1> <ASN1> <ip1> <subnet1> <account1_address>