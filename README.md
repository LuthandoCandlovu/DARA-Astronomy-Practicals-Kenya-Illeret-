<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1F3A,55:0E7C86,100:F5B942&height=230&section=header&text=DARA%20Astronomy%20Practicals&fontSize=50&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=Optical%20%C2%B7%20Radio%20%C2%B7%20RFI%20%C2%B7%20Data%20Reduction&descSize=18&descAlignY=60" alt="DARA Astronomy Practicals banner" width="100%"/>

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1400&color=F5B942&center=true&vCenter=true&width=700&lines=Inspect+FITS+images;Explore+radio+%2F+RMI+time+series;Flag+RFI+candidates+in+frequency+spectra;Reduce+data+and+summarise+it" alt="Typing animation of the four modules"/></a>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-0B1F3A?style=flat-square&logo=python&logoColor=F5B942)
![Streamlit](https://img.shields.io/badge/Streamlit-app-0E7C86?style=flat-square&logo=streamlit&logoColor=white)
![Data](https://img.shields.io/badge/Data-FITS%20%7C%20CSV-0B1F3A?style=flat-square)
![Platform](https://img.shields.io/badge/Windows-PowerShell-0E7C86?style=flat-square&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-learning%20toolkit-F5B942?style=flat-square&labelColor=0B1F3A)

**A Python / Streamlit starter app for four practical areas of astronomy training, developed from the DARA practicals completed in Kenya.**

[Overview](#overview) · [Architecture](#architecture) · [Modules](#modules) · [Quick start](#quick-start) · [RFI workflow](#rfi-workflow) · [Data](#data-formats) · [Roadmap](#roadmap)

</div>

---

## Overview

One interactive browser app for the core skills of astronomy data work. Pick a practical in the sidebar, upload your data, and explore it visually.

<table>
<tr>
<td width="25%" valign="top"><b>01 · Optical</b><br/><sub>FITS images and their 2D image planes</sub></td>
<td width="25%" valign="top"><b>02 · Radio / RMI</b><br/><sub>Measurement time series, one or many columns</sub></td>
<td width="25%" valign="top"><b>03 · RFI</b><br/><sub>Frequency spectra with candidate flagging</sub></td>
<td width="25%" valign="top"><b>04 · Reduction</b><br/><sub>Descriptive statistics for numeric fields</sub></td>
</tr>
</table>

> [!IMPORTANT]
> **Scientific note.** This is a general-purpose learning toolkit, not a reconstruction of a specific DARA Kenya practical. Upload data you are permitted to use, document its source and units, and check instrument-specific requirements. High-power spectrum points are only candidates for investigation; they are not automatically confirmed RFI.

---

## Architecture

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#0B1F3A','primaryTextColor':'#ffffff','primaryBorderColor':'#0E7C86','lineColor':'#F5B942','secondaryColor':'#0E7C86','tertiaryColor':'#0B1F3A','fontFamily':'Segoe UI, Arial'}}}%%
flowchart LR
    IN(["Your data<br/>.fits / .csv"]) --> APP["Streamlit app<br/>app.py"]
    APP --> M1["01 Optical"]
    APP --> M2["02 Radio / RMI"]
    APP --> M3["03 RFI spectrum"]
    APP --> M4["04 Data reduction"]
    M1 --> OUT(["Plots and statistics<br/>in your browser"])
    M2 --> OUT
    M3 --> OUT
    M4 --> OUT
    style APP fill:#0E7C86,stroke:#F5B942,color:#ffffff,stroke-width:2px
    style OUT fill:#F5B942,stroke:#0B1F3A,color:#0B1F3A,stroke-width:2px
```

### Session flow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#0B1F3A','primaryTextColor':'#ffffff','primaryBorderColor':'#0E7C86','lineColor':'#F5B942','actorBkg':'#0B1F3A','actorTextColor':'#ffffff','actorBorder':'#F5B942','signalColor':'#0E7C86','noteBkgColor':'#F5B942','noteTextColor':'#0B1F3A'}}}%%
sequenceDiagram
    autonumber
    actor U as You
    participant A as Streamlit app
    participant D as Your file
    participant P as Plots
    U->>A: streamlit run app.py
    A-->>U: Opens in browser
    U->>A: Choose a practical
    U->>D: Upload FITS or CSV
    D->>A: Parse and validate
    A->>P: Build plots and statistics
    P-->>U: Explore and interpret
    Note over U,P: Interpretation stays with you
```

---

## Modules

| # | Module | Input | What you can do |
|:-:|:--|:-:|:--|
| 01 | **Optical astronomy** | `FITS` | Open an image file and inspect its 2D image plane before any reduction |
| 02 | **Radio / RMI** | `CSV` | Plot numeric measurement columns over time to spot drifts, steps and anomalies |
| 03 | **RFI spectrum** | `CSV` | Plot measured power against frequency and highlight high-power candidates |
| 04 | **Data reduction** | `CSV` | Compute descriptive statistics for any set of numeric fields |

---

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

<details>
<summary><b>PowerShell blocks activation?</b></summary>
<br/>

Use the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

</details>

The app opens in your browser. Choose a practical from the sidebar and upload a FITS or CSV file as appropriate.

---

## RFI workflow

A high-power point is a question, not an answer. Treat it like this:

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#0B1F3A','primaryTextColor':'#ffffff','primaryBorderColor':'#0E7C86','lineColor':'#F5B942','fontFamily':'Segoe UI, Arial'}}}%%
flowchart TD
    S["Spectrum loaded"] --> Q{"Point well above<br/>the noise floor?"}
    Q -- No --> N["Likely noise or<br/>astronomical signal"]
    Q -- Yes --> C["Mark as RFI candidate"]
    C --> T["Time behaviour"]
    C --> F["Frequency context"]
    C --> O["Observing setup"]
    C --> I["Instrument behaviour"]
    T --> R["Document and decide"]
    F --> R
    O --> R
    I --> R
    style C fill:#F5B942,stroke:#0B1F3A,color:#0B1F3A
    style R fill:#0E7C86,stroke:#F5B942,color:#ffffff
```

---

## Data formats

| Module | Format | Required content |
|:--|:-:|:--|
| Optical | FITS | Image containing a 2D image plane |
| Radio / RMI | CSV | One or more numeric measurement columns |
| RFI | CSV | Numeric frequency and measured-power columns |
| Data reduction | CSV | Numeric fields to summarise |

> [!NOTE]
> The toolkit does not download training datasets automatically. Obtain data from a documented public archive, or use data you are authorised to share. Include attribution, units, instrument details and licensing where applicable.

---

## Roadmap

- [ ] Tests and example datasets with known provenance
- [ ] Celestial coordinate handling using WCS
- [ ] Radio calibration and domain-specific reduction, once the instrument and data format are known
- [ ] Validated RFI analysis that considers time, frequency, observing context and instrument behaviour
- [ ] Screenshots and a short demo GIF of each module

---

## Project structure

```text
.
├── app.py              Streamlit entry point
├── requirements.txt    Python dependencies
└── README.md
```

---

<div align="center">

**Luthando Candlovu** · Computer Science Honours · South Africa

[![GitHub](https://img.shields.io/badge/GitHub-LuthandoCandlovu-0B1F3A?style=flat-square&logo=github&logoColor=F5B942)](https://github.com/LuthandoCandlovu)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F5B942,55:0E7C86,100:0B1F3A&height=110&section=footer&animation=twinkling" alt="" width="100%"/>

</div>
