import os
import fnmatch
import pysrt
import csv
import simplekml
import piexif

VID_Radius = input("Enter radius for videos")
POI_Radius = input("Enter radius for Point of Interest")

vidPath = "videos"

def getCoordinates(img):
	imgPath = "images"
	coordinates = {}
	if fnmatch.fnmatch(img, "*.JPG"):
		path = '/'.join([imgPath, img])
		exif = piexif.load(path)
		if "GPS" in exif:
			gps = exif["GPS"]
			lat = piexif.GPSIFD.GPSLatitude in gps ? gps[piexif.GPSIFD.GPSLatitude].decode("utf-8"):None
			lat_ref = piexif.GPSIFD.GPSLatitudeRef in gps ? gps[piexif.GPSIFD.GPSLatitudeRef].decode("utf-8"):None
			lon = piexif.GPSIFD.GPSLongitude in gps ? gps[piexif.GPSIFD.GPSLongitude].decode("utf-8"):None
			lon_ref = piexif.GPSIFD.GPSLongitudeRef in gps ? gps[piexif.GPSIFD.GPSLongitudeRef].decode("utf-8"):None
			lat = inDegrees(lat)
			lon = inDegrees(lon)
			if lat_ref != 'N':
                lat = 0 - lat
            if lon_ref != 'E':
            	lon = 0 - lon
            coordinates["lat"] = lat
            coordinates["lon"] = lon
    return coordinates

def inDegrees(value):
	d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)

        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)

        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)

        return d + (m / 60.0) + (s / 3600.0)



