<div align="center">

# 🌐 NetWorx Database Patcher

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/platform-windows-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
</p>

<p align="center">
  <strong>A beautiful CLI tool to manage NetWorx trial and reminder dates</strong>
</p>

<p align="center">
  Automatically updates NetWorx database configuration with elegant terminal UI
</p>

</div>

---

## ✨ Features

- 🎨 **Beautiful Terminal UI** - Rich, colorful output with tables and progress indicators
- 🔄 **Automatic Process Management** - Safely stops and restarts NetWorx during updates
- 🔍 **Smart Detection** - Automatically finds NetWorx installation path
- 📅 **Date Management** - Updates trial and reminder dates intelligently
- ⚡ **Fast & Reliable** - Quick execution with comprehensive error handling
- 📊 **Visual Feedback** - Clear before/after comparison of updated values

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- NetWorx installed on Windows
- Administrator privileges (recommended)

### Installation

1. Clone or download this repository:
```bash
git clone [repository-url]
cd networx-patcher
```

2. Install required dependencies:
```bash
pip install rich psutil
```

### Usage

Simply run the script:
```bash
python script.py
```

The script will:
1. 🔍 Locate your NetWorx installation
2. ⏸️ Stop the NetWorx process
3. 📝 Update the database with current dates
4. ▶️ Restart NetWorx automatically

## 📋 What It Does

The script modifies two key parameters in the NetWorx configuration database:

| Parameter | Updated To |
|-----------|------------|
| `TrialDate` | Current system date |
| `NextReminder` | Current date + 30 days |

## 🎯 How It Works

```
┌─────────────────────────────────────┐
│  1. Find NetWorx Installation      │
│  2. Stop Running Process            │
│  3. Connect to SQLite Database      │
│  4. Update Configuration Values     │
│  5. Commit Changes                  │
│  6. Restart NetWorx                 │
└─────────────────────────────────────┘
```

## 📸 Screenshot

The script provides a beautiful terminal interface with:
- Color-coded status messages
- Progress spinners for operations
- Before/after comparison tables
- Clear success/error indicators

## 🛠️ Technical Details

### Database Location
```
C:\ProgramData\SoftPerfect\NetWorx\NetWorx.db3
```

### Dependencies
- `sqlite3` - Database operations
- `rich` - Terminal UI and formatting
- `psutil` - Process management
- `pathlib` - Path handling
- `datetime` - Date calculations

### Supported Installation Paths
The script automatically checks:
- `C:\Program Files\NetWorx\`
- `C:\Program Files (x86)\NetWorx\`
- `C:\Program Files\SoftPerfect\NetWorx\`
- `C:\Program Files (x86)\SoftPerfect\NetWorx\`

## ⚠️ Important Notes

- 🔐 Run with administrator privileges for best results
- 💾 The script automatically backs up by stopping NetWorx before modifications
- 🔄 NetWorx will be restarted automatically after updates
- ⚡ Safe to run multiple times - idempotent operation

## 🐛 Troubleshooting

### Database Not Found
Ensure NetWorx is installed in the default location or modify the `db_path` parameter.

### Permission Denied
Run your terminal as Administrator.

### NetWorx Won't Restart
Manually start NetWorx from the Start menu or installation directory.

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⚡ Disclaimer

This tool is for educational purposes. Use at your own risk. Always ensure you have proper backups before modifying application databases.

---

<div align="center">
  <p>Made with ❤️ and Python</p>
  <p>
    <sub>If you find this useful, consider giving it a ⭐</sub>
  </p>
</div>
