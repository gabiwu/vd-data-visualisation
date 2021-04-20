import pandas
import pandas as pd
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from math import pi
from bokeh.io import output_file, show
from bokeh.palettes import Spectral
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource

# Read in CSV - Using Panda library
df = pandas.read_csv('recoveries.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

# get list
"""Country_list = source.data['Country'].tolist()
Recovered_list = source.data['Recovered'].tolist()
"""
x = df.value_counts()

data = pd.Series(x).reset_index(name='value').rename(columns={'index':'Area'})

data['angle'] = data['Recovered']/data['Recovered'].sum() * 2*pi #radian
data['color'] = Spectral[len(x)]

# Add plot
p = figure(
  plot_height=350,
  title="COVID-19 Recoveries Worldwide Statistics", 
  # #4atoolbar_location=None,
  tools = "pan, box_select, zoom_in, zoom_out, save, reset"
)

# Render glyph - Pie chart
p.wedge(
  x=0, y=1, radius=0.4,
  start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
  line_color="black", fill_color='color', legend_field='Country', source=data
)

# Add Legend
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

# Add Tootltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@Country</h3>
    <div><strong>Population: </strong>@Population</div>
    <div><strong>Cases: </strong>@Cases</div>
    <div><strong>Recovered: </strong>@Recovered</div>
    <div><img src="@Image" alt="@Image" width="200" /></div>
  </div>
"""
p.add_tools(hover)

save(p)
# Show results
show(p)

# Save file
output_file('recoveries.html')