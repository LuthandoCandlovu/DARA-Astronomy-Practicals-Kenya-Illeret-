<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1F3A,50:0E7C86,100:F5B942&height=240&section=header&text=DARA%20Astronomy%20Practicals&fontSize=50&fontColor=ffffff&animation=twinkling&fontAlignY=36&desc=Toolkit%20for%20Optical%20%E2%80%A2%20Radio%20%E2%80%A2%20RFI%20%E2%80%A2%20Data%20Reduction&descSize=18&descAlignY=58" alt="DARA Astronomy Practicals banner" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=F5B942&center=true&vCenter=true&width=720&lines=%F0%9F%94%AD+Inspect+FITS+images+from+optical+telescopes;%F0%9F%93%A1+Explore+radio+%2F+RMI+measurement+time-series;%F0%9F%93%B6+Hunt+for+RFI+candidates+in+frequency+spectra;%F0%9F%93%8A+Reduce+data+and+summarise+it+with+statistics" alt="Typing animation"/>
</a>

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-0B1F3A?style=for-the-badge&logo=python&logoColor=F5B942)
![Streamlit](https://img.shields.io/badge/Streamlit-App-0E7C86?style=for-the-badge&logo=streamlit&logoColor=white)
![Astropy](https://img.shields.io/badge/FITS-Astronomy-F5B942?style=for-the-badge&logo=nasa&logoColor=0B1F3A)
![Platform](https://img.shields.io/badge/Windows-PowerShell-0B1F3A?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning%20Toolkit-0E7C86?style=for-the-badge)

**A Python / Streamlit starter application for exploring four practical areas of astronomy training.**
*Built from the DARA practicals completed in Kenya* 🇰🇪

[✨ Overview](#-overview) •
[🧭 Modules](#-modules) •
[🚀 Quick Start](#-quick-start) •
[📂 Data Formats](#-data-formats) •
[🛣️ Roadmap](#%EF%B8%8F-roadmap)

</div>

---

## ✨ Overview

This toolkit brings the core skills practised in astronomy training into **one interactive browser app**. Pick a practical from the sidebar, upload your data, and explore it visually: no notebooks to juggle, no scripts to rewrite.

<div align="center">

| 🔭 Optical | 📡 Radio / RMI | 📶 RFI | 📊 Data Reduction |
|:---:|:---:|:---:|:---:|
| FITS image inspection | Measurement time-series | Frequency-spectrum exploration | Descriptive statistics |
| `.fits` | `.csv` | `.csv` | `.csv` |

</div>

> [!IMPORTANT]
> **Scientific note.** This is a general-purpose learning toolkit, **not** a reconstruction of a specific DARA Kenya practical. Upload only data you are permitted to use, document its source and units, and check instrument-specific requirements.
> High-power spectrum points are **candidates for investigation**, not automatically confirmed RFI.

---

## 🧭 Modules

<div align="center">

```mermaid
flowchart LR
    A([🌌 DARA Toolkit<br/>app.py]) --> B[🔭 Optical Astronomy]
    A --> C[📡 Radio / RMI]
    A --> D[📶 RFI Spectrum]
    A --> E[📊 Data Reduction]

    B --> B1[/FITS image<br/>2D plane/]
    C --> C1[/CSV time-series<br/>numeric columns/]
    D --> D1[/CSV frequency<br/>+ power/]
    E --> E1[/CSV numeric<br/>fields/]

    B1 --> V[🖼️ Interactive plots<br/>in your browser]
    C1 --> V
    D1 --> V
    E1 --> V

    style A fill:#0B1F3A,stroke:#F5B942,color:#ffffff,stroke-width:2px
    style B fill:#0E7C86,stroke:#0B1F3A,color:#ffffff
    style C fill:#0E7C86,stroke:#0B1F3A,color:#ffffff
    style D fill:#0E7C86,stroke:#0B1F3A,color:#ffffff
    style E fill:#0E7C86,stroke:#0B1F3A,color:#ffffff
    style V fill:#F5B942,stroke:#0B1F3A,color:#0B1F3A,stroke-width:2px
```

</div>

### 🔭 1. Optical Astronomy: FITS Image Inspection
Load a FITS file, inspect its header, and view the 2D image plane. A first step in any imaging pipeline: check the data before you reduce it.

### 📡 2. Radio / RMI Time-Series Exploration
Upload a CSV with one or more numeric measurement columns and watch how signals evolve over time. Useful for spotting drifts, steps, and unusual behaviour.

### 📶 3. RFI Frequency-Spectrum Exploration
Plot measured power against frequency and flag high-power points as **RFI candidates**. Radio-frequency interference is a daily reality for radio telescopes, so the first skill is learning to *see* it.

### 📊 4. General Data Reduction & Descriptive Statistics
Summarise any numeric CSV with mean, median, spread and more, the foundation under every other module.

---

## 🔄 How a Practical Flows

<div align="center">

```mermaid
sequenceDiagram
    autonumber
    actor You as 👩‍🔬 You
    participant App as 🖥️ Streamlit App
    participant Data as 📁 Your Data
    participant Plot as 📈 Visualisation

    You->>App: streamlit run app.py
    App-->>You: Opens in browser 🌐
    You->>App: Choose a practical (sidebar)
    You->>Data: Upload FITS / CSV
    Data->>App: Parse & validate
    App->>Plot: Build plots + statistics
    Plot-->>You: Explore, inspect, interpret ✨
```

</div>

---

## 🚀 Quick Start

### 🪟 Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

<details>
<summary><b>🔒 Activation blocked? Click here</b></summary>

<br/>

Use the virtual environment directly, with no activation needed:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

</details>

The app opens in your browser. Choose a practical from the sidebar and upload a FITS or CSV file as appropriate. 🎉

---

## 📂 Data Formats

| Module | Format | Required content |
|:--|:--:|:--|
| 🔭 **Optical** | `FITS` | An image containing a 2D image plane |
| 📡 **Radio / RMI** | `CSV` | One or more numeric measurement columns |
| 📶 **RFI** | `CSV` | Numeric **frequency** and measured **power** columns |
| 📊 **Data Reduction** | `CSV` | Numeric fields to summarise |

> [!NOTE]
> The toolkit does **not** download training datasets automatically. Obtain data from a documented public archive, or use data you are authorised to share. Always include **attribution, units, instrument details and licensing** where applicable.

---

## 🧪 Reading an RFI Spectrum

<div align="center">

```mermaid
flowchart TD
    S[📶 Spectrum loaded] --> P{Point well above<br/>the noise floor?}
    P -- No --> N[✅ Likely noise / astronomical signal]
    P -- Yes --> C[🚩 Mark as RFI candidate]
    C --> Q{Check context}
    Q --> T[⏱️ Time behaviour]
    Q --> F[📻 Known frequency allocations]
    Q --> O[🔭 Observing setup]
    Q --> I[🛠️ Instrument behaviour]
    T --> R[🧾 Document & decide]
    F --> R
    O --> R
    I --> R

    style S fill:#0B1F3A,stroke:#F5B942,color:#fff
    style C fill:#F5B942,stroke:#0B1F3A,color:#0B1F3A
    style R fill:#0E7C86,stroke:#0B1F3A,color:#fff
```

</div>

A bright spike is a **question, not an answer**. Confirming RFI means considering time, frequency, observing context and instrument behaviour together.

---

## 🛣️ Roadmap

- [ ] 🧪 Add tests and example datasets with known provenance
- [ ] 🌍 Add celestial coordinate handling using **WCS**
- [ ] 📡 Add radio calibration and domain-specific reduction, once the instrument/data format is known
- [ ] 🛡️ Add validated RFI analysis that considers time, frequency, observing context and instrument behaviour

---

## 🗂️ Project Structure

```text
📦 dara-astronomy-practicals
 ┣ 📜 app.py             # Streamlit entry point
 ┣ 📜 requirements.txt   # Python dependencies
 ┗ 📜 README.md          # You are here ✨
```

---

<div align="center">

### 👋 Author

**Luthando Candlovu**
Computer Science Honours Student · South Africa 🇿🇦

[![GitHub](https://img.shields.io/badge/GitHub-LuthandoCandlovu-0B1F3A?style=for-the-badge&logo=github&logoColor=F5B942)](https://github.com/LuthandoCandlovu)

*Built with curiosity under African skies* 🌌

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F5B942,50:0E7C86,100:0B1F3A&height=120&section=footer&animation=twinkling" alt="footer" width="100%"/>

</div>
