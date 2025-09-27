# Web Vulnerability Scanner (Educational Project)

## 📌 Project Overview
This is a lightweight Python tool I built to explore common web vulnerabilities. It performs basic checks for:
- **SQL Injection (SQLi)**
- **Cross-Site Scripting (XSS)**
- **Directory Brute Forcing**

The goal of this project is **educational learning** — understanding how vulnerabilities can be detected in a safe, controlled environment. It is **not intended for production use**.

---

## ⚠️ Disclaimer
This tool is provided **for educational purposes only**. Do not use it on systems you do not own or have explicit permission to test. Misuse of this tool could be illegal.

---

## 🚀 Features
- Tests for common SQL injection payloads (e.g., `' OR '1'='1`)
- Tests for reflected XSS vulnerabilities using basic payloads
- Attempts to discover common hidden directories (e.g., `/admin`, `/uploads`, `/config`)

---

## 🛠️ Tech Stack
- **Python 3**
- **requests** library
- **BeautifulSoup4** (for response parsing)

---

## ▶️ Usage
Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/web-vuln-scanner.git
cd web-vuln-scanner
pip install -r requirements.txt
```

Run the scanner:
```bash
python scanner.py
```

Enter the target URL when prompted, for example:
```
Enter target URL (e.g., http://example.com): http://testphp.vulnweb.com
```

---

## 📖 Example Output
```
[+] Testing for SQL Injection...
Potential SQL Injection vulnerability found with payload: ' OR '1'='1

[+] Testing for XSS...
Potential XSS vulnerability found with payload: <script>alert('XSS')</script>

[+] Brute forcing common directories...
Found directory: http://testphp.vulnweb.com/admin
```

---

## 🌟 Why I Built This
I created this project while exploring offensive security techniques and penetration testing fundamentals. It helped me learn how to:
- Think like an attacker when evaluating applications
- Automate vulnerability testing
- Better understand HTTP requests, responses, and edge cases

This project reflects my **hands-on interest in security research**, which connects directly to my career goal of contributing to real-world offensive security programs.

---

## 🔗 Project Link
[GitHub Repository](https://github.com/yourusername/web-vuln-scanner)
