"""
Utility functions for coordinate transformations between
Geodetic Latitude/Longitude (ll) (EPSG:4326)
Antarctic Polar Stereographic (xy) (EPSG:3031)
UTM coordinates (utm)

Derived from Matthew Siegfried's functions of the same purpose.

Zachary Katz
zachary_katz@mines.edu

v1.0
May 2025


Functions
---------
ll2xy
      Convert between Latitude/Longitude and PS71 XY
xy2ll
      Convert between PS71 XY and Latitude/Longitude
utm2ps71
      Convert between UTM coordinates and PS71 XY
ps712utm
      Convert between PS71 XY and UTM coordinates
"""

# Imports
from pyproj import CRS, Transformer


def ll2xy(lon: list[float], lat: list[float]) -> tuple[list[float], list[float]]:
    """
    Transform coordinates from input geodetic coordinates (lon, lat)
    to output Antarctic Polar Stereographic coordinates (x, y).
    Can also take single floats.

    Parameters
    ----------
    lon: list[float]
         Geodetic longitude in EPSG:4326
    lat: list[float]
         Geodetic latitude in EPSG:4326

    Returns
    -------
    x: list[float]
       Antarctic Polar Stereographic (EPSG:3031) x
    y: list[float]
       Antarctic Polar Stereographic (EPSG:3031) y
    """

    crs_ll = CRS("EPSG:4326")
    crs_xy = CRS("EPSG:3031")
    ll_to_xy = Transformer.from_crs(crs_ll, crs_xy, always_xy=True)
    x, y = ll_to_xy.transform(lon, lat)
    return x, y


def xy2ll(x: list[float], y: list[float]) -> tuple[list[float], list[float]]:
    """
    Transform coordinates from Antarctic Polar Stereographic coordinates (x, y)
    to output geodetic coordinates (lon, lat).
    Can also take single floats.

    Parameters
    ----------
    x: list[float]
       Antarctic Polar Stereographic (EPSG:3031) x
    y: list[float]
       Antarctic Polar Stereographic (EPSG:3031) y

    Returns
    -------
    lon: list[float]
         Geodetic longitude in EPSG:4326
    lat: list[float]
         Geodetic latitude in EPSG:4326
    """
    crs_ll = CRS("EPSG:4326")
    crs_xy = CRS("EPSG:3031")
    xy_to_ll = Transformer.from_crs(crs_xy, crs_ll, always_xy=True)
    lon, lat = xy_to_ll.transform(x, y)
    return lon, lat

def utm2ps71(utmx: list[float], utmy: list[float], crs: int) -> tuple[list[float], list[float]]:
    """
    Transform coordinates from input UTM coordinates (utmx, utmy)
    to output Antarctic Polar Stereographic coordinates (x, y)
    Can also take lists of floats!

    Parameters
    utmx - UTM x coordinate [float]
    utmy - UTM y coordinate [float]
    crs - EPSG code of UTM projection [int]

    Returns
    x - Antarctic Polar Stereographic (EPSG:3031) x [float]
    y - Antarctic Polar Stereographic (EPSG:3031) y [float]

    """
    
    crs_utm = CRS(f"EPSG:{crs}")
    crs_xy = CRS("EPSG:3031")
    ll_to_xy = Transformer.from_crs(crs_utm, crs_xy, always_xy = True)
    x, y = ll_to_xy.transform(utmx, utmy)
    return x, y

def ps712utm(x: list[float], y: list[float], crs: int) -> tuple[list[float], list[float]]:
   """
   Transform coordinates from input Antarctic Polar Stereographic coordinates 
   (x, y)UTM coordinates (utmx, utmy) to output UTM coordinates (utmx, utmy)
   Can also take lists of floats!

   Parameters
   x - Antarctic Polar Stereographic (EPSG:3031) x [float]
   y - Antarctic Polar Stereographic (EPSG:3031) y [float]
   crs - EPSG code of UTM projection [int]

   Returns
   utmx - UTM x coordinate [float]
   utmy - UTM y coordinate [float]
   """
   
   crs_utm = CRS(f"EPSG:{crs}")
   crs_xy = CRS("EPSG:3031")
   ll_to_xy = Transformer.from_crs(crs_xy,crs_utm, always_xy = True)
   utmx, utmy = ll_to_xy.transform(x, y)
   return utmx, utmy
