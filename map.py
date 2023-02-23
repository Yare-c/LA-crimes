from flask import Flask
from crimes import *
import folium

app = Flask(__name__)
m = folium.Map(location=[34.05917017526604, -118.21947176302209])



for power in zip(finale, another_data, crimes_data):
    if power[2] == "VEHICLE - STOLEN":
        folium.Circle(radius=5, color='red', location=[power[0][0], power[0][1]], tooltip=power[1]).add_to(m)
    if power[2] == "BATTERY - SIMPLE ASSAULT":
        folium.Circle(radius=5, color='blue', location=[power[0][0], power[0][1]], tooltip=power[1]).add_to(m)
    if power[2] == "THEFT OF IDENTITY":
        folium.Circle(radius=5, color='black', location=[power[0][0], power[0][1]], tooltip=power[1]).add_to(m)
    if power[2] == "BURGLARY FROM VEHICLE":
        folium.Circle(radius=5, color='green', location=[power[0][0], power[0][1]], tooltip=power[1]).add_to(m)
    if power[2] == "VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)":
        folium.Circle(radius=5, color='pink', location=[power[0][0], power[0][1]], tooltip=power[1]).add_to(m)


@app.route("/")
def map():
    return m.get_root().render()


