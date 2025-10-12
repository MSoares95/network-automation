# Project 2 - Configuration Backup 💾

## 🎯 Goal
Automate the backup of running configurations from Cisco routers and firewalls using **Python and Netmiko**.

---

## 📂 Structure

```
Project2_Backup_Configs/
├── devices_backup.yaml # Device inventory
├── backup_config.py # Python automation script
├── backups/ # Where configuration files are saved
├── screenshots/ # Where printscreens are saved
└── README.md
```


---

## 🗂️ Device Inventory
Example `devices_backup.yaml`:

```yaml
- name: R1
  host: 192.168.136.134
  username: admin
  password: admin
  device_type: cisco_ios

- name: FW1
  host: 192.168.136.136
  username: cisco
  password: cisco
  device_type: cisco_asa
```

---

## 🐍 Python Script

Main logic in backup_config.py:

- Connect to device using Netmiko
- Run show running-config
- Save output to file named:
```php-template
<hostname>_<timestamp>.txt
```
Example:
```
R1_2025-09-17_20-11-46.txt
```

---

## Run the Script
```bash
cd Project2_Backup_Configs
python3 backup_config.py
```

---

## ✅ Sample Output
```
=== Connecting to R1 (192.168.136.134) ===
Backup saved: /.../backups/R1_2025-09-17_20-11-46.txt
=== Connecting to R2 (192.168.136.135) ===
Backup saved: /.../backups/R1_2025-09-17_20-11-46.txt
=== Connecting to FW1 (192.168.136.136) ===
Backup saved: /.../backups/FW1_2025-09-17_20-11-46.txt
````
## 📸 Suggested Screenshots

- Terminal output with backup success messages
- Example of saved config file in backups/ folder
- YAML inventory file (devices_backup.yaml)
