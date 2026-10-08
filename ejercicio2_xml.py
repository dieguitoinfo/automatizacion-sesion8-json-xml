import xml.etree.ElementTree as ET

# Cargar y leer el archivo XML
tree = ET.parse("dispositivos.xml")
root = tree.getroot()

print("Etiqueta principal:", root.tag)

# Recorrer los routers
for router in root.findall("router"):
    router_id = router.attrib.get("id")
    hostname = router.find("hostname").text
    location = router.find("location").text

    print(f"\nRouter ID: {router_id}")
    print(f"Hostname: {hostname}")
    print(f"Ubicación: {location}")
    print("Interfaces:")

    # Recorrer las interfaces del router
    for iface in router.find("interfaces").findall("interface"):
        nombre = iface.attrib.get("name")
        ip = iface.find("ip").text
        estado = iface.find("status").text

        print(f" - {nombre} -> IP: {ip} | Estado: {estado}")