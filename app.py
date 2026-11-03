from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from astropy.io import fits

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

st.set_page_config(page_title="DARA Astronomy Practicals Toolkit", layout="wide")
st.title("🔭 DARA Astronomy Practicals Toolkit")
st.caption("Optical astronomy • Radio/RMI measurements • RFI exploration • Data reduction")
st.info(
    "Starter toolkit for learning and portfolio development. RFI candidates are not "
    "automatically confirmed interference; validate them against observing context and instrument documentation."
)

module = st.sidebar.selectbox(
    "Choose a practical",
    [
        "1. Optical Astronomy — FITS image",
        "2. Radio / RMI — time series",
        "3. RFI — frequency spectrum",
        "4. Data Reduction — CSV analysis",
    ],
)

def numeric_summary(values):
    values = np.asarray(values, dtype=float)
    valid = values[np.isfinite(values)]
    if valid.size == 0:
        return None
    return {
        "Valid samples": int(valid.size),
        "Missing/invalid samples": int(values.size - valid.size),
        "Minimum": float(np.min(valid)),
        "Maximum": float(np.max(valid)),
        "Mean": float(np.mean(valid)),
        "Median": float(np.median(valid)),
        "Standard deviation": float(np.std(valid)),
    }

if module.startswith("1."):
    st.header("Optical astronomy: inspect a FITS image")
    uploaded = st.file_uploader("Upload a FITS image (.fits / .fit)", type=["fits", "fit", "fts"])
    if uploaded:
        try:
            with fits.open(uploaded) as hdul:
                image = None
                header = None
                for hdu in hdul:
                    if hdu.data is not None:
                        candidate = np.asarray(hdu.data).squeeze()
                        if candidate.ndim == 2:
                            image = candidate.astype(float)
                            header = hdu.header.copy()
                            break
            if image is None:
                st.error("No 2D image was found in this FITS file.")
            else:
                valid = image[np.isfinite(image)]
                if valid.size == 0:
                    st.error("The image contains no finite pixel values.")
                else:
                    low, high = np.percentile(valid, [1, 99])
                    fig, ax = plt.subplots(figsize=(9, 6))
                    im = ax.imshow(image, origin="lower", cmap="inferno", vmin=low, vmax=high)
                    ax.set_xlabel("Pixel X")
                    ax.set_ylabel("Pixel Y")
                    ax.set_title("Uploaded optical astronomy FITS image")
                    fig.colorbar(im, ax=ax, label="Pixel value")
                    st.pyplot(fig)
                    plt.close(fig)
                    st.subheader("Image summary")
                    st.json({
                        "shape": list(image.shape),
                        "minimum": float(np.min(valid)),
                        "maximum": float(np.max(valid)),
                        "mean": float(np.mean(valid)),
                        "median": float(np.median(valid)),
                        "standard_deviation": float(np.std(valid)),
                    })
                    st.subheader("Selected FITS metadata")
                    st.code("\n".join(
                        f"{k} = {header[k]}" for k in
                        ["OBJECT", "TELESCOP", "INSTRUME", "FILTER", "DATE-OBS", "BUNIT"]
                        if k in header
                    ) or "No common metadata keys found. Inspect the FITS header for details.")
                    st.download_button(
                        "Download image summary JSON",
                        data=pd.Series({
                            "height": image.shape[0], "width": image.shape[1],
                            "mean": float(np.mean(valid)), "median": float(np.median(valid)),
                            "std": float(np.std(valid))
                        }).to_json(indent=2),
                        file_name="optical_image_summary.json",
                        mime="application/json",
                    )
        except Exception as exc:
            st.error(f"Could not read this FITS file: {exc}")
    else:
        st.write("Upload a public or personally collected FITS image to begin.")

elif module.startswith("2."):
    st.header("Radio / RMI: explore measurements")
    st.write("Upload a CSV containing at least one numeric measurement column. If available, choose time and signal columns.")
    uploaded = st.file_uploader("Upload radio/RMI measurement CSV", type=["csv"], key="radio")
    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            st.write("Preview", df.head(10))
            numeric_cols = df.select_dtypes(include="number").columns.tolist()
            if not numeric_cols:
                st.warning("No numeric columns found in this CSV.")
            else:
                signal_col = st.selectbox("Measurement / signal column", numeric_cols)
                x_options = ["Row number"] + list(df.columns)
                x_col = st.selectbox("Horizontal axis", x_options)
                y = pd.to_numeric(df[signal_col], errors="coerce").to_numpy()
                if x_col == "Row number":
                    x = np.arange(len(df))
                    x_label = "Sample index"
                else:
                    x = df[x_col]
                    x_label = x_col
                fig, ax = plt.subplots(figsize=(10, 4))
                ax.plot(x, y, linewidth=1)
                ax.set_xlabel(x_label)
                ax.set_ylabel(signal_col)
                ax.set_title("Radio / RMI measurement series")
                ax.grid(True, alpha=0.3)
                fig.tight_layout()
                st.pyplot(fig)
                plt.close(fig)
                st.subheader("Measurement statistics")
                st.json(numeric_summary(y))
                st.download_button(
                    "Download cleaned measurement CSV",
                    data=df.assign(**{signal_col: y}).to_csv(index=False),
                    file_name="radio_rmi_measurements.csv",
                    mime="text/csv",
                )
        except Exception as exc:
            st.error(f"Could not process this CSV: {exc}")
    else:
        st.caption("No training file? Use the sample CSV included in the project folder.")

