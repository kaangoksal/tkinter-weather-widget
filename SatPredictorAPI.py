import requests
from datetime import datetime


class SatPredictorAPI:

    def __init__(self):
        pass

    def get_sattalite_visibility_data_on_coordinates(self, latitude: float, longitude: float,
                                                     date: datetime = datetime.now(), elevation: float = 10.0,
                                                     glonass: bool = True, gps: bool = True):
        """
        Returns an array of sattalite visibilities
        :param latitude:
        :param longitude:
        :param date:
        :param elevation:
        :param glonass:
        :param gps:
        :return:
        """

        url = "http://satpredictor2.deere.com/visibilitydata"

        if glonass:
            glonass = "YES"
        else:
            glonass = "NO"

        if gps:
            gps = "YES"
        else:
            gps = "NO"

        cc = date

        day = str(cc.day)
        month = cc.month
        year = str(cc.year)

        month_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        month_string = month_array[month - 1]

        print(month_string)
        print(day)
        print(year)

        # address=&latitude=33.780141&longitude=-84.389046&isGPS=YES&isGLONASS=YES&eleMask=10.0&tZStr=17&selDate=20+Jun+2018

        payload = "address=&" + "latitude=" + str(latitude) + "&longitude=" + str(longitude) + "&isGPS=" + gps + \
                  "&isGLONASS=" + glonass \
                  + "&eleMask=" + str(elevation) \
                  + "&tZStr=17" \
                    "&selDate=" + str(day) + "+" + str(month_string) + "+" + str(year)

        headers = {
            'accept': "application/json, text/javascript, */*; q=0.01",
            'accept-encoding': "gzip, deflate",
            'Cache-Control': "no-cache",
            'connection': "keep-alive",
            'content-length': "147",
            'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
            'Postman-Token': "1282bf48-5561f-48d9-9ab4-1f13667971e7"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return response.json()

# ssp = SatPredictorAPI()
#
# ssp.get_sattalite_visibility_data_on_coordinates(1,2)
