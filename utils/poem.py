import random
import html
import re


def _highlight_geodata(text: str, geodata: dict) -> str:
    if not text:
        return ""
    safe = html.escape(text)
    vals = []
    for key in ["ip", "city", "region", "country", "location", "isp", "timezone"]:
        v = (geodata or {}).get(key)
        if isinstance(v, str) and v.strip():
            vals.append(v.strip())
    for v in sorted(set(vals), key=len, reverse=True):
        pattern = re.escape(html.escape(v))
        safe = re.sub(rf"(?i)\b({pattern})\b", r'<span class="red-word">\1</span>', safe)
    return safe


def _choice(options):
    return random.choice(options)


def _compose_line(subjects, verbs, modifiers, endings, insert: str = "") -> str:
    s = _choice(subjects)
    v = _choice(verbs)
    m = _choice(modifiers)
    e = _choice(endings)
    line = f"{s} {v} {m} {e}"

    if insert:
        line = line.replace("{}", insert)
    return line.strip()


def _city_line(city: str) -> str:
    subjects = [
        "In {}", "From {}", "{} at midnight", "Down in {}",
        "Behind doors of {}", "Over {}'s cobbles", "Within {}'s fog",
        "At the edge of {}", "Under roofs in {}", "Above the alleys of {}",
        "Near the river in {}", "Under lamplight of {}",
    ]
    verbs = [
        "the windows", "the footfalls", "the shutters", "the lock",
        "the gate", "the stairwell", "the lamplight", "the gutters",
        "the hedges", "the crosswalk",
    ]
    modifiers = [
        "remember", "count", "practice", "hum", "tilt",
        "lean", "fog", "glisten", "wait", "ache",
    ]
    endings = [
        "your borrowed name", "the rain's small teeth", "a number twice",
        "what left and stayed", "a rumor in chalk", "the colder hour",
        "footsteps out of step", "the moth's agenda", "keys without pockets",
        "a bell with no church",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, city)


def _region_line(region: str) -> str:
    subjects = [
        "Across {}", "Through {}", "On roads of {}", "Pastures of {}",
        "Mile markers in {}", "Waystones of {}", "The hedgerows of {}",
        "Barn doors in {}", "Signposts in {}", "Dirt lanes of {}",
    ]
    verbs = [
        "forget", "lean", "ask", "echo", "fold",
        "smudge", "shiver", "point", "drift", "listen",
    ]
    modifiers = [
        "the way home", "yesterday's dust", "the unlit turn",
        "a map with damp edges", "the last whistle",
        "corn-silk rumors", "low thunder", "the names of crows",
        "gravel prayers", "boot-black dawn",
    ]
    endings = [
        "without directions", "in a tin voice", "as if warned",
        "like a held breath", "in slow grammar",
        "between fenceposts", "with two shadows",
        "beneath the hill's ear", "under a pale vane", "on borrowed light",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, region)


def _country_line(country: str) -> str:
    subjects = [
        "This {} night", "Flagpoles in {}", "Old hymns of {}",
        "Riverbanks of {}", "Threshing floors in {}",
        "Attics across {}", "Lanterns in {}", "Bell towers of {}",
        "Back roads in {}", "Shutters of {}",
    ]
    verbs = [
        "taste", "hang", "trade", "file", "spell",
        "hold", "knot", "gutter", "stack", "murmur",
    ]
    modifiers = [
        "of iron and rain", "with heavy cloth", "verses with crows",
        "their teeth on stone", "letters in silt",
        "echoes in grain", "ash-grey vowels", "cordwood dreams",
        "chapters of frost", "a hush of tin",
    ]
    endings = [
        "until the river answers", "through the rafters",
        "behind nailed doors", "under a red moon",
        "until boots forget their sizes", "like a promise unsworn",
        "in the kitchen's low light", "by the well's black eye",
        "along the siding's scars", "in a language of nails",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, country)


def _ip_line(ip: str) -> str:
    subjects = [
        "At {}", "From {}", "Within {}", "Around {}", "Near {}",
        "Inside {}", "Under {}", "By {}", "Across {}", "Beyond {}",
    ]
    verbs = [
        "a door clicks", "a pulse answers", "packets curl", "a hush rides",
        "a moth memorizes", "the porchlight lingers", "the cable hums",
        "a whisper counts", "the socket blinks", "static gathers",
    ]
    modifiers = [
        "without hinges", "twice and once", "like ivy", "toward thirteen",
        "under your breath", "behind the drywall", "with patient code",
        "through the conduit", "under bare bulbs", "beneath the rain",
    ]
    endings = [
        "then holds its breath", "and waits for a knock", "counting the wet seconds",
        "until someone answers", "with a practiced shiver", "like a small confession",
        "before the surge", "as the room tilts", "and the fuse remembers",
        "like a name on a wire",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, ip)


