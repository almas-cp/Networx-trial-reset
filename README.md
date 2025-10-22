# 🌐 NetWorx Trial Reset

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**A beautiful CLI tool to automatically reset NetWorx trial period**

*Extend your NetWorx bandwidth monitoring trial with elegant automation*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Troubleshooting](#-troubleshooting)

</div>

---

## 🎯 Overview

**NetWorx Trial Reset** is a sleek Python script that automatically resets the trial period for [NetWorx](https://www.softperfect.com/products/networx/) - a powerful bandwidth monitoring and data usage reporting tool for Windows. Built with a beautiful terminal interface powered by Rich, it handles the entire process seamlessly - from stopping the NetWorx service to updating the database and restarting it.

### What is NetWorx?

NetWorx is a versatile bandwidth monitoring tool that helps you track your Internet connection usage, measure connection speed, and identify network issues. It offers a fully-featured 30-day trial period, after which it requires a license purchase[attached_file:1].

### Why Use This Script?

- 🎨 **Beautiful Terminal UI** - Rich, colorful output with progress indicators and tables
- 🔄 **Zero Manual Work** - Fully automated trial reset process
- 🛡️ **Safe & Reliable** - Proper error handling and automatic service recovery
- ⚡ **Lightning Fast** - Updates complete in seconds
- 🔍 **Smart Detection** - Automatically finds NetWorx installation
- 📊 **Visual Feedback** - Clear before/after value comparison

---

## ✨ Features

### Core Functionality

- **Automatic Process Management**
  - Detects running NetWorx processes
  - Safely terminates before database modification
  - Auto-restarts after successful update

- **Intelligent Date Handling**
  - Resets `TrialDate` to current system date
  - Sets `NextReminder` to 30 days ahead
  - Extends trial period automatically

- **Beautiful CLI Interface**
  - Colorful progress spinners
  - Comparison tables (old vs new values)
  - Clear status indicators (✓ ✗ ⚠)
  - Bordered panels and formatted output

- **Robust Error Handling**
  - Database validation checks
  - File existence verification
  - Graceful failure recovery
  - Service restart even on errors

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have:

- **NetWorx** installed on Windows ([Download here](https://www.softperfect.com/products/networx/))
- **Python 3.7+** installed on your system
- **Administrator privileges** (required for process management)

### Step 1: Clone the Repository

```bash
git clone https://github.com/almas-cp/Networx-trial-reset.git
cd Networx-trial-reset
```

### Step 2: Install Dependencies

```bash
pip install rich psutil
```

That's it! You're ready to go. 🎉

---

## 💻 Usage

### Basic Usage

Run the script with administrator privileges:

```bash
python script.py
```

> **Note:** Administrator privileges are required to stop and restart NetWorx processes.

### What Happens When You Run It

```
┌─────────────────────────────────────────┐
│ 1. 🔍 Locates NetWorx Installation │
│ 2. 🛑 Stops Running NetWorx Process │
│ 3. 🔌 Connects to SQLite Database │
│ 4. ✏️ Resets Trial Date Values │
│ 5. 💾 Commits All Changes │
│ 6. ▶️ Restarts NetWorx Service │
└─────────────────────────────────────────┘
```

### What Gets Updated

| Parameter | Description | New Value |
|-----------|-------------|-----------|
| **TrialDate** | Trial start date | Current system date |
| **NextReminder** | Next trial reminder | Current date + 30 days |

This effectively resets your NetWorx trial period to start from today.

---

## 🔧 Technical Details

### Database Configuration

| Setting | Value |
|---------|-------|
| **Database Location** | `C:\ProgramData\SoftPerfect\NetWorx\NetWorx.db3` |
| **Database Type** | SQLite 3 |
| **Target Table** | `CONFIG` |
| **Modified Parameters** | `TrialDate`, `NextReminder` |

### Supported NetWorx Paths

The script automatically searches these common installation locations:

- `C:\Program Files\NetWorx\networx.exe`
- `C:\Program Files (x86)\NetWorx\networx.exe`
- `C:\Program Files\SoftPerfect\NetWorx\networx.exe`
- `C:\Program Files (x86)\SoftPerfect\NetWorx\networx.exe`

### Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `sqlite3` | Database operations | Built-in |
| `rich` | Terminal UI & formatting | Latest |
| `psutil` | Process management | Latest |
| `datetime` | Date calculations | Built-in |
| `pathlib` | Path handling | Built-in |

---

## 📋 How It Works

### The Trial Mechanism

NetWorx stores its trial information in an SQLite database located at `C:\ProgramData\SoftPerfect\NetWorx\NetWorx.db3`. The `CONFIG` table contains trial-related parameters that track when the trial started and when to show the next reminder[attached_file:1].

### Database Modifications

The script modifies two key parameters:

```sql
UPDATE CONFIG
SET PARAM_VALUE = '2025-10-22'
WHERE PARAM_NAME = 'TrialDate';

UPDATE CONFIG
SET PARAM_VALUE = '2025-11-21'
WHERE PARAM_NAME = 'NextReminder';
```

### Process Flow

1. **Detection** - Locates NetWorx installation and running processes
2. **Termination** - Safely stops NetWorx.exe if running (required for database access)
3. **Connection** - Opens SQLite database connection
4. **Reading** - Retrieves current trial configuration values
5. **Updating** - Resets TrialDate to today and NextReminder to +30 days
6. **Committing** - Saves changes to database
7. **Restarting** - Launches NetWorx application with reset trial

---

## 🐛 Troubleshooting

### Common Issues

#### Database Not Found

**Problem:** Script can't locate `NetWorx.db3`

**Solution:**
- Verify NetWorx is properly installed
- Check the path: `C:\ProgramData\SoftPerfect\NetWorx\`
- Run NetWorx at least once before using this script
- Modify the `db_path` parameter if you have a custom installation

#### Permission Denied

**Problem:** Access denied when modifying database

**Solution:**
- **Run terminal/command prompt as Administrator** (required)
- Ensure NetWorx is not running in the background
- Check file permissions on the database directory
- Disable antivirus temporarily if it's blocking access

#### NetWorx Won't Restart

**Problem:** Script completes but NetWorx doesn't start

**Solution:**
- Manually start NetWorx from Start menu
- Verify the executable path is correct
- Check Windows Event Viewer for startup errors
- Ensure no other processes are blocking the restart

#### Table 'CONFIG' Not Found

**Problem:** Error message about missing CONFIG table

**Solution:**
- The table name is case-sensitive (`CONFIG` not `config`)
- Latest version handles this automatically
- Ensure you're using NetWorx and not a different monitoring tool
- Try running NetWorx once to initialize the database

#### Script Works But Trial Still Expired

**Problem:** Trial period not reset after running script

**Solution:**
- Make sure NetWorx was fully closed before running script
- Restart your computer after running the script
- Clear NetWorx cache in `%APPDATA%\NetWorx\`
- Check if your NetWorx version uses a different database structure

---

## ⚙️ Advanced Configuration

### Custom Database Path

If NetWorx is installed in a non-standard location:

```python
update_networx_config(db_path=r'C:\Custom\Path\NetWorx.db3')
```

### Modify Trial Duration

To change the trial duration from 30 days:

```python
reminder_date = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d')
#                                              ^^
#                        Change 30 to your preferred number of days
```

### Schedule Automatic Resets

You can use Windows Task Scheduler to run this script automatically:

1. Open Task Scheduler
2. Create a new task
3. Set trigger (e.g., every 25 days)
4. Action: `python C:\path\to\script.py`
5. Run with highest privileges enabled

---

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- 🍎 Add support for macOS version of NetWorx
- 🐧 Add support for Linux version of NetWorx
- 🎨 More terminal UI themes and color schemes
- 📅 Custom date formats and configurations
- 🔄 Automatic scheduling with built-in task creation
- 🔔 Desktop notifications for successful resets
- 📝 Detailed logging with rotation
- 🔐 Backup and restore functionality

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What This Means

✅ Commercial use  
✅ Modification  
✅ Distribution  
✅ Private use  

❌ Liability  
❌ Warranty  

---

## ⚠️ Disclaimer

**Important Legal Notice:**

- This tool is for **educational and testing purposes only**
- Use at your own risk and responsibility
- This script modifies NetWorx trial data to extend evaluation periods
- **Please support the developers:** If you find NetWorx useful, consider [purchasing a license](https://www.softperfect.com/products/networx/)
- Not affiliated with, endorsed by, or associated with SoftPerfect Research
- Modifying software trials may violate terms of service
- Always maintain proper backups before modifying application databases
- The author is not responsible for any consequences of using this tool

### About NetWorx

NetWorx is developed by [SoftPerfect Research](https://www.softperfect.com/) and offers a legitimate 30-day trial period. If you use NetWorx regularly, please consider supporting the developers by purchasing a license[attached_file:1].

---

## 🙏 Acknowledgments

- [SoftPerfect Research](https://www.softperfect.com/) - For creating NetWorx
- [Rich](https://github.com/Textualize/rich) - For the beautiful terminal interface
- [psutil](https://github.com/giampaolo/psutil) - For cross-platform process utilities
- The Python community for excellent documentation

---

## 📞 Support

Having issues? Here's how to get help:

- 🐛 **Bug Reports:** [Open an issue](https://github.com/almas-cp/Networx-trial-reset/issues)
- 💡 **Feature Requests:** [Open an issue](https://github.com/almas-cp/Networx-trial-reset/issues)
- 💬 **Questions:** [Start a discussion](https://github.com/almas-cp/Networx-trial-reset/discussions)

For NetWorx-specific issues, please contact [SoftPerfect Support](https://www.softperfect.com/support/)[attached_file:1].

---

## 📚 Additional Resources

- [NetWorx Official Website](https://www.softperfect.com/products/networx/)
- [NetWorx Features](https://www.softperfect.com/products/networx/#features)
- [NetWorx Download](https://www.softperfect.com/products/networx/#download)
- [Purchase NetWorx License](https://www.softperfect.com/products/networx/)

---

<div align="center">

**Made with ❤️ and Python**

*If you find NetWorx useful, please support the developers by purchasing a license*

*If you find this tool helpful, consider giving it a ⭐*

[⬆ Back to Top](#-networx-trial-reset)

</div>