# 📘 Lab 2 — Gathering and Saving Cisco Device Facts (IOS + ASA)

## 🎯 Objective
This lab demonstrates how to use **Ansible** to automatically **collect Cisco device facts** (such as hostname, version, model, and interfaces) from **Cisco IOS and ASA** devices, and save the results to structured files for documentation or auditing purposes.
![Lab Topology](https://github.com/user-attachments/assets/2f974662-3fa7-441b-814a-438a4e66cde0)

---

Medium Link: https://medium.com/@mickaelsoares/network-automation-with-ansible-collecting-cisco-device-facts-c7954990a2d1


---


## 🧰 Requirements
- Completion of **Lab 1** (Ansible environment configured)
- SSH access to Cisco IOS and ASA devices
- Inventory file (`inventory/hosts.ini`) already configured
- Python virtual environment activated (`source automation-env/bin/activate`)


---

## 📂 Directory Structure

```bash
ansible-lab/
├── inventory/
│   └── hosts.ini
├── playbooks/
│   └── gather_facts.yml
├── outputs/
│   ├── ios.json
│   └── asa.json
└── README.md
```

---

## ⚙️ Playbook: gather_facts.yml

https://github.com/MSoares95/network-automation/blob/main/Ansible_Labs/Lab2_Collecting_Cisco_Devices_Facts/playbooks/gather_facts.yml


---

## 🧩 Explanation

- Gather IOS device facts	Executes show version on IOS devices
- Save IOS facts to file	Saves the collected information to /outputs
- Gather ASA device facts	Executes show version on ASA firewalls
- Save ASA facts to file	Saves the collected information to /outputs

Each device produces a separate json file containing the full version details.


---

## ▶️ Run the Playbook

```bash
ansible-playbook -i inventory/hosts.ini playbooks/gather_facts.yml
```

---

## ✅ Expected Output

Example console output:

<img width="946" height="650" alt="Gather_facts_1" src="https://github.com/user-attachments/assets/07a89b67-a36b-4119-bd20-b05df1df61fe" />



---

## 📁 Sample Output Files

<img width="628" height="168" alt="Gather_facts_2" src="https://github.com/user-attachments/assets/523d93fa-8ed0-491f-a049-4f3c2f2d0110" />





---

## 🧠 Key Concepts

Conditional tasks (when) → differentiate commands for IOS and ASA

- cli_command module → runs any show or exec command on network devices
- copy module → saves command output to local files
- Facts storage → enables version tracking and device documentation


---

## 🚀 Next Steps

Lab 3 — Configuring NTP and Logging on Cisco IOS and ASA devices using Ansible.
