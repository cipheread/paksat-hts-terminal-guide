#!/usr/bin/env python3
"""
PAKSAT HTS Terminal — Antenna Alignment Wizard
Provides azimuth/elevation lookup and live signal feedback for pointing.
"""

import argparse
import math
import time

# PakSat-MM1 orbital position
PAKSAT_MM1_LONGITUDE = 38.0  # degrees East

# Approximate azimuth/elevation for major Pakistani cities
CITY_TABLE = {
    "karachi":      {"lat": 24.86, "lon": 67.01},
    "lahore":       {"lat": 31.55, "lon": 74.35},
    "islamabad":    {"lat": 33.72, "lon": 73.04},
    "peshawar":     {"lat": 34.01, "lon": 71.57},
    "quetta":       {"lat": 30.19, "lon": 66.99},
    "multan":       {"lat": 30.20, "lon": 71.47},
    "faisalabad":   {"lat": 31.42, "lon": 73.09},
    "hyderabad":    {"lat": 25.38, "lon": 68.37},
    "gwadar":       {"lat": 25.12, "lon": 62.33},
    "gilgit":       {"lat": 35.92, "lon": 74.31},
}


def calc_pointing(site_lat_deg, site_lon_deg, sat_lon_deg=PAKSAT_MM1_LONGITUDE):
    """Calculate azimuth and elevation for a given ground station location."""
    site_lat = math.radians(site_lat_deg)
    delta_lon = math.radians(sat_lon_deg - site_lon_deg)

    # Elevation
    r_earth = 6371.0
    r_orbit = 42164.0
    cos_el = math.cos(site_lat) * math.cos(delta_lon)
    elevation = math.degrees(math.atan(
        (cos_el - r_earth / r_orbit) / math.sqrt(1 - cos_el ** 2)
    ))

    # Azimuth
    azimuth_rad = math.atan2(
        math.tan(delta_lon),
        math.sin(site_lat)
    )
    azimuth = (180 + math.degrees(azimuth_rad)) % 360

    return round(azimuth, 1), round(elevation, 1)


def live_signal_monitor():
    """Simulate live signal quality feedback during alignment."""
    print("\n📡 Live Signal Monitor (Ctrl+C to stop)\n")
    print(f"  {'Time':<10} {'Quality':>10} {'SNR (dB)':>12} {'Status':>12}")
    print("  " + "-" * 48)
    try:
        while True:
            # Replace with actual terminal API call
            quality = 78  # placeholder
            snr = 10.8    # placeholder
            status = "🟢 LOCKED" if quality >= 60 else "🔴 SEARCHING"
            ts = time.strftime("%H:%M:%S")
            print(f"  {ts:<10} {quality:>9}% {snr:>11.1f} {status:>12}", end="\r")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\n  Monitoring stopped.")


def main():
    parser = argparse.ArgumentParser(description="PAKSAT HTS Antenna Alignment Wizard")
    parser.add_argument("--satellite", default="PAKSAT-MM1", help="Target satellite")
    parser.add_argument("--location", help="Lat,Lon e.g. '30.37,69.34'")
    parser.add_argument("--city", help="City name (see supported list)")
    parser.add_argument("--scan", action="store_true", help="Start live signal monitor")
    parser.add_argument("--list-cities", action="store_true", help="List supported cities")
    args = parser.parse_args()

    print(f"\n🛰️  PAKSAT HTS Alignment Wizard — {args.satellite}\n")

    if args.list_cities:
        print("  Supported cities:")
        for city in sorted(CITY_TABLE.keys()):
            d = CITY_TABLE[city]
            az, el = calc_pointing(d["lat"], d["lon"])
            print(f"    {city.title():<15} Az: {az:>6}°   El: {el:>5}°")
        return

    lat, lon = None, None

    if args.city:
        city_key = args.city.lower()
        if city_key not in CITY_TABLE:
            print(f"  ❌ City '{args.city}' not in table. Use --list-cities.")
            return
        d = CITY_TABLE[city_key]
        lat, lon = d["lat"], d["lon"]

    elif args.location:
        try:
            lat, lon = map(float, args.location.split(","))
        except ValueError:
            print("  ❌ Invalid format. Use --location '30.37,69.34'")
            return

    if lat is not None:
        az, el = calc_pointing(lat, lon)
        print(f"  Site Location : {lat:.4f}°N, {lon:.4f}°E")
        print(f"  Azimuth       : {az}° (measured clockwise from True North)")
        print(f"  Elevation     : {el}°")
        print(f"\n  Tip: Set elevation first, then sweep azimuth slowly.")

    if args.scan:
        live_signal_monitor()


if __name__ == "__main__":
    main()
