# Automated Security Audit & Hardening Lab

## 📌 Project Overview
This project demonstrates a complete **Vulnerability Assessment and Remediation** cycle in a Linux environment. It includes service discovery, automated security auditing using Python, and system hardening.

### 🛠 Tools Used
*   **OS:** Ubuntu / WSL
*   **Languages:** Python 3
*   **Network Scanning:** Nmap
*   **Web Server:** Nginx

---

## 🚀 Lab Phases

### Phase 1: Reconnaissance & Discovery
Using `nmap`, I identified active services and potential vulnerabilities in the local environment.
**Command:** `nmap -sV --script vuln localhost`
*Findings:* Identified a vulnerable Nginx version and an unauthorized service running on port 8080.

### Phase 2: Automated Auditing (Python)
I developed a custom Python tool (`auditor.py`) to automate the check of critical ports and software versions. This tool mimics basic functionality of enterprise vulnerability scanners.

### Phase 3: System Hardening (Remediation)
Steps taken to secure the system:
1.  **Service Termination:** Disabled unauthorized background processes.
2.  **Patch Management:** Updated Nginx to the latest version to mitigate CVEs.
3.  **Firewall Configuration:** Configured `ufw` to block all ports except HTTP/HTTPS.

---

## 📁 Structure
*   `scripts/vulnerable_service.py` - Mock target for discovery.
*   `scripts/auditor.py` - Custom security auditing script.
*   `README.md` - Project documentation.

## ⚠️ Disclaimer
This project is for **educational purposes only**. All tests were performed in a controlled, authorized local environment.
