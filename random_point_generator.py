import numpy as np
import random
from shapely.geometry import Polygon, Point
import pandas as pd

# http://apps.headwallphotonics.com/
# https://medium.com/the-data-journal/a-quick-trick-to-create-random-lat-long-coordinates-in-python-within-a-defined-polygon-e8997f05123a

dirr = "C:\\Users\\carlo\\Desktop\\optim_proj"
poly = pd.read_csv(dirr+"\\polygon_NL.csv", header=0)

poly_NL = Polygon(zip(poly["lat"], poly["lng"]))

def polygon_random_points (poly, num_points, random_func=random.uniform):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point([random_func(min_x, max_x),
                              random_func(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points

n = 15
points = polygon_random_points(poly_NL, n)

lats = []
lngs = []
for p in points:
    #print(p.x, ",", p.y)
    lats.append(p.x)
    lngs.append(p.y)

ids = list(range(1, n+1))
places= list(map(lambda x: "p"+str(x), ids))

places_df = pd.DataFrame()
places_df["id"] = ids
places_df["place"] = places
places_df["lat"] = lats
places_df["lng"] = lngs

places_df.to_csv(dirr+"\\places.csv", index=False)


# =============================================================================
# 
# outside = Point([(25.708811223770937, -100.40932472768554)])
# inside = Point([(25.68947606955076, -100.30392464223632)])
# 
# print(poly_NL.contains(inside))
# print(poly_NL.contains(outside))
# =============================================================================




