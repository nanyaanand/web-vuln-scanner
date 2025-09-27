# Web Vulnerability Scanner (Educational Project)
# Author: Ananya Anand
# Description: A lightweight Python tool to scan a target website for common vulnerabilities like XSS, SQLi, and directory brute force.
# Disclaimer: This tool is for educational purposes only. Do not use against systems you do not own or have explicit permission to test.

import requests
from bs4 import BeautifulSoup

# Common payloads for testing SQLi and XSS vulnerabilities
SQLI_PAYLOADS = ["' OR '1'='1", "' OR '1'='1' --", "admin' --"]
XSS_PAYLOADS = ["<script>alert('XSS')</script>", "\" onmouseover=alert('XSS')"]

# Common directories to brute force
directories = ["admin", "login", "uploads", "config", "dashboard"]


def check_sqli(url):
    print("[+] Testing for SQL Injection...")
    for payload in SQLI_PAYLOADS:
        try:
            new_url = f"{url}?id={payload}"
            response = requests.get(new_url, timeout=5)
            if "error" in response.text.lower() or "sql" in response.text.lower():
                print(f"Potential SQL Injection vulnerability found with payload: {payload}")
        except Exception as e:
            print(f"Error testing SQLi payload {payload}: {e}")


def check_xss(url):
    print("[+] Testing for XSS...")
    for payload in XSS_PAYLOADS:
        try:
            response = requests.get(url, params={"q": payload}, timeout=5)
            if payload in response.text:
                print(f"Potential XSS vulnerability found with payload: {payload}")
        except Exception as e:
            print(f"Error testing XSS payload {payload}: {e}")


def brute_force_directories(url):
    print("[+] Brute forcing common directories...")
    for directory in directories:
        try:
            new_url = f"{url}/{directory}"
            response = requests.get(new_url, timeout=5)
            if response.status_code == 200:
                print(f"Found directory: {new_url}")
        except Exception as e:
            print(f"Error accessing {new_url}: {e}")


if __name__ == "__main__":
    target_url = input("Enter target URL (e.g., http://example.com): ").strip()
    if target_url:
        check_sqli(target_url)
        check_xss(target_url)
        brute_force_directories(target_url)
    else:
        print("No URL provided.")
