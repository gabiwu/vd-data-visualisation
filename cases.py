from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models import Legend
# Adding a colour palette based on a defining 'factor'... City
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues9
from bokeh.embed import components
import pandas

# Read in CSV - Using Panda library
df = pandas.read_csv('cases.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

output_file('cases.html')

# City list
city_list = source.data['City'].tolist()

# Add plot
p = figure(
    y_range=city_list,
    plot_width=800,
    plot_height=600,
    title='Highest COVID-19 Cases in England',
    x_axis_label='Total Cases',
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph - Horizontal bar plot
p.add_layout(Legend(), 'right')

p.hbar(
    y='City',
    right='CulmulativeTotal',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'City',
        palette=Blues9,
        factors=city_list
    ),
    fill_alpha=0.9,
    source=source,
    legend_group='City'
)

# Add Legend
#p.legend.orientation = 'vertical'
#p.legend.location = 'top_right'
#p.legend.label_text_font_size = '10px'

# Add Tootltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@City</h3>
    <div><strong>Population: </strong>@Population</div>
    <div><strong>Week Total: </strong>@WeekTotal</div>
    <div><strong>Total Cases: </strong>@CulmulativeTotal</div>
    <div><img src="@Image" alt="" width="200" /></div>
  </div>
"""
p.add_tools(hover)

# Show results
# show(p)

# Save file
save(p)

# Print out div and script
#script, div = components(p)
# print(div)
# print(script)