def _loc_line(loc: str) -> str:
    subjects = [
        "Coordinates {}", "At {}", "Under {}", "Beside {}", "Above {}",
        "Around {}", "Beyond {}", "Within {}", "Near {}", "Past {}",
    ]
    verbs = [
        "circle", "tilt", "stitch", "orbit", "draw",
        "hum", "perch", "anchor", "tremble", "listen",
    ]
    modifiers = [
        "like wolves", "toward the cellar", "the map with hair",
        "until they fade", "on the window",
        "beneath the steps", "at the lintel", "under the ash",
        "against the nail", "through the frost",
    ]
    endings = [
        "as if warned", "in small handwriting", "until noon forgets",
        "like a patient orbit", "in borrowed chalk",
        "to the bone's locket", "with three mistakes", "in a red margin",
        "as the kettle sighs", "under a dull star",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, loc)


def _isp_line(isp: str) -> str:
    subjects = [
        "Through {}", "Over {}", "Along {}", "Across {}", "Under {}",
        "Inside {}", "Past {}", "Beside {}", "Between {}", "Beyond {}",
    ]
    verbs = [
        "the static", "lullabies", "wires", "sparrows", "dial tones",
        "needles", "attics", "copper", "signals", "thunderheads",
    ]
    modifiers = [
        "grow teeth", "detune themselves", "remember storms", "perch and listen",
        "learn to shiver", "thread the dark", "collect rumors",
        "braid with rain", "sift the dust", "hum a buried key",
    ]
    endings = [
        "behind the eaves", "at the milepost", "under the stairs", "through the switchbox",
        "out past the fence", "toward the substation", "beneath wet sky",
        "over tile and tin", "into the old house", "between pulse and pause",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, isp)


def _tz_line(tz: str) -> str:
    subjects = [
        "In {}", "Across {}", "Under {}", "Inside {}", "Within {}",
        "Before {}", "After {}", "Through {}", "About {}", "Around {}",
    ]
    verbs = [
        "clocks", "sundials", "hourglasses", "bells", "shadows",
        "mornings", "noons", "midnights", "seconds", "minutes",
    ]
    modifiers = [
        "molt their numbers", "whisper in reverse", "breathe low",
        "file their teeth", "double themselves",
        "limp a little", "lean into dusk", "count backward",
        "forget the chime", "borrow an hour",
    ]
    endings = [
        "on the sill of night", "within the ticking house", "behind the curtain",
        "in the kitchen's blue light", "under the eaves",
        "where the hallway bends", "beside the kettle", "in the attic air",
        "without a witness", "like a hush of tin",
    ]
    return _compose_line(subjects, verbs, modifiers, endings, tz)


def generate_poem(geodata: dict) -> list:

    city = (geodata or {}).get("city", "a nameless city")
    region = (geodata or {}).get("region", "a shadowed region")
    country = (geodata or {}).get("country", "a forgotten country")
    ip = (geodata or {}).get("ip", "an unseen IP")
    loc = (geodata or {}).get("location", "coordinates unknown")
    isp = (geodata or {}).get("isp", "an unspeaking provider")
    tz = (geodata or {}).get("timezone", "an unholy timezone")

    lines = [
        _city_line(city),
        _region_line(region),
        _country_line(country),
        _ip_line(ip),
        _loc_line(loc),
        _isp_line(isp),
        _tz_line(tz),
    ]

    neutral_subjects = [
        "A window", "Bootsteps", "Candles", "The cellar door", "Mice",
        "Rain", "A coat on a nail", "The mirror", "Coal dust", "The doorknob",
    ]
    neutral_verbs = [
        "fogs", "practice", "bloom", "learn", "take notes",
        "rehearses", "remembers", "forgets", "settles", "tastes",
    ]
    neutral_mods = [
        "with names unsaid", "walking away", "with quiet bruises", "a new hinge",
        "in the pantry", "on the shingles", "old shoulders", "who arrived",
        "into lullabies", "like pennies",
    ]
    neutral_ends = [
        "and keeps the room", "until the stove exhales", "under thin glass",
        "as the rafters listen", "behind the curtain", "in borrowed light",
        "without telling anyone", "in the blue hour", "with a soft click",
        "as midnight measures",
    ]
    lines.append(_compose_line(neutral_subjects, neutral_verbs, neutral_mods, neutral_ends))
    lines.append(_compose_line(neutral_subjects, neutral_verbs, neutral_mods, neutral_ends))

    random.shuffle(lines)

    return [_highlight_geodata(l, geodata or {}) for l in lines]
