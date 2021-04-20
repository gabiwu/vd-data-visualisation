from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues9
from bokeh.embed import components
import pandas

# Build CSV DataFrame using API to pull data from external CSV
parsedCSV = pandas.read_csv('testing.csv')

# Build Column Data Source
testingDict = ColumnDataSource(
  data=dict(
    cName=ColumnDataSource(parsedCSV).data['CityName'].tolist(),
    cPop=ColumnDataSource(parsedCSV).data['Population'].tolist(),
    cCount=ColumnDataSource(parsedCSV).data['WeeklyCount'].tolist(),
    cImg=ColumnDataSource(parsedCSV).data['CityImage'].tolist()
  )
)

# Define Plot Figure
myPlot = figure(
    x_range=testingDict.data['cName'],
    plot_width=800,
    plot_height=600,
    title='COVID-19 Testing in England',
    x_axis_label='Locations',
    y_axis_label='Total Cases',
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Define Plot Renderers (Line & Circle)
myPlot.line(
  'cName',
  'cCount',
  line_width=2,
  line_color='red',
  legend_label='Weekly Tests in England',
  source=testingDict
)
myPlot.circle(
  'cName', 
  'cCount', 
  fill_color='red', 
  line_color='red', 
  size=8, 
  source=testingDict)

# Add Legend
myPlot.legend.orientation = 'vertical'
myPlot.legend.location = 'top_right'
myPlot.legend.label_text_font_size = '10px'

# Add Mouse-Hover Popup
hover = HoverTool()
hover.tooltips = """
 <div>
   <h3>@cName</h3>
   <div><strong>Population: </strong>@cPop</div>
   <div><strong>Weekly Count: </strong>@cCount</div>
   <div><img src="@cImg" alt="" width="200" /></div>
 </div>
"""
myPlot.add_tools(hover)

# Save file
output_file('testing.html')
save(myPlot)

# Show results
show(myPlot)