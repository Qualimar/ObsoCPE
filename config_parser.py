import re

def parse_config(config_data):
    parsed_data = {
        "interfaces": [],
        "vlans": [],
        "dhcp": False,
        "dhcp_relay": False,
        "qos": False,
        "ip_sla": False,
    }
    
    interfaces = re.findall(r'^interface (\S+)', config_data, re.MULTILINE)
    parsed_data["interfaces"].extend(interfaces)
    
    vlans = re.findall(r'^vlan (\d+)', config_data, re.MULTILINE)
    parsed_data["vlans"].extend(vlans)
    
    if "ip dhcp pool" in config_data:
        parsed_data["dhcp"] = True
    
    if "ip helper-address" in config_data:
        parsed_data["dhcp_relay"] = True
    
    if "class-map" in config_data or "policy-map" in config_data:
        parsed_data["qos"] = True
    
    if "ip sla" in config_data:
        parsed_data["ip_sla"] = True
    
    return parsed_data

def convert_config(constructeur_a, modele_a, constructeur_b, modele_b, config_data):
    parsed_data = parse_config(config_data)
    
    converted_config = f"Conversion de {constructeur_a} {modele_a} à {constructeur_b} {modele_b}\n"
    converted_config += f"Interfaces détectées : {', '.join(parsed_data['interfaces'])}\n"
    converted_config += f"VLANs détectés : {', '.join(parsed_data['vlans'])}\n"
    converted_config += f"DHCP : {'Oui' if parsed_data['dhcp'] else 'Non'}\n"
    converted_config += f"DHCP Relay : {'Oui' if parsed_data['dhcp_relay'] else 'Non'}\n"
    converted_config += f"QoS : {'Oui' if parsed_data['qos'] else 'Non'}\n"
    converted_config += f"IP SLA : {'Oui' if parsed_data['ip_sla'] else 'Non'}\n"
    
    # Logique de conversion en fonction du constructeur et du modèle
    # Ajoutez ici les transformations spécifiques en fonction de vos besoins

    return converted_config
