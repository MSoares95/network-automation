from netmiko import ConnectHandler
import yaml

# Carrega dispositivos
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

# Carrega comandos
with open("config_commands.yaml") as f:
    config_cmds = yaml.safe_load(f)

for device in devices:
    name = device.get("name", device["host"])
    print(f"\n=== Deploying config to {name} ({device['host']}) ===")

    try:
        dev_copy = device.copy()
        dev_copy.pop("name", None)

        connection = ConnectHandler(**dev_copy)

        device_type = dev_copy["device_type"]
        commands = config_cmds.get(device_type, [])

        for cmd in commands:
            if cmd.startswith("banner motd"):
                # Extrai o banner sem o prefixo
                banner_lines = cmd.replace("banner motd", "").strip().splitlines()

                # Entra no modo config
                connection.config_mode()

                # Inicia banner
                connection.send_command_timing("banner motd ^")
                for line in banner_lines:
                    connection.send_command_timing(line)

                # Fecha o banner
                connection.send_command_timing("^")
                connection.exit_config_mode()
            else:
                connection.send_config_set([cmd])

        connection.save_config()
        connection.disconnect()
        print(f"✔ Config applied successfully to {name}")

    except Exception as e:
        print(f"Error on {name}: {e}")
