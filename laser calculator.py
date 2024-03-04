import math

class Material:
    def __init__(self, name, melting_point, tensile_strength, refractive_index):
        self.name = name
        self.melting_point = melting_point
        self.tensile_strength = tensile_strength
        self.refractive_index = refractive_index

class Laser:
    def __init__(self, type, wavelength, power):
        self.type = type
        self.wavelength = wavelength
        self.power = power

def calculate_laser_power(material, laser, process):
    if process == "welding":
        laser_power = (material.melting_point * material.tensile_strength * welding_speed * welding_time) / (laser.wavelength * laser.pulse_duration * laser.repetition_rate)
    elif process == "cutting":
        laser_power = laser.power * cutting_time
    else:
        raise ValueError("Invalid process")

    return laser_power

# Example usage

# Define some materials
steel = Material("Steel", 1454, 500, None)
glass = Material("Glass", 801, None, 1.52)

# Define some lasers
femtosecond_laser = Laser("Femtosecond laser", 1030, None)
co2_laser = Laser("CO2 laser", 10.6, 100)

# Calculate the laser power for welding steel with a femtosecond laser
welding_speed = 1  # in mm/s
welding_time = 3  # in s
laser_power = calculate_laser_power(steel, femtosecond_laser, "welding")
print("Laser power for welding steel with a femtosecond laser:", laser_power, "W")

# Calculate the laser power for cutting glass with a CO2 laser
cutting_time = 3  # in s
laser_power = calculate_laser_power(glass, co2_laser, "cutting")
print("Laser power for cutting glass with a CO2 laser:", laser_power, "W")