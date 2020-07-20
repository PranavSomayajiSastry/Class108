import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("marks.csv")
fig =ff.create_distplot([df ["Marks In Percentage"].tolist()],["Marks In Percentage"])
fig.show()