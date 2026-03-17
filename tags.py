"""
Foundation-1 tag vocabulary for structured prompt construction.
Based on the RoyalCities Foundation-1 model's training tag hierarchy.
"""

import random

INSTRUMENT_FAMILIES = [
    "Synth", "Keys", "Bass", "Bowed Strings", "Mallet",
    "Wind", "Guitar", "Brass", "Vocal", "Plucked Strings",
]

SUBFAMILIES = {
    "Synth": [
        ("Synth Lead", 40), ("Pluck", 15), ("Pad", 12), ("Supersaw", 10),
        ("FM Synth", 8), ("Wavetable Synth", 8), ("Atmosphere", 4), ("Texture", 3),
    ],
    "Keys": [
        ("Grand Piano", 20), ("Digital Piano", 25), ("Rhodes Piano", 20),
        ("Felt Piano", 8), ("Wurlitzer Piano", 8), ("Clavinet", 6),
        ("Hammond Organ", 6), ("Church Organ", 4), ("Harpsichord", 3),
    ],
    "Bass": [
        ("Wavetable Bass", 25), ("Reese Bass", 20), ("Sub Bass", 18),
        ("Electric Bass", 12), ("Analog Bass", 8), ("FM Bass", 7),
        ("Picked Bass", 5), ("Digital Bass", 5),
    ],
    "Bowed Strings": [
        ("Violin", 35), ("Cello", 30), ("Viola", 10),
        ("Fiddle", 10), ("Digital Strings", 15),
    ],
    "Mallet": [
        ("Bell", 30), ("Marimba", 25), ("Vibraphone", 15),
        ("Glockenspiel", 10), ("Kalimba", 10), ("Xylophone", 10),
    ],
    "Wind": [
        ("Flute", 40), ("Pan Flute", 20), ("Piccolo", 8),
        ("Clarinet", 8), ("Oboe", 6), ("Bassoon", 4),
        ("Ocarina", 6), ("World Winds", 8),
    ],
    "Guitar": [
        ("Electric Guitar", 50), ("Acoustic Guitar", 30), ("Nylon Guitar", 20),
    ],
    "Brass": [
        ("Trumpet", 40), ("Brass", 25), ("French Horn", 10),
        ("Tuba", 8), ("Tenor Trombone", 9), ("Bass Trombone", 8),
    ],
    "Vocal": [
        ("Texture", 45), ("Choir", 25), ("Ensemble", 15), ("Synthetic Choir", 15),
    ],
    "Plucked Strings": [
        ("Harp", 45), ("Concert Harp", 20), ("Celtic Harp", 15),
        ("Koto", 10), ("Sitar", 10),
    ],
}

ALL_SUBFAMILIES = []
for family_subs in SUBFAMILIES.values():
    for name, _ in family_subs:
        if name not in ALL_SUBFAMILIES:
            ALL_SUBFAMILIES.append(name)
ALL_SUBFAMILIES.sort()

TIMBRE_TAGS = [
    "Warm", "Bright", "Tight", "Thick", "Airy", "Rich", "Clean", "Gritty",
    "Crisp", "Focused", "Metallic", "Dark", "Shiny", "Present", "Silky",
    "Sparkly", "Smooth", "Cold", "Buzzy", "Round", "Fat", "Punchy", "Thin",
    "Soft", "Woody", "Hollow", "Nasal", "Biting", "Overdriven", "Subdued",
    "Breathy", "Glassy", "Pizzicato", "Staccato", "Snappy", "Full", "Harsh",
    "Knock", "Muddy", "Steel", "Veiled", "Rubbery", "Rumble", "Noisy",
    "Boomy", "Crispy", "Dreamy", "Heavy", "Tiny", "Spiccato",
]

BAND_TAGS = ["Sub", "Sub Bass", "Bass", "Low Mids", "Mids", "Upper Mids", "Highs", "Air"]

SPATIAL_TAGS = [
    "Wide", "Mono", "Near", "Far", "Spacey", "Ambient",
    "Distant", "Intimate", "Small", "Big", "Deep",
]

WAVE_TECH_TAGS = [
    "Saw", "Square", "Sine", "Triangle", "Pulse", "Analog", "Digital",
    "FM", "Supersaw", "Reese", "Pitch Bend", "White Noise", "Filter",
]

