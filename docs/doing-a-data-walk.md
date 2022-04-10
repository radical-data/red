# Doing a Data Walk

<!-- Apps:

- [Echoes](https://echoes.xyz/)
- [Open GPS Tracker](https://wiki.openstreetmap.org/wiki/Open_GPS_Tracker) -->

## Apps for recording data

There are apps that allow you to track your walk while adding photos, videos, sound files or notes.

In general, there are more and higher quality GPS apps for Android mobiles. I recommend OSMAnd for Android users and GPXTracker (optionally combined with GeotagPhotosTagger) for iOS.

| App | Platform | Multimedia waypoints |
| --- | --- | --- |
| [OSMAnd](https://osmand.net/) | Android and iOS, but with limitations on iOS | :heavy_check_mark: on Android |
| [GPXTracker](https://wiki.openstreetmap.org/wiki/OpenGpxTracker) | iOS | :x: |
| OpenGPSTrackker | Android and iOS | :x: |

### OSMAnd

- Download [OSMAnd](https://osmand.net/) app to your mobile. It is available for Android and iOS
- For Android, if you want to add multimedia: Enable the audio/video notes plugin https://osmand.net/features/audio-video-notes-plugin
- Press record, do the walk. Add photos, audio notes or videos as you go, they will be linked to the map.
- When you finish press 'Stop'. Your walk will be saved to your phone
- You can access the saved file in My Places > Tracks. From here, you can view the walk within the app in the 'Visible' folder
- Here, you can also see the folder called 'Rec'. Opening it, you will see any walk you have done. You can use 'Share' to get it onto your computer.

Note for iOS users: OSMAnd are planning to add the audio/video notes plugin to the iOS app in 2022.

### GPXTracker

You can add and name waypoints.

### Extras

#### GeotagPhotosTagger

If you want to use photos and have an iphone, you can use GeotagPhotosTagger to combine the photos with the gpx file. This means you can combine photos from a dSLR to the walk.

#### Any app (or paper)

Can use any app and then join the data to the gpx after with either the geocode or, more easily a timestamp.

[Add Python code to automate this]

## Tools for visualising

Import in:

- Python, can use [gpxpy](https://pypi.org/project/gpxpy/)
- R, can use [gpx]()

Visualise with:

- Python: [gpxlotter](https://pypi.org/project/gpxplotter/), based on matplotlib and folium
- [JOSM](https://josm.openstreetmap.de/): software for visualising and editing data with Open Street Maps
- [QGIS](https://qgis.org)



Tutorial:

- in Python: [Build interactive GPS activity maps from GPX files usingfolium](https://towardsdatascience.com/build-interactive-gps-activity-maps-from-gpx-files-using-folium-cf9eebba1fe7)
- in R: [Visualising GPX hiking data and photos with leaflet](https://marionlouveaux.fr/blog/gpx-tracks-and-leaflet-interactive-map/)
- no code, with Google Maps: [How To Add a GPX File to Google Maps](https://www.alphr.com/gpx-google-maps/)
