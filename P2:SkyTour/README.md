# **Messier Object Observation Simulator**

This project analyzes and visualizes the altitude and azimuthal angles of celestial objects, specifically focusing on Messier objects, as observed from the Keck Observatory (or other specified locations) at a given time. The tool is designed for amateur astronomers, researchers, and students interested in simulating sky observations for specific dates and locations.

---

## **Features**
- Computes and visualizes **altitude** and **azimuth** angles for celestial objects over a range of time.
- Allows customization of location and time for observations.
- Includes a sample implementation for **M33 (Triangulum Galaxy)** and additional celestial targets like Jupiter, Venus, and Mars.
- Generates visual plots of the observed altitude and azimuth across a night.
- Saves the final altitude plot as a **PDF** for sharing or documentation purposes.

---

## **Code Workflow**
1. **Setup**: 
   - The code initializes libraries such as `numpy`, `matplotlib`, and `astropy` for calculations and plotting.
   - Configures the observation location (Keck Observatory by default) with latitude, longitude, and elevation.

2. **Target Selection**:
   - A list of celestial objects can be analyzed. 
   - The code demonstrates this with `M33`, Jupiter, Venus, and Mars.

3. **Time Frame**:
   - Observations span the night of **November 12, 2023**, starting at sunset (6 PM) and ending at sunrise (7 AM).

4. **Altitude and Azimuth Calculation**:
   - Transforms sky coordinates into **AltAz** for a specified time and location.
   - Visualizes the changing altitude and azimuth as a function of time.

5. **Plotting**:
   - Altitude and azimuth are plotted over time.
   - Results are presented in **degrees** on the y-axis and **local time** (LST/UT) on the x-axis.

## **Customization Options**
- **Observation Location**: Change the `EarthLocation` parameters to use a different latitude, longitude, or elevation.
- **Observation Time**: Modify the `Time` object to specify a new observation date or time range.
- **Targets**: Add or replace celestial objects in the `target_list`.

---

## **Future Improvements**
- Automate the inclusion of all 110 Messier objects.
- Add labels for sunrise, sunset, and midnight for better interpretability.
- Integrate with external APIs for live sky data.

---

## **Contributors**
- Dr. Fitzgerald from UCLA Astronomy 142 who wrote this assignemnt and helped me through theh project. 
