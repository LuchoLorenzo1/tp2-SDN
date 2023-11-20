.PHONY: install pox mn mn_clean udp_client tcp_client udp_server tcp_server

install:
	git clone http://github.com/noxrepo/pox
	cd pox; git checkout dart
	mv firewall.py pox/ext/

pox:
	pox/pox.py firewall forwarding.l2_learning log.level --DEBUG samples.pretty_log

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

MSG = bienvenido
ADDR = 10.0.0.4
PORT = 3000

udp_client:
	python scripts/clients/udp_client.py ${MSG} ${ADDR} ${PORT}

udp_server:
	python scripts/servers/udp_server.py ${PORT}

tcp_client:
	python scripts/clients/tcp_client.py ${MSG} ${ADDR} ${PORT}

tcp_server:
	python scripts/servers/tcp_server.py ${PORT}

