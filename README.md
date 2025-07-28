# 🌐 IP Address Lookup Tool (Python + ipinfo.io)

This project is a simple and effective Python-based tool to **fetch geolocation and ISP details** of any IP address using the [ipinfo.io](https://ipinfo.io/) API.

---

## 🧠 Project Summary

This tool allows you to:
- Automatically detect your own public IP address
- Enter any IP address to retrieve location, timezone, ISP, and more
- Use a secure API token stored in a `.env` file

Ideal for learning about APIs, networking, and Python environment management.

---

## 🚀 Features

- 🔍 Detects your public IP automatically
- 📡 Shows city, region, country, coordinates, ISP, and timezone
- 🔐 Uses `.env` file to store your API key securely
- 🔁 Menu-driven CLI interface (loop until user exits)

---

## 🧱 File Structure

```bash
├── main.py            # Main script with CLI and ipinfo API requests
├── .env               # Store your IPINFO_TOKEN here (not pushed to GitHub)