STYLE_TAGS = [
    "Dubstep", "Chiptune", "Acid", "303", "Retro", "Vintage",
    "Laser", "Siren", "FX", "Formant Vocal", "Growl",
]

FX_REVERB = [
    "None", "Low Reverb", "Medium Reverb", "High Reverb", "Plate Reverb",
]
FX_DELAY = [
    "None", "Low Delay", "Medium Delay", "High Delay",
    "Ping Pong Delay", "Stereo Delay", "Cross Delay", "Mono Delay",
]
FX_DISTORTION = [
    "None", "Low Distortion", "Medium Distortion", "High Distortion",
]
FX_MODULATION = [
    "None", "Phaser", "Low Phaser", "Medium Phaser", "High Phaser",
    "Bitcrush", "High Bitcrush",
]

STRUCTURE_TAGS = [
    "None", "Chord Progression", "Dance Chord Progression", "Melody",
    "Top Melody", "Arp", "Bassline",
]

SPEED_TAGS = ["None", "Slow Speed", "Medium Speed", "Fast Speed"]

RHYTHM_TAGS = ["None", "Off Beat", "Alternating", "Triplets", "Strummed", "Arp"]

CONTOUR_TAGS = [
    "None", "Rising", "Falling", "Bounce", "Rolling", "Sustained", "Choppy", "Top",
]

DENSITY_TAGS = ["None", "Simple", "Repeating", "Catchy", "Complex", "Epic"]

KEYS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
SCALES = ["major", "minor"]
BARS_OPTIONS = [4, 8]
BPM_OPTIONS = [100, 110, 120, 128, 130, 140, 150]

FAMILY_EXTRA_TAGS = {
    "Brass": ["Nasal", "Present", "Biting", "Bright", "Big"],
    "Wind": ["Hollow", "Airy", "Breathy", "Thin", "Woody"],
    "Mallet": ["Woody", "Sparkly", "Shiny", "Crisp", "Bright"],
    "Bass": ["Fat", "Punchy", "Tight", "Gritty", "Dark", "Sub Bass", "Bass"],
    "Synth": ["Digital", "Analog", "FM", "Supersaw", "Wide", "Laser", "Saw", "Square"],
    "Keys": ["Warm", "Clean", "Soft", "Rich", "Smooth"],
    "Guitar": ["Crisp", "Woody", "Bright", "Clean", "Gritty"],
    "Vocal": ["Formant Vocal", "Breathy", "Intimate", "Airy"],
    "Bowed Strings": ["Full", "Rich", "Warm", "Smooth", "Intimate"],
    "Plucked Strings": ["Sparkly", "Bright", "Clean", "Airy", "Delicate"],
}


# Weighted FX pools for random generation
FX_REVERB_WEIGHTED = [
    ("Low Reverb", 37), ("Medium Reverb", 45), ("High Reverb", 17), ("Plate Reverb", 1),
]
FX_DELAY_WEIGHTED = [
    ("Low Delay", 28), ("Medium Delay", 25), ("Ping Pong Delay", 27),
    ("Stereo Delay", 10), ("Cross Delay", 3), ("Delay", 4),
    ("High Delay", 2), ("Mono Delay", 1),
]
FX_DISTORTION_WEIGHTED = [
    ("Low Distortion", 35), ("Medium Distortion", 34),
    ("High Distortion", 20), ("Distortion", 11),
]
FX_PHASER_WEIGHTED = [
    ("Phaser", 38), ("Low Phaser", 24), ("Medium Phaser", 19), ("High Phaser", 19),
]
FX_BITCRUSH_WEIGHTED = [("Bitcrush", 95), ("High Bitcrush", 5)]


def _weighted_choice(pool):
    """Pick one item from a list of (name, weight) tuples."""
    names = [n for n, _ in pool]
    weights = [w for _, w in pool]
    return random.choices(names, weights=weights, k=1)[0]


def _pick_n_unique(pool, n):
    """Pick n unique items from a list (plain strings)."""
    return random.sample(pool, min(n, len(pool)))


