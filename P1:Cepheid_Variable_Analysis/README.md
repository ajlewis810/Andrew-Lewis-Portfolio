### Project 1: Cephied Varaibale Star Observation anad Analysis

## Overview
This repository contains the code and analysis for my study of the Cepheid variable star CY Aquarii (CY Aqr). The primary goal of this project was to analyze the star's brightness variations over time, derive its light curve, and perform photometric calibration using a standard reference star. The findings can be used to study the intrinsic properties of CY Aqr, such as its pulsation period, amplitude, and potential distance.

## Objectives
1. Measure the apparent magnitudes of CY Aquarii in the V and R photometric bands using UCLA 24 inch telescope.
2. Calibrate these magnitudes using a standard star.
3. Construct a precise light curve to characterize the star's variability.
4. Analyze the pulsation period and amplitude of CY Aqr.

## Dataset
- **Target Star**: CY Aquarii (CY Aqr), with an approximate apparent magnitude of 11.
- **Reference Star**: Known magnitudes:
  - V-band: 9.70 mag (uncertainty: ±0.0013 mag)
  - R-band: 9.35 mag (uncertainty: ±0.0012 mag)
- **Photometric Data**: Observations were taken over 90 min (full period of CY Aqr) using a CCD camera and standard filters (V and R).

## Key Steps in the Analysis
### 1. Preprocessing
- Imported raw photometric data.
- Cleaned and prepared the dataset for analysis by removing noisy or inconsistent measurements.

### 2. Calibration
- Applied differential photometry to calibrate the apparent magnitudes of CY Aqr using the reference star's known magnitudes.

### 3. Light Curve Construction
- Plotted the apparent magnitudes of CY Aqr as a function of time to generate its light curve.
- Identified periodic variations characteristic of Cepheid variables.

### 4. Period Analysis
- Performed analysis and made use of Period - Luminosity Relationship.
- Calculated the amplitude of variability in the V and R bands.

## Acknowledgments
Special thanks to the UCLA Astro 180 Laboratory for providing the instrumentation and support needed for this project. 
In particular Professor: Dr. Pradip Gatkine
Teaching assistants: Nicholas Ferraro and Aidan Gibbs 
Group Members: Osmin Caceres and Ian Keyes


