# 🌐 NetWorx Trial Reset

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**A beautiful CLI tool to automatically manage NetWorx trial and reminder dates**

*Stop worrying about trial expirations with elegant automation*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Troubleshooting](#-troubleshooting)

</div>

---

## 🎯 Overview

**NetWorx Trial Reset** is a sleek Python script that automatically updates your NetWorx database configuration with smart date management. Built with a beautiful terminal interface powered by Rich, it handles the entire process seamlessly - from stopping the NetWorx service to updating the database and restarting it.

### Why Use This?

- 🎨 **Beautiful Terminal UI** - Rich, colorful output with progress indicators and tables
- 🔄 **Zero Manual Work** - Fully automated process management
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
  - Updates `TrialDate` to current system date
  - Sets `NextReminder` to 30 days ahead
  - Proper date formatting (YYYY-MM-DD)

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

- **Python 3.7+** installed on your system
- **NetWorx** installed on Windows
- **Administrator privileges** (recommended for process management)

### Step 1: Clone the Repository

