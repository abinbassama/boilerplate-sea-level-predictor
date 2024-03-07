import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig,ax=plt.subplots()

    ax.scatter('Year','CSIRO Adjusted Sea Level',data=df)

    # Create first line of best fit
    result=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    ax.axline((0, result.intercept), slope=result.slope, color='Red',label='Best Fit Line')



    # Create second line of best fit
    df_new=df[(df['Year']>=2000)]
    result2 = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    ax.axline((0, result2.intercept), slope=result2.slope, color='Green', label='Best Fit Line First')
    # Add labels and title
    ax.set_xlim(1860, 2070)
    ax.set_ylim(-5, 20)
    ax.axline((0, result2.intercept), slope=result2.slope, color='Green', label='Best Fit Line Second')
    ax.set_xlabel('Years')
    ax.set_ylabel('Sea Level (Inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
