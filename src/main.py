from data_loader import load_data, clean_data
from visualization import configure_plots, draw_line_plot, draw_bar_plot, draw_box_plot
from config import INPUT_DATA, OUTPUTS

import pandas as pd

def main():
    # Initial configuration
    configure_plots()
    
    # Data loading and cleaning
    raw_data = load_data(INPUT_DATA)
    cleaned_data = clean_data(raw_data)
    
    # Plots generation
    draw_line_plot(cleaned_data, OUTPUTS['line'])
    draw_bar_plot(cleaned_data, OUTPUTS['bar'])
    draw_box_plot(cleaned_data, OUTPUTS['box'])
    
    print("✅ Visualizations generated succesfully at:", list(OUTPUTS.values()))



if __name__ == "__main__":
    main()