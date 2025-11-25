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

### Installation

Clone the repository:

```bash
git clone https://github.com/<your_repo>/advanced-subnet-calculator.git
```

Install dependencies:

```bash
pip install -r requirements.txt --user
```

Configure AWS CLI (required if using EC2 IP fetch):

```bash
aws configure
```

**OR**

1. Download the latest release from [Releases](https://github.com/Tes3awy/subnetting/releases/).
2. Extract `subnetting.zip` file.
3. `cd` into the `subnetting` directory.
4. Run the following command in terminal:

```bash
pip install -r requirements.txt --user
```
---

---

### How it Works

# Run the main script in AWS Cloud9:

```bash
python3 main.py
```

You will be prompted to choose the input mode:

Enter [1] to enter an IP address
Enter [2] to use your EC2 server IP address

Options:

1. Enter an IP manually
    - Type any IPv4 address in CIDR format (e.g., 192.168.1.0/24)
    - The script will calculate subnets based on your input

2. Use your EC2 server IP
    - The script fetches running EC2 instance IPs using boto3
    - Choose public or private IP for subnet calculation

Next, select the subnetting mode:

Do you want to enter number of (n) networks or (h) hosts? `[n/h]`:

    - `n` → Enter the number of networks you need
    - `h` → Enter the number of hosts per subnet

The script calculates for each subnet:

- Network ID
- Broadcast ID
- First host
- Last host
- Total usable hosts

Results are displayed in a **formatted table** using `tabulate`.

**Note:**

- CIDR notation without a prefix is treated as `/32`
- Gateway input accepts `0` or `1` only:  
  - `0` picks the first IP of the subnet  
  - `1` picks the last IP of the subnet
### Features
- Automatic AWS EC2 IP detection
- Supports both network-based and host-based subnetting
- Nicely formatted output table
- Works on Python 3.7+
### Example Output
 Enter [1] to enter an IP address
 Enter [2] to use your EC2 server IP address: 1
 Enter Required IP Address in CIDR format: 192.168.1.0/24
 ===== Subnetting Calculator =====
 Do you want to enter number of (n) networks or (h) hosts? [n/h]: n
 Enter number of networks needed: 4
 ===== Subnetting Result =====
+-----------+------------+------------+--------------+------------+-----------+-------------------+
| Subnet #  | CIDR       | Network ID | Broadcast ID | First Host | Last Host | Total Usable Hosts |
+-----------+------------+------------+--------------+------------+-----------+-------------------+
| 1         | 192.168.1.0/26 | 192.168.1.0 | 192.168.1.63 | 192.168.1.1 | 192.168.1.62 | 62                |
| 2         | 192.168.1.64/26 | 192.168.1.64 | 192.168.1.127 | 192.168.1.65 | 192.168.1.126 | 62                |
| 3         | 192.168.1.128/26 | 192.168.1.128 | 192.168.1.191 | 192.168.1.129 | 192.168.1.190 | 62                |
| 4         | 192.168.1.192/26 | 192.168.1.192 | 192.168.1.255 | 192.168.1.193 | 192.168.1.254 | 62                |
+-----------+------------+------------+--------------+------------+-----------+-------------------+
### License
This project is licensed under the MIT License.
