import os
import yaml
from netmiko import ConnectHandler
from datetime import datetime

# Pasta de backup
backup_folder = os.path.expanduser("~/Documentos/NetAuto/Project2-Backup-Configs/backups")
os.makedirs(backup_folder, exist_ok=True)

# Timestamp completo
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Ler devices do YAML
with open("devices_backup.yaml") as f:
    devices = yaml.safe_load(f)  # lista de dicionários

for device in devices:
    # Pega o nome do dispositivo (para imprimir / nome de arquivo)
    device_name = device.get("name", device.get("host", "unknown"))
    
    # Cria um dicionário somente com os argumentos que Netmiko aceita
    netmiko_params = {
        "device_type": device["device_type"],
        "host": device["host"],
        "username": device["username"],
        "password": device["password"],
    }
    if "secret" in device:
        netmiko_params["secret"] = device["secret"]
    
    print(f"Connecting to {device_name} ({device['host']})...")
    
    try:
        connection = ConnectHandler(**netmiko_params, ssh_config_file="~/.ssh/config")
        if "secret" in device:
            connection.enable()

        config = connection.send_command("show running-config")
        
        filename = os.path.join(backup_folder, f"{device_name}_{timestamp}.txt")
        with open(filename, "w") as f:
            f.write(config)

        print(f"Backup saved here: {filename}")
        connection.disconnect()
    except Exception as e:
        print(f"Erro ao conectar a {device_name}: {e}")
