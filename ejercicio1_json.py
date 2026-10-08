import json


# Respuesta simulada que podría devolver una API de un router.
json_response = """
{
    "device": "Core-Router-01",
    "status": "active",
    "interfaces": [
        {
            "name": "GigabitEthernet0/0",
            "ip": "192.168.1.1",
            "netmask": "255.255.255.0",
            "status": "up"
        },
        {
            "name": "GigabitEthernet0/1",
            "ip": "10.0.0.1",
            "netmask": "255.255.255.252",
            "status": "up"
        },
        {
            "name": "GigabitEthernet0/2",
            "ip": "unassigned",
            "netmask": "none",
            "status": "down"
        }
    ]
}
"""

# Convierte el texto JSON en datos que Python puede usar.
data = json.loads(json_response)

print(f"=== REPORTE DEL DISPOSITIVO: {data['device']} ===")
print(f"Estado general: {data['status']}\n")

# Muestra solo las interfaces activas con IP asignada.
print("Interfaces configuradas y activas:")
for iface in data["interfaces"]:
    if iface["status"] == "up" and iface["ip"] != "unassigned":
        print(
            f" - Interfaz: {iface['name']} | "
            f"IP: {iface['ip']} | Estado: {iface['status']}"
        )

# Reúne las IP activas en un nuevo objeto.
nuevo_dispositivo = {
    "device": data["device"],
    "active_ips": [
        iface["ip"]
        for iface in data["interfaces"]
        if iface["status"] == "up" and iface["ip"] != "unassigned"
    ],
}

# Convierte el objeto de Python a texto JSON ordenado.
json_output = json.dumps(nuevo_dispositivo, indent=4)

print("\n=== JSON REESTRUCTURADO ===")
print(json_output)