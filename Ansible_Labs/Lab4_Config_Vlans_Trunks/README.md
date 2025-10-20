## 🕒 Lab 4: Configuring VLANs and Trunks with Ansible

## 🎯 Objective
In Lab 4, we automate the configuration of VLANs and trunks on Cisco switches using Ansible. 
This exercise demonstrates how to manage multiple devices consistently, safely, and efficiently.

<img width="286" height="254" alt="Lab Topology" src="https://github.com/user-attachments/assets/81d7c6e1-f7d0-4043-8134-acda831e854f" />

---

##🌐 Medium Link: https://medium.com/@mickaelsoares/network-automation-with-ansible-lab4-configure-vlans-and-trunks-f97775cd2d61

---

##🧰 Requirements
Ansible control node (Linux environment)
SSH connectivity to Cisco devices
Cisco IOS Switches


---

##▶️ Run the Playbook

```yaml
ansible-playbook -i inventory/hosts.ini playbooks/config_vlans_trunks.yml
```

The config_vlans_trunks.yml playbook is organized into three main sections:
- Variables – Define VLANs and trunk ports.
- VLAN Creation – Use the cisco.ios.ios_vlan module to create VLANs.
- Trunk Port Configuration – Use the cisco.ios.ios_interface module to configure trunk ports.

## Variables:
```yaml
vlans:
  - id: 10
    name: "VLAN_10"
  - id: 20
    name: "VLAN_20"
  - id: 30
    name: "VLAN_30"

trunk_ports:
  - "GigabitEthernet0/1"
  - "GigabitEthernet0/2"
````

## Creating VLANs

Using a loop, we can create all VLANs consistently:
```yaml
- name: Create VLANs
  cisco.ios.ios_vlan:
    vlan_id: "{{ item.id }}"
    name: "{{ item.name }}"
    state: present
  loop: "{{ vlans }}"
```

## Configuring Trunk Ports

Trunk ports carry multiple VLANs between switches. The configuration is:
```yaml
- name: Configure trunk ports
  cisco.ios.ios_interface:
    name: "{{ item }}"
    mode: trunk
    trunk_vlans: "{{ vlans | map(attribute='id') | join(',') }}"
  loop: "{{ trunk_ports }}"
```

## ✅ Verification

## Check VLANs
```bash
show vlan brief
```
Screenshot example:

<img width="481" height="135" alt="Teste-sh_vlan_br" src="https://github.com/user-attachments/assets/fd585799-72f4-47a7-a1a2-310d5ffc31e5" />



## Check trunk ports
```bash
show interface trunk
```
Screenshot example:

<img width="419" height="190" alt="Teste-sh_int_tr" src="https://github.com/user-attachments/assets/98d0f119-9db2-4ae4-b33f-025e58414022" />


## Check interface status
```bash
show interface status
```
Screenshot example:

<img width="431" height="126" alt="Teste-sh_int_status" src="https://github.com/user-attachments/assets/55b6881d-5f34-4121-aa07-5b6e96ff0238" />

---

## Conclusion

Automating VLANs and trunk configurations with Ansible brings consistency, efficiency, and scalability. By using variables and loops:
- Changes are applied across multiple devices simultaneously.
- Manual errors are minimized.
- The network is easier to audit and maintain.

This lab is a fundamental step toward real-world network automation, preparing you for enterprise-level tasks with confidence.


🚀 Next Step
