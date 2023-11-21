# Comandos generales

⚠️ **Aclaración:** Los comandos deben ejecutarse desde el root del proyecto.

### **1.** Instalar POX
```
$ make install
```  
### **2.** Ejecutar POX
```
$ make pox
```  
### **4.** Crear topología de mininet
```
$ make mn
```  
### **5.** Testear conexiones entre todos los hosts
```
mininet> pingall
```

### **6.** Abrir terminales de hosts de ambos extremos de la red
```
mininet> xterm lh1 rh1
```

### **7.** Testear reglas del firewall mediante comando `iperf` en modo cliente y servidor
```
lh1> iperf -c 10.0.0.3 -e -p 5001 -u
```
```
rh1> iperf -s -p 5001 -u
```
📝 *Para testear cada una de las reglas se deberán ir modificando los valores de los puertos (`-p <puerto>`), ip de destino (`-c <ip_destino>`) y protocolo de transporte (`-u` es UDP, sin `-u` es TCP) que usa `iperf`.*