# network-automation 🔧🌐
Repository for Networking area

This repository contains hands-on **networking and automation projects** developed in an **EVE-NG lab** environment.  
The focus is on **Cisco and Python/Ansible automation**.  

---

## 📌 Projects Included

### 1️⃣ [Project 1 - Device Version & Interface Status](./Project1_Device_Status/README.md)
- Connects to multiple devices using **Netmiko**.  
- Extracts **software version** (filtered from `show version`).  
- Retrieves **interface operational state** (`show ip int brief` or equivalent on ASA).  
- Supports multiple device types (IOS/XE routers, ASA firewalls).  

### 2️⃣ [Project 2 - Configuration Backup](./Project2_Backup_Configs/README.md)
- Automates **running-config backup** from routers and firewalls.  
- Saves configs locally with hostname + timestamp.  
- YAML-driven device inventory.  

---

## 🖥️ Lab Topology

![Lab Topology](./docs/topology.png)

- **Ubuntu 22.04** (Automation Host)  
- **Cisco CSR1000v Routers** (R1)  
- **Cisco IOSv Routers** (R2)  
- **Cisco ASA Firewall** (FW1)  

---

## 🚀 Requirements

- EVE-NG CE with equipment images installed
- Python 3.10+  
- [Netmiko](https://github.com/ktbyers/netmiko)  
- [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)  
- Devices accessible via SSH  

```bash
pip install netmiko pyyaml


## 📅 Roadmap

✔ Project 1 - Device Info
✔ Project 2 - Backup Configurations
⬜ Project 3 - Bulk Configuration Deployment
⬜ Project 4 - Ansible Playbooks for Network Automation
