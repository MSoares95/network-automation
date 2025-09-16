from netmiko import ConnectHandler
import yaml

# Load devices from YAML
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

for device in devices:
    device_name = device.get("name", device["host"])
    print(f"\n=== Connecting to {device_name} ({device['host']}) ===")

    device_copy = device.copy()
    device_copy.pop("name", None)

    try:
        connection = ConnectHandler(**device_copy)

        # Select commands based on device type
        if device_copy['device_type'] == "cisco_asa":
            connection.enable()
            commands = [
                "show version | include Cisco Adaptive Security Appliance Software Version",
                "show interface ip brief"
            ]
        else:
            commands = [
                "show version | inc , Version",
                "show ip interface brief"
            ]

        for cmd in commands:
            output = connection.send_command(cmd)
            print(f"\n>> {cmd}\n{output}")

        connection.disconnect()
    except Exception as e:
        print(f"Error connecting to {device_name}: {e}")
