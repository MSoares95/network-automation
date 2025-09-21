# Project 3 - Bulk Deployment

## 🎯 Goal

This project demonstrates **bulk configuration deployment** using:

- **Python 3 / Netmiko** library for SSH automation  
- **YAML** to store configuration commands per device type  

Configurations applied:

- Banner MOTD for login notices  
- NTP server configuration  
- Logging enabled to remote syslog host  

Medium: https://medium.com/@mickaelsoares/network-automation-with-python-and-netmiko-bulk-deployment-fb4496d4474f

---

## **Lab Topology**

**EVE-NG topology:**

![Lab Topology2](https://github.com/user-attachments/assets/a61a3123-cc5e-4154-9382-ff03a182d5d7)


---

## **Prerequisites**

- Automation Server with Ubuntu 22.04/24.04 Desktop (or server)  
- Python 3.10+  
- Virtual environment (`venv`)  
- Netmiko, PyYAML installed  

**Install dependencies:**

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
python3 -m venv automation-env
source automation-env/bin/activate
pip install --upgrade pip
pip install netmiko pyyaml
```

---

## ** 📂 Structure**

```text
Project3-Bulk_Deploy/
│
├── automation-env/          # Python virtual environment
├── config_commands.yaml     # YAML file with commands per device type
├── devices.yaml             # YAML file listing all devices
├── deploy_config.py         # Python script to deploy configurations
├── session_logs/            # (optional) logs of SSH sessions
└── README.md
```

---

## ** 🗂️ YAML Configuration**

config_commands.yaml:

```yaml
cisco_ios:
  - banner motd %Authorized Access Only!\nAll activity is monitored.%
  - ntp server 192.168.100.10
  - logging on
  - logging trap informational
  - logging 192.168.100.20
  - logging buffered informational
  - logging console informational

cisco_asa:
  - banner motd "Authorized Access Only!\nAll activity is monitored."
  - ntp server 192.168.100.10
  - logging enable
  - logging trap informational
  - logging host inside 192.168.100.20
```

devices.yaml:

```yaml
- name: R1
  host: 192.168.136.134
  device_type: cisco_ios
  username: cisco
  password: cisco
  secret: cisco

- name: R2
  host: 192.168.136.135
  device_type: cisco_ios
  username: cisco
  password: cisco
  secret: cisco

- name: FW1
  host: 192.168.136.136
  device_type: cisco_asa
  username: cisco
  password: cisco
  secret: cisco
```

---

## **🐍 Python Script**
We use Netmiko to deploy the configurations.

Key snippet from deploy_config.py:

```python
for device in devices:
    connection = ConnectHandler(**device)
    if device["device_type"] == "cisco_asa":
        connection.enable()  # enter privileged mode for ASA

    cmds = commands_by_type[device["device_type"]]
    connection.send_config_set(cmds)
    connection.save_config()
```

Explanation:
- Connects via SSH using Netmiko
- ASA devices require enable() before configuration
- send_config_set() applies commands from YAML
- save_config() ensures persistent changes


---

## **✅ Expected output:**

```text
=== Deploying config to R1 (192.168.136.134) ===
✔ Config applied successfully to R1

=== Deploying config to R2 (192.168.136.135) ===
✔ Config applied successfully to R2

=== Deploying config to FW1 (192.168.136.136) ===
✔ Config applied successfully to FW1
```

---

## **📸 Verification**
Check images below

![Project3 - R1 banner](https://github.com/user-attachments/assets/8fc184cd-c738-45b8-ac96-4a979ccc4464)

![Project3 - FW1 banner](https://github.com/user-attachments/assets/a3e15cdc-34fb-4bd1-94ee-461b8559dc85)

![Project3 - R1 ntp](https://github.com/user-attachments/assets/5b6cf797-b052-4bbf-a100-ffa8fa5c194b)

![Project3 - FW1 ntp](https://github.com/user-attachments/assets/f2726c1a-fb82-46b6-8497-b27db9ee573e)

![Project3 - R2 logging](https://github.com/user-attachments/assets/9dddb609-dd59-48b7-bf79-bbb82a50a786)



---

## **Next Steps**
- Backup running configurations before deployment
- Add error handling and logging for failed deployments
- Extend YAML for interface IPs, routing, and ACLs
- Integrate with Ansible for more advanced automation