elif module.startswith("3."):
    st.header("RFI: explore a frequency spectrum")
    st.write("Upload frequency and measured-power columns. Threshold flags are exploratory only, not proof of RFI.")
    uploaded = st.file_uploader("Upload spectrum CSV", type=["csv"], key="rfi")
    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            numeric_cols = df.select_dtypes(include="number").columns.tolist()
            if len(numeric_cols) < 2:
                st.warning("Please provide at least two numeric columns: frequency and power.")
            else:
                freq_col = st.selectbox("Frequency column", numeric_cols, key="freq")
                other_cols = [c for c in numeric_cols if c != freq_col]
                power_col = st.selectbox("Power / intensity column", other_cols, key="power")
                threshold_pct = st.slider("Exploratory high-power threshold percentile", 80, 99, 95)
                freq = pd.to_numeric(df[freq_col], errors="coerce").to_numpy(dtype=float)
                power = pd.to_numeric(df[power_col], errors="coerce").to_numpy(dtype=float)
                valid = np.isfinite(freq) & np.isfinite(power)
                if not valid.any():
                    st.error("No valid frequency/power rows were found.")
                else:
                    cutoff = float(np.percentile(power[valid], threshold_pct))
                    flagged = valid & (power >= cutoff)
                    fig, ax = plt.subplots(figsize=(10, 4))
                    ax.plot(freq[valid], power[valid], linewidth=1, label="Measured spectrum")
                    ax.axhline(cutoff, linestyle="--", label=f"{threshold_pct}th percentile")
                    ax.scatter(freq[flagged], power[flagged], s=18, label="High-power candidates")
                    ax.set_xlabel(freq_col)
                    ax.set_ylabel(power_col)
                    ax.set_title("RFI exploration spectrum (candidate peaks only)")
                    ax.grid(True, alpha=0.3)
                    ax.legend()
                    fig.tight_layout()
                    st.pyplot(fig)
                    plt.close(fig)
                    st.metric("Exploratory high-power candidates", int(flagged.sum()))
                    st.warning(
                        "High-power points may come from genuine sources, instrumental effects, "
                        "noise, or RFI. Confirm using observing notes, calibration, bandwidth, "
                        "time behaviour, and the instrument's documented units."
                    )
                    result = df.copy()
                    result["valid_row"] = valid
                    result["high_power_candidate"] = flagged
                    result.to_csv(OUT / "rfi_candidates.csv", index=False)
                    st.download_button(
                        "Download flagged spectrum CSV",
                        data=result.to_csv(index=False),
                        file_name="rfi_candidates.csv",
                        mime="text/csv",
                    )
        except Exception as exc:
            st.error(f"Could not process this spectrum: {exc}")
    else:
        st.caption("Upload a spectrum CSV from your practical or use the included example.")

else:
    st.header("Data reduction: clean and summarize CSV data")
    uploaded = st.file_uploader("Upload a measurement CSV", type=["csv"], key="reduce")
    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            st.write("Raw data preview", df.head(10))
            numeric_cols = df.select_dtypes(include="number").columns.tolist()
            if numeric_cols:
                selected = st.multiselect("Numeric columns to summarize", numeric_cols, default=numeric_cols)
                cleaned = df.copy()
                for col in selected:
                    cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")
                summary = cleaned[selected].describe().T if selected else pd.DataFrame()
                st.subheader("Descriptive statistics")
                st.dataframe(summary)
                st.write(f"Rows: {len(df)} | Columns: {len(df.columns)}")
                st.write("Missing values per column")
                st.dataframe(cleaned.isna().sum().rename("missing values").to_frame())
                st.download_button(
                    "Download processed CSV",
                    data=cleaned.to_csv(index=False),
                    file_name="reduced_astronomy_data.csv",
                    mime="text/csv",
                )
                st.download_button(
                    "Download statistics CSV",
                    data=summary.to_csv(),
                    file_name="data_reduction_summary.csv",
                    mime="text/csv",
                )
            else:
                st.warning("No numeric columns found.")
        except Exception as exc:
            st.error(f"Could not reduce this CSV: {exc}")
    else:
        st.write("Upload any supported measurement CSV to inspect missing values and calculate summary statistics.")

st.divider()
st.caption("AstroBridge Africa • DARA-inspired learning project • Cite and document the origin of every dataset.")
