# 🔍 Advanced TCP Port Scanner

A Python-based TCP Port Scanner developed as part of a Cyber Security & Ethical Hacking Internship. This tool scans a target system, identifies open ports, detects associated services, and generates a scan report.

---

## 📌 Project Overview

Port scanning is one of the fundamental techniques used in network administration, cybersecurity assessments, and penetration testing. This project helps identify active services running on a target machine by scanning a specified range of TCP ports.

The scanner was tested in a controlled virtual lab environment using Kali Linux and Metasploitable 2.

---

## ✨ Features

* TCP Port Scanning
* Custom Target IP Address
* User-Defined Port Range
* Service Detection
* Open Port Enumeration
* Scan Summary Report
* Results Export to Text File
* Exception Handling
* Beginner-Friendly Interface

---

## 🛠️ Technologies Used

* Python 3
* Socket Programming
* Kali Linux
* VirtualBox
* Metasploitable 2

---

## 📂 Project Structure

```text
PortScanner/
│
├── port_scanner.py
├── scan_results.txt
├── README.md
└── screenshots/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/devloperraj12/PortScanner.git
cd PortScanner
```

---

## ▶️ Usage

Run the scanner:

```bash
python3 port_scanner.py
```

Enter:

```text
Target IP Address
Start Port
End Port
```

Example:

```text
Target IP Address: 192.168.1.3
Start Port: 1
End Port: 10000
```

---

## 📸 Sample Output

```text
[+] Port 21 OPEN | Service: ftp
[+] Port 22 OPEN | Service: ssh
[+] Port 23 OPEN | Service: telnet
[+] Port 80 OPEN | Service: http
[+] Port 3306 OPEN | Service: mysql

===========================
SCAN SUMMARY
===========================
Target IP      : 192.168.1.3
Ports Scanned  : 1-10000
Open Ports     : 26
```

---

## 🧪 Testing Environment

| Component        | Details          |
| ---------------- | ---------------- |
| Attacker Machine | Kali Linux       |
| Target Machine   | Metasploitable 2 |
| Virtualization   | VirtualBox       |
| Language         | Python 3         |

---

## 🔒 Ethical Use Notice

This tool is intended strictly for educational purposes and authorized security testing. Only scan systems that you own or have explicit permission to assess.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Socket Programming
* Network Communication
* TCP/IP Fundamentals
* Cybersecurity Reconnaissance
* Service Enumeration
* Ethical Hacking Concepts

---

## 👨‍💻 Author

**Raj Kumar Sah**

Cyber Security & Ethical Hacking Intern

GitHub: https://github.com/devloperraj12

LinkedIn: https://www.linkedin.com/in/rajkrsah17

---


