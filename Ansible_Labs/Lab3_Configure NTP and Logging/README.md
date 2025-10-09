# 🕒 Lab 3 — Configure NTP and Logging on Cisco Devices using Ansible

## 🎯 Objective
In this lab, we automate the configuration of **NTP** (Network Time Protocol) and **Syslog Logging** on Cisco **IOS** and **ASA** devices using **Ansible**.  
This ensures time synchronization and centralized log collection across the network — both critical for troubleshooting and security.

---

## 🌐 Medium Link: 
https://medium.com/@mickaelsoares/network-automation-with-ansible-lab3-configure-ntp-and-logging-864af70865cf

---


## 🧰 Requirements
- Ansible control node (Linux environment)
- SSH connectivity to Cisco devices
- Cisco IOS and ASA devices configured with management IP
- Completed **Lab 2** (device access validated)

Install the required Ansible collections:
```bash
ansible-galaxy collection install cisco.ios cisco.asa
```

---

## 📁 Directory Structure

```bash
ansible-lab/
├── inventory/
│   └── hosts.ini
├── playbooks/
│   └── config_ntp_logging.yml
├── output/
│   └── logs/
└── README.md
```

---

## ⚙️ Inventory File

File: inventory/hosts.ini

```bash
[ios]
192.168.136.134
192.168.136.135

[asa]
192.168.136.136

[all:vars]
ansible_user=cisco
ansible_password=cisco
ansible_become=yes
ansible_become_method=enable
ansible_become_password=cisco
```

---

## 🧠 Playbook 

playbooks/config_ntp_logging.yml

https://github.com/MSoares95/network-automation/blob/main/Ansible_Labs/Lab3_Configure%20NTP%20and%20Logging/playbooks/config_ntp_logging.yml

---

## ▶️ Run the Playbook
```bash
ansible-playbook -i inventory/hosts.ini playbooks/config_ntp_logging.yml
```
---

## ✅ Expected Results
The playbook applies consistent time and logging configurations across all network devices.
Sample IOS configuration after execution:

```bash
Copiar código
R1#show run | include ntp|logging
ntp server 192.168.100.10
logging host 192.168.100.20
logging trap informational
service timestamps log datetime msec
```
ASA example:

```bash
ASA1# show run ntp
ntp server 192.168.100.10 source inside
ASA1# show run logging
logging enable
logging host inside 192.168.100.20
logging trap informational
```
---

## 🧩 Key Concepts
Concept	Description
- NTP	Synchronizes device clocks with a centralized server
- Syslog sends event messages to a central logging server
- cisco.ios.ios_config is the module for sending config commands to IOS devices
- cisco.asa.asa_config is the module for sending config commands to ASA firewalls
- Variables	Make configurations reusable and easy to update

---

## 🚀 Next Step
Proceed to Lab 4 — Configuring VLANs and Trunks across Multiple Switches.
