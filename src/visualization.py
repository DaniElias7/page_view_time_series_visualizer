import os

import matplotlib.pyplot as plt
import seaborn as sns

def configure_plots():
    """General aesthetic configuration for the plots"""
    plt.rcParams['figure.figsize'] = (14, 6)
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 12

def create_output_folder(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

def draw_line_plot(data, output_path):
    """Generate the line plot"""
    create_output_folder(output_path)

    fig, ax = plt.subplots()
    ax.plot(data.index, data['value'], color='firebrick', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig(output_path)
    plt.close()
    return fig

def draw_bar_plot(data, output_path):
    """Generate the bar plot"""
    create_output_folder(output_path)

    df = data.copy()
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    monthly_avg = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = monthly_avg.plot(kind='bar', figsize=(10, 7)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[m[:3] for m in monthly_avg.columns])
    plt.tight_layout()
    fig.savefig(output_path)
    plt.close()
    return fig

def draw_box_plot(data, output_path):
    """Generate the boxplots"""
    create_output_folder(output_path)

    df = data.copy()
    df['Year'] = df.index.year
    df['Month'] = df.index.strftime('%b')
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 8))
    
    sns.boxplot(x='Year', y='value', data=df, ax=ax1, palette='viridis')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    sns.boxplot(x='Month', y='value', data=df, ax=ax2, order=months_order, palette='icefire')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    plt.tight_layout()
    fig.savefig(output_path)
    plt.close()
    return fig