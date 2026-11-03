# DARA Astronomy Practicals Toolkit

A Python/Streamlit starter application for exploring four practical areas associated with astronomy training:

1. Optical astronomy FITS-image inspection
2. Radio/RMI measurement time-series exploration
3. RFI frequency-spectrum exploration
4. General data reduction and descriptive statistics

## Important scientific note

This is a general-purpose learning toolkit, not a reconstruction of a specific DARA Kenya practical. Upload data you are permitted to use, document its source and units, and check instrument-specific requirements. High-power spectrum points are only candidates for investigation; they are not automatically confirmed RFI.

## Run on Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If activation is blocked, use the environment directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The app opens in your browser. Choose a practical from the sidebar and upload a FITS or CSV file as appropriate.

## Data formats

- Optical module: FITS image containing a 2D image plane.
- Radio/RMI module: CSV with one or more numeric measurement columns.
- RFI module: CSV with numeric frequency and measured-power columns.
- Data reduction module: CSV with numeric fields to summarize.

The toolkit does not download training datasets automatically. Obtain data from a documented public archive or use data you are authorized to share. Include attribution, units, instrument details, and licensing where applicable.

## Suggested improvements

- Add tests and example datasets with known provenance.
- Add celestial coordinate handling using WCS.
- Add radio calibration and domain-specific reduction only when the instrument/data format is known.
- Add validated RFI analysis that considers time, frequency, observing context, and instrument behaviour.
