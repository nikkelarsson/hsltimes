import os
from pathlib import Path

import pandas as pd
from hsltimes import reader

home = str(Path.home())

class Schedules():
    def __init__(self, stop_name, bus_number):
        stops_file = reader.TextFileReader().read_data(f"{home}/.local/share/hsltimes/stops.txt")
        routes_file = reader.TextFileReader().read_data(f"{home}/.local/share/hsltimes/routes.txt")
        stoptimes_file = reader.TextFileReader().read_data(f"{home}/.local/share/hsltimes/stop_times.txt")

        self.__df_stops = pd.read_csv(stops_file)
        self.__df_routes = pd.read_csv(routes_file)
        self.__df_stoptimes = pd.read_csv(stoptimes_file)

        self.validate_arguments(stop_name, bus_number)
        self.validate_bus_number(bus_number)
        self.validate_stop_name(stop_name)

        self.__FOLDER = "week_schedule"
        self.__BUS_NUM = bus_number
        self.__STOP_NAME = stop_name.lower()


    def validate_arguments(self, stop_name, bus_number):
        if not isinstance(stop_name, str) or not isinstance(bus_number, str):
            raise ValueError("Parser class arguments needs to be in string format")

    def validate_bus_number(self, bus_number):
        df_routes = self.__df_routes
        if bus_number not in df_routes["route_short_name"].values:
            raise ValueError(f"Bus number {bus_number} does not exist")

    def validate_stop_name(self, stop_name):
        df_stops = self.__df_stops
        stop_name = stop_name.capitalize()
        if stop_name not in df_stops["stop_name"].values:
            raise ValueError(f"Stop name {stop_name} does not exist")


    def generate_all(self):
        df_stops = self.__df_stops
        df_routes = self.__df_routes
        df_stoptimes = self.__df_stoptimes

        # GET DESIRED STOP WITH STOP NAME
        df_stops = df_stops[df_stops["stop_name"] == self.__STOP_NAME.capitalize()]

        # GET STOP_ID
        stop_id = df_stops.iloc[0]["stop_id"]


        # GET ENTIRE SCHEDULE OF THE DESIRED STOP
        df_stoptimes = df_stoptimes[df_stoptimes["stop_id"] == stop_id].reset_index(drop = True)

        # GET ROUTE_ID FOR BUS
        route_id = df_routes[df_routes["route_short_name"] == self.__BUS_NUM]["route_id"].iloc[0]

        # GET SCHEDULE FOR PARTICULAR BUS
        df_stoptimes = df_stoptimes[df_stoptimes["trip_id"].str.startswith(route_id, na = False)].reset_index(drop = True)

        # CLEAN OUT ALL COLUMNS EXCEPT TRIP_ID AND DEPARTURE_TIME
        df_stoptimes = df_stoptimes[["trip_id", "departure_time"]]

        # ADD NEW COLUMN FOR BUS_NUM
        df_stoptimes["bus_num"] = self.__BUS_NUM



        # GET SCHEDULE FOR WEEKDAYS
        # MONDAY
        df_ma = df_stoptimes[df_stoptimes["trip_id"].str.contains("Ma", na = False)].reset_index(drop = True)

        # # TUESDAY
        df_ti = df_stoptimes[df_stoptimes["trip_id"].str.contains("Ti", na = False)].reset_index(drop = True)

        # # WEDNESDAY
        df_ke = df_stoptimes[df_stoptimes["trip_id"].str.contains("Ke", na = False)].reset_index(drop = True)

        # # THURSDAY
        df_to = df_stoptimes[df_stoptimes["trip_id"].str.contains("To", na = False)].reset_index(drop = True)

        # # FRIDAY
        df_pe = df_stoptimes[df_stoptimes["trip_id"].str.contains("Pe", na = False)].reset_index(drop = True)

        # # SATURDAY
        df_la = df_stoptimes[df_stoptimes["trip_id"].str.contains("La", na = False)].reset_index(drop = True)

        # # SUNDAY
        df_su = df_stoptimes[df_stoptimes["trip_id"].str.contains("Su", na = False)].reset_index(drop = True)

        # EXPORT ALL DATA
        # CREATE FOLDER NAMED VIA self.__FOLDER
        os.makedirs(self.__FOLDER, exist_ok=True)

        # CREATE ALL CSV DATA
        df_ma.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_maanantai")
        df_ti.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_tiistai")
        df_ke.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_keskiviikko")
        df_to.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_torstai")
        df_pe.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_perjantai")
        df_la.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_lautantai")
        df_su.to_csv(f"{self.__FOLDER}/{self.__STOP_NAME}_sunnuntai")




