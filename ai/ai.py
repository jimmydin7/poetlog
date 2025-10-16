import os
import requests
import html
import re

open_ai_api_key = os.environ.get('OPENAI_API_KEY')
alternative_api = os.environ.get('ALTERNATIVE_FREE_API')


def _highlight_geodata(text: str, geodata: dict) -> str:

    if not text:
        return ""

    safe = html.escape(text)

    to_highlight = []
    for key in ["ip", "city", "region", "country", "location", "isp", "timezone"]:
        val = geodata.get(key) if isinstance(geodata, dict) else None
        if isinstance(val, str) and val.strip():
            to_highlight.append(val.strip())

    to_highlight = sorted(set(to_highlight), key=len, reverse=True)
    for val in to_highlight:
        pattern = re.escape(html.escape(val))
        safe = re.sub(rf"(?i)\b({pattern})\b", r'<span class="red-word">\1</span>', safe)
    return safe


def _fallback_poem(geodata: dict) -> list:
    city = (geodata or {}).get("city", "your city")
    region = (geodata or {}).get("region", "your region")
    country = (geodata or {}).get("country", "your country")
    ip = (geodata or {}).get("ip", "your IP")
    loc = (geodata or {}).get("location", "unknown coords")
    isp = (geodata or {}).get("isp", "your ISP")
    tz = (geodata or {}).get("timezone", "your timezone")

    raw_lines = [
        f"From {city}, where the streetlights hiss,",
        f"In {region}, {country}, shadows reminisce,",
        f"A whisper rides along the wire of {isp},",
        f"At {loc}, cold winds count and never miss,",
        f"The clock in {tz} ticks with a hungry grin,",
        f"And at {ip}, the night invites you in...",
    ]
    return [_highlight_geodata(line, geodata or {}) for line in raw_lines]


def generate_poem(geodata: dict) -> list:
    if not open_ai_api_key:
        return _fallback_poem(geodata)

    model = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")
    endpoint = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1/chat/completions")


    prompt = (
        "You are a poet of the macabre. Write a short, spooky 6-line poem that subtly weaves in "
        "the user's IP, city, region, country, ISP, coordinates, and timezone. "
        "Avoid labeling the fields; incorporate them naturally. Keep to exactly 6 lines, no title.\n\n"
        f"Data:\n"
        f"- IP: {geodata.get('ip', '')}\n"
        f"- City: {geodata.get('city', '')}\n"
        f"- Region: {geodata.get('region', '')}\n"
        f"- Country: {geodata.get('country', '')}\n"
        f"- Coordinates: {geodata.get('location', '')}\n"
        f"- ISP: {geodata.get('isp', '')}\n"
        f"- Timezone: {geodata.get('timezone', '')}\n"
    )

    headers = {
        "Authorization": f"Bearer {open_ai_api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You craft atmospheric, eerie poetry."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.8,
        "max_tokens": 220,
        "n": 1,
    }

    try:
        resp = requests.post(endpoint, headers=headers, json=body, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        content = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )
        if not content:
            return _fallback_poem(geodata)


        lines = [l for l in content.splitlines() if l.strip()][:6]
        if not lines:
            return _fallback_poem(geodata)
        return [_highlight_geodata(line, geodata or {}) for line in lines]
    except Exception:
        return _fallback_poem(geodata)