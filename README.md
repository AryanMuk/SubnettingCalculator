[![Tested on Python 3.7+](https://img.shields.io/badge/Python%203.7+-blue.svg?logo=python&logoColor=white&style=flat-square)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-purple?style=flat-square)]()

# Advanced IPv4 Subnet Calculator (AWS Cloud9)

## Table of Contents

1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [How it Works](#how-it-works)
5. [Features](#features)
6. [Example Output](#example-output)
7. [License](#license)

---

### Project Overview

This Python 3 tool calculates IPv4 subnets and integrates with **AWS EC2 instances**.  

Key functionalities:

- Fetch running EC2 public/private IPs automatically
- Subnet manually via CIDR input
- Subnet based on number of networks or required hosts
- Convert IP to CIDR automatically (Class A/B/C)
- Display results in a formatted table using `tabulate`

---

### Getting Started

Project structure:

```bash
│   main.py
│   subnetting.py
│   ec2_ip_fetcher.py
│   ip_to_cidr.py
│   requirements.txt
│   README.md
│   .gitignore
│   LICENSE
│
└───assets
        demo.png
---

---
## Installation

Clone the repository:

```bash
$ git clone https://github.com/<your_repo>/advanced-subnet-calculator.git
$ cd advanced-subnet-calculator
$ pip install -r requirements.txt --user
---
