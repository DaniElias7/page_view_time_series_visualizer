# freeCodeCamp Forum Time Series Visualization

Analysis and visualization of daily page views on the freeCodeCamp forum (2016-2019) using Python, Pandas, Matplotlib, and Seaborn.

## Description

This project generates three types of visualizations from page view data:
1. **Line Chart**: Daily temporal trend
2. **Bar Chart**: Monthly averages by year
3. **Box Plots**: Annual distribution and monthly seasonality

## Requirements

- Python 3.8+
- Libraries:
  ```bash
  pandas
  matplotlib
  seaborn
  numpy
  ```

## Installation

1. Clone repository:
   ```bash
   git clone https://github.com/DaniElias7/page_view_time_series_visualizer
   cd page_view_time_series_visualizer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 
## Usage

Run main script:
   ```bash
   python src/main.py
   ```
**Generated Outputs**:

- outputs/line_plot.png
- outputs/bar_plot.png
- outputs/box_plot.png

## License
MIT 