def generate_random_prompt(mode="simple", family_override=None):
    """
    Generate a random structured prompt for Foundation-1.

    Args:
        mode: "simple" for coherent single-family prompts,
              "experimental" for richer synth-heavy prompts with optional timbre mixing
        family_override: force a specific instrument family, or None for random

    Returns:
        A formatted prompt string (without key/scale/bars/bpm - those are added by the sampler)
    """
    rng = random

    if family_override and family_override != "Random":
        family = family_override
    else:
        family = rng.choice(INSTRUMENT_FAMILIES)

    sub_pool = SUBFAMILIES.get(family, [])
    subfamily = _weighted_choice(sub_pool) if sub_pool else family

    parts = [family]
    if subfamily != family:
        parts.append(subfamily)

    if mode == "experimental":
        n_timbre = rng.randint(4, 7) if family in ("Synth", "Bass") else rng.randint(3, 5)
        n_spatial = rng.randint(1, 3)
        n_wave = rng.randint(2, 4) if family in ("Synth", "Bass") else rng.randint(0, 2)
        n_style = rng.randint(1, 2) if family in ("Synth", "Bass") else rng.randint(0, 1)
    else:
        n_timbre = rng.randint(2, 4)
        n_spatial = rng.randint(0, 2)
        n_wave = rng.randint(0, 2)
        n_style = rng.randint(0, 1)

    timbre_picks = _pick_n_unique(TIMBRE_TAGS, n_timbre)
    parts.extend(timbre_picks)

    if n_spatial > 0:
        parts.extend(_pick_n_unique(SPATIAL_TAGS, n_spatial))

    if n_wave > 0:
        wave_picks = _pick_n_unique(WAVE_TECH_TAGS, n_wave)
        parts.extend(wave_picks)

    if n_style > 0:
        valid_styles = STYLE_TAGS[:]
        if family not in ("Synth", "Bass"):
            valid_styles = [s for s in valid_styles if s not in ("303", "Acid")]
        if valid_styles:
            parts.extend(_pick_n_unique(valid_styles, n_style))

    # Family-specific bonus tags
    extra_pool = FAMILY_EXTRA_TAGS.get(family, [])
    if extra_pool:
        n_extra = rng.randint(0, min(2, len(extra_pool)))
        already = set(parts)
        extras = [t for t in _pick_n_unique(extra_pool, n_extra + 2) if t not in already]
        parts.extend(extras[:n_extra])

    # Band tags
    if rng.random() < 0.5:
        parts.append(rng.choice(BAND_TAGS))

    # FX
    if rng.random() < 0.6:
        parts.append(_weighted_choice(FX_REVERB_WEIGHTED))
    if rng.random() < 0.4:
        parts.append(_weighted_choice(FX_DELAY_WEIGHTED))
    if rng.random() < 0.35:
        parts.append(_weighted_choice(FX_DISTORTION_WEIGHTED))
    if rng.random() < 0.25:
        parts.append(_weighted_choice(FX_PHASER_WEIGHTED))
    if rng.random() < 0.08:
        parts.append(_weighted_choice(FX_BITCRUSH_WEIGHTED))

    # Structure / notation
    structure_options = [s for s in STRUCTURE_TAGS if s != "None"]
    if family == "Bass":
        structure_options.append("Bassline")
    structure = rng.choice(structure_options)
    parts.append(structure)

    # Rhythm, speed, density, contour
    if rng.random() < 0.4:
        parts.append(rng.choice([r for r in RHYTHM_TAGS if r != "None"]))
    if rng.random() < 0.4:
        parts.append(rng.choice([s for s in SPEED_TAGS if s != "None"]))
    if rng.random() < 0.5:
        parts.append(rng.choice([d for d in DENSITY_TAGS if d != "None"]))
    if rng.random() < 0.3:
        parts.append(rng.choice([c for c in CONTOUR_TAGS if c != "None"]))

    # Experimental: optional second family for timbre mixing (~20% chance)
    if mode == "experimental" and rng.random() < 0.22:
        other_families = [f for f in INSTRUMENT_FAMILIES if f != family]
        mix_family = rng.choice(other_families)
        mix_sub_pool = SUBFAMILIES.get(mix_family, [])
        if mix_sub_pool:
            mix_sub = _weighted_choice(mix_sub_pool)
            parts.append(mix_sub)

    return ", ".join(parts)
