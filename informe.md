# Preguntas a responder
1. ¿Cuál es la diferencia entre un Switch y un router? ¿Qué tienen en común?
    > El objetivo principal de un router es conectar varias redes simultáneamente (se utiliza en el núcleo de la red) y se considera que es un dispositivo que trabaja en la capa de red. En cambio, un switch permite que distintos dispositivos conectados puedan compartir información sin importar su localización dentro de un edificio o campus (se utiliza en redes de acceso). Se considera que un switch trabaja en la capa de enlace. Lo que tienen en común es que ambos son dispositivos que toman los paquetes recibidos mediante sus puertos de entrada y los envían por aquellos puertos de salida que les permitan llegar a sus respectivos destinos finales.
2. ¿Cuál es la diferencia entre un Switch convencional y un Switch OpenFlow?
    > En uno convencional, el plano de datos y de control se encuentran implementados y funcionan en el mismo dispositivo. En cambio, en un switch OpenFlow sólo se ejecutarán acciones propias del plano de datos. Todas las funciones características del plano de control (cálculo de tablas de flujo, etc.) son llevadas a cabo por un dispositivo externo llamado controller. Es con este último con quien el switch mantiene una comunicación constante mediante mensajes propios del protocolo.
3. ¿Se pueden reemplazar todos los routers de la Intenet por Switches OpenFlow? Piense en el escenario interASes para elaborar su respuesta
    > 

# Simulación

## Firewall deactivated

Archivo de configuración
```
{
    "firewall_dpid": -1,
    "host1_ip": "10.0.0.1",
    "banned_ip1": "10.0.0.1",
    "banned_ip2": "10.0.0.4"
}
```
Output mininet
```
mininet> pingall
*** Ping: testing ping reachability
lh1 -> lh2 rh1 rh2 
lh2 -> lh1 rh1 rh2 
rh1 -> lh1 lh2 rh2 
rh2 -> lh1 lh2 rh1 
*** Results: 0% dropped (12/12 received)
```

## Firewall activated

Pingall
```
mininet> pingall
*** Ping: testing ping reachability
lh1 -> lh2 rh1 X 
lh2 -> lh1 rh1 rh2 
rh1 -> lh1 lh2 rh2 
rh2 -> X lh2 rh1 
*** Results: 16% dropped (10/12 received)
```