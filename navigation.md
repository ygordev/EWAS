  # Atributos da lib PyNMEA2
  ## Descrição dos atributos de uma mensagem NMEA RATTM
        ("Target Number", "target_number", int),
        ("Target Distance", "distance", Decimal),
        ("Bearing from Own Ship", "bearing", Decimal),
        ("Bearing Reference", "brg_ref"), # T / R (True / Relative)
        ("Target Speed", "speed", Decimal),
        ("Target Course over Ground", "cog", Decimal),
        ("Course Units", "cog_unit"), # T / R (True / Relative)
        ("Distance of CPA", "dist_cpa", Decimal),
        ("Time until CPA", "time_cpa", Decimal),
        ("Distance Units", "dist_unit"),  # K / N / S (Kilometers / Knots / Statute miles)
        ("Target Name", "name"),
        ("Target Status", "status"),  # L / Q / T (Lost from tracking process / Query - in process of acquisition / Tracking at the present time)
        ("Target Reference", "reference"), # R, null otherwise
        ("Timestamp (UTC)", "timestamp", timestamp),
        ("Acquisition Type", "acquisition"),  # A / M (Automatic / Manual)
    )

## Descrição dos atributos de uma mensagem NMEA HDT
("Heading", "heading", Decimal),
("True", "hdg_true"),

## Descrição dos atributos de uma mensagem NMEA GPRMC
        ("Timestamp", "timestamp", timestamp),
        ('Status', 'status'), # contains the 'A' or 'V' flag
        ("Latitude", "lat"),
        ("Latitude Direction", "lat_dir"),
        ("Longitude", "lon"),
        ("Longitude Direction", "lon_dir"),
        ("Speed Over Ground", "spd_over_grnd", float),
        ("True Course", "true_course", float),
        ("Datestamp", "datestamp", datestamp),
        ("Magnetic Variation", "mag_variation"),
        ("Magnetic Variation Direction", "mag_var_dir"),
    