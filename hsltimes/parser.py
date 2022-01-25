from hsltimes import reader
from pathlib import Path
import pandas as pd
home = str(Path.home())




class Parser():
    def __init__(self):
        self.__filereader = reader.TextFileReader()
        self.__stops_file = self.__filereader.read_data(f"{home}/.local/share/hsltimes/stops.txt")
        self.__stop_times_file = self.__filereader.read_data(f"{home}/.local/share/hsltimes/stop_times.txt")
        self.__routes_file = self.__filereader.read_data(f"{home}/.local/share/hsltimes/routes.txt")
        self.__trips_file = self.__filereader.read_data(f"{home}/.local/share/hsltimes/trips.txt")



    def generate_all(self):
        routes = open(f"{home}/.local/share/hsltimes/routes.txt", "r")


        df = pd.read_csv(routes)
        print(df.loc[df["route_short_name"] == "502"])



# pysakit: {
#     majurinpolku_1: {
#         502: {
#            aikataulu: {
#                ma: [00.05, 00.35, 00.55...],
#                ti: [00.05, 00.35, 00.55...],
#                ke: [00.05, 00.35, 00.55...],
#                to: [00.05, 00.35, 00.55...],
#                pe: [00.05, 00.35, 00.55...],
#           }
#         }
#         113: {
#            aikataulu: {
#                ma: [00.05, 00.35, 00.55...],
#                ti: [00.05, 00.35, 00.55...],
#                ke: [00.05, 00.35, 00.55...],
#                to: [00.05, 00.35, 00.55...],
#                pe: [00.05, 00.35, 00.55...],
#           }
#         }
#     },
#     majurinpolku_2: {
#         502: {
#            aikataulu: {
#                ma: [00.05, 00.35, 00.55...],
#                ti: [00.05, 00.35, 00.55...],
#                ke: [00.05, 00.35, 00.55...],
#                to: [00.05, 00.35, 00.55...],
#                pe: [00.05, 00.35, 00.55...],
#           }
#         }
#         113: {
#            aikataulu: {
#                ma: [00.05, 00.35, 00.55...],
#                ti: [00.05, 00.35, 00.55...],
#                ke: [00.05, 00.35, 00.55...],
#                to: [00.05, 00.35, 00.55...],
#                pe: [00.05, 00.35, 00.55...],
#           }
#         }
#     },
# }