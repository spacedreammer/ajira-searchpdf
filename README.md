# 📂 Job Offer PDF Search Tool

**Author:** Issa (SpaceDreammer)  
**Version:** 1.0  
**License:** Apache-2.0 license
**Date:** September 2025  

---

## 📌 Overview

This is a desktop tool built with **Python (Tkinter GUI)** for searching names in official job offer PDFs published on [Ajira](https://www.ajira.go.tz).

The app:

- Scrapes the latest PDF job calling 
- Opens each PDF in memory  
- Extracts table data (MAMLAKA YA AJIRA, KADA, JINA)  
- Searches for the entered name  
- Displays results in a friendly GUI with highlights
- 📌 Currently uploaded pdf will be the one searched

---

## 🚀 How to Run

### 🟦 Option 1: Windows Executable (Recommended)

1. Download the ZIP file and extract it.  
2. Inside, open the `dist/` folder.  
3. Double-click **`JobSearchTool.exe`**.  

✅ No need to install Python or any dependencies.  

⚠️ Note: Since the app is unsigned, **Windows SmartScreen** may show:  
*"Windows protected your PC"*.  
Click **More info → Run anyway**.  

---

### 🟩 Option 2: Linux (Ubuntu/Debian)

#### A) Using `.AppImage` (portable)
1. Download **`JobSearchTool-x86_64.AppImage`**.  
2. Make it executable:  
   ```bash
   chmod +x JobSearchTool-x86_64.AppImage```
3. Run it:
    ```bash
    ./JobSearchTool-x86_64.AppImage
  B) Using .deb package

  Download jobsearchtool_1.0_amd64.deb.

  Install it with:

          sudo dpkg -i jobsearchtool_1.0_amd64.deb

🐍 Option 3: Run from Python Source

If you prefer to run the source code directly:

Requirements

Python 3.8+

Install libraries:

    pip install requests beautifulsoup4 pdfplumber


On Ubuntu, also install Tkinter:

    sudo apt-get install python3-tk
  ```bash
        python3 tik.py


