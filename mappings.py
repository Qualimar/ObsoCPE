def get_modeles(constructeur):
    modeles = {
        "Cisco": ["C1117", "C887"],
        "Juniper": ["SRX300", "SRX320"],
        "Huawei": ["AR169", "AR169F"],
    }
    return modeles.get(constructeur, [])
