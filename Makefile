.PHONY: install pox mn mn_clean

install:
	git clone http://github.com/noxrepo/pox
	cd pox; git checkout dart
	mv firewall.py pox/ext/

pox:
	pox/pox.py firewall forwarding.l2_learning log.level --DEBUG samples.pretty_log log --file=pox.log

TOPO_FILE = topology.py
SWITCH_TYPE = ovsk
TOPO_NAME = mytopo
SWITCHES = 4
CONTROLLER_IP = 127.0.0.1
CONTROLLER_PORT = 6633

mn: mn_clean
	sudo mn --custom ${TOPO_FILE} --arp --mac --switch ${SWITCH_TYPE} --topo ${TOPO_NAME},${SWITCHES} --controller remote,ip=${CONTROLLER_IP},port=${CONTROLLER_PORT}

mn_clean:
	mn -c