def orbital_period(semi_major_axis, central_mass):
    """
    Calculate the orbital period of a satellite using Kepler's third law.

    Args:
    semi_major_axis (float): Semi-major axis of the orbit in meters.
    central_mass (float): Mass of the central body around which the satellite orbits in kilograms.

    Returns:
    float: Orbital period in seconds.
    """
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    period = 2 * 3.14159 * (semi_major_axis ** 3 / (G * central_mass)) ** 0.5
    return period

# Example usage:
# Earth's mass ~ 5.972e24 kg, GEO orbit semi-major axis ~ 42,164 km
# orbital_period(42164000, 5.972e24)

print('Earth orbital period in seconds: ' + str(orbital_period(42164000, 5.972e24)))
