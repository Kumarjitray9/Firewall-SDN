#!/usr/bin/python


"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

MAC,IP, Controller, CLI stuff configured

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', mac="00:00:00:00:00:11", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:12", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:13", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:14", ip="192.168.1.4/24")
        h5 = self.addHost('h5', mac="00:00:00:00:00:15", ip="192.168.1.5/24")
        h6 = self.addHost('h6', mac="00:00:00:00:00:16", ip="192.168.1.6/24")

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)
        self.addLink(h5, s1)
        self.addLink(h6, s1)


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #net.pingAll()
    CLI(net)
    #net.stop()