# ENV allpy310

# pip install ephem

import ephem

def mars_visibility(observer_latitude, observer_longitude):
    """
    Determine the next time Mars is visible from a given location on Earth.

    Args:
    observer_latitude (float): Latitude of the observer in degrees.
    observer_longitude (float): Longitude of the observer in degrees.

    Returns:
    str: Date and time when Mars is visible next.
    """
    observer = ephem.Observer()
    observer.lat = str(observer_latitude)
    observer.long = str(observer_longitude)
    mars = ephem.Mars()
    next_rising = observer.next_rising(mars)
    return next_rising.datetime().strftime('%Y-%m-%d %H:%M:%S')

# Example usage:
# mars_visibility(48.8566, 2.3522)  # Paris coordinates

print("Date and time when Mars is visible next in Paris - " + str(mars_visibility(48.8566, 2.3522)))
