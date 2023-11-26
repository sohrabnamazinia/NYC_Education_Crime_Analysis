from shapely.geometry import Point, Polygon

def find_borough(lat, lon):
    point = Point(lon, lat)

    # Define approximate boundaries for each borough
    bronx_polygon = Polygon([
        (-73.9339, 40.7855),
        (-73.9092, 40.7985),
        (-73.825, 40.886),
        (-73.887, 40.9172),
        (-73.9339, 40.7855)
    ])

    brooklyn_polygon = Polygon([
        (-74.0419, 40.5708),
        (-73.8331, 40.5902),
        (-73.8554, 40.6413),
        (-73.8672, 40.6565),
        (-73.9481, 40.7004),
        (-74.0419, 40.5708)
    ])

    manhattan_polygon = Polygon([
        (-74.0192, 40.6975),
        (-73.9339, 40.7855),
        (-73.9092, 40.799),
        (-73.9651, 40.878),
        (-74.0192, 40.6975)
    ])

    queens_polygon = Polygon([
        (-73.7004, 40.4774),
        (-73.8061, 40.4774),
        (-73.8061, 40.7928),
        (-73.7004, 40.7928),
        (-73.7004, 40.4774)
    ])

    staten_island_polygon = Polygon([
        (-74.2591, 40.4774),
        (-74.034, 40.4774),
        (-74.034, 40.6511),
        (-74.2591, 40.6511),
        (-74.2591, 40.4774)
    ])

    # Check if the coordinates are within any of the borough boundaries
    if point.within(bronx_polygon):
        return 'R'
    elif point.within(brooklyn_polygon):
        return 'K'
    elif point.within(manhattan_polygon):
        return 'M'
    elif point.within(queens_polygon):
        return 'Q'
    elif point.within(staten_island_polygon):
        return 'X'
    else:
        return 'Unknown'

# K: Brooklyn (Kings County)
# M: Manhattan
# Q: Queens
# R: The Bronx (originally "B" for Bronx, but "R" was chosen to avoid confusion with Brooklyn)
# X: Staten Island (Richmond County)