from netaddr import *
import pprint
import argparse

parser = argparse.ArgumentParser(description = 'Display IPv4 subnet details')
parser.add_argument('network', help='starting network with CIDR suffix')
parser.add_argument('--hosts', help='list individual host addresses', action='store_true')
parser.add_argument('--bits', help='display binary notation', action='store_true')
args = parser.parse_args()




def displaySubnet(name, subnet):

    print "----------------------------------"
    print 'name %s network %s' %(name, subnet)
    print "----------------------------------"

    block_size = subnet.size
    network = subnet.network
    netmask = subnet.netmask
    broadcast = subnet.broadcast

    network_bits = ''
    if (args.bits):
        network_bits = network.bits()

    netmask_bits = ''
    if (args.bits):
        netmask_bits = netmask.bits()

    broadcast_bits = ''
    if (args.bits):
    	broadcast_bits = broadcast.bits()

    print 'block size\t%s' %(block_size)
    print 'netmask\t\t%s\t\t%s' %(netmask, netmask_bits)
    print 'network\t\t%s\t\t%s' %(network, network_bits)

    if args.hosts:
        for ip in subnet.iter_hosts():
            print '\t\t%s' %ip
    else:
        print 'first host\t%s' %(network + 1)
        print 'last host\t%s' %(broadcast - 1)

    print 'broadcast\t%s\t\t%s' %(subnet.broadcast, broadcast_bits)
    print 'next network\t%s' %(subnet.network + subnet.size)

#print 'network is %s' %args.network
#print '--hosts is %s' %args.hosts
network = IPNetwork(args.network)
displaySubnet('test', network)

if __name__ == '__main__':
	pass
    #this_subnet = IPNetwork('150.75.4.128/28')
    #displaySubnet('sol', this_subnet)
