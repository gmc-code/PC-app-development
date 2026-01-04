# This is a module.
# You can define variables and functions here, and use them from any form.
# This helps the sliders form get setings from settings form and voices form

# Internal storage for start for set_breath_patterns and settings

import anvil.js

def get_default_ua_speech_rate():
    win = anvil.js.window
    ua = win.navigator.userAgent.lower()
    # 2dp only from 0.20 to 1.40
    if "ipad" in ua:
        return "0.65"
    elif "macintosh" in ua:
        return "0.65"
    elif "iphone" in ua:
        return "0.65"
    elif "windows" in ua:
        return "0.70"
    elif "android" in ua:
        return "0.35"
    return "1.00"

# ===============================================================

_settings = {
    "inhale": 4,
    "hold1": 4,
    "exhale": 4,
    "hold2": 4,
    "cycles": 6,
    "play_phase_sounds": False,
    "speak_phases": True,
    "speak_counts": True,
}

voice_rate = get_default_ua_speech_rate()
# print(voice_rate)

_voice_settings = {
    "voice": None,
    "voice_rate": voice_rate,
    "voice_filler": " ,  ",
}

# not used yet
_slider_theme_colors_settings = {
    "energy": '#F39C12',
    "calm": '#57b0eb',
    "sleep": '#ae2be4',
    "focus": '#2fcc35',
}

_slider_color_settings = {
    "inhale": '#33cc33',
    "hold1": '#cccccc',
    "exhale": '#3399ff',
    "hold2": '#cccccc',
}

_slider_animate_color_settings = {
    "inhale": '#99ff99',
    "hold1": '#e5e5e5',
    "exhale": '#cce6ff',
    "hold2": '#e5e5e5',
}

# -------------------------
# _slider_color_settings
# -------------------------

def get_slider_color_settings():
    return _slider_color_settings

def get_slider_color(phase):
    return _slider_color_settings[phase]

def get_slider_animate_color_settings():
    return _slider_animate_color_settings

def get_slider_animate_color(phase):
    return _slider_animate_color_settings[phase]

# -------------------------
# Breath pattern
# -------------------------

def set_breath_pattern(inhale=4, hold1=4, exhale=4, hold2=4):
    _settings.update({
        "inhale": inhale,
        "hold1": hold1,
        "exhale": exhale,
        "hold2": hold2
    })

def get_breath_pattern():
    # RETURN DICTIONARY
    return {
        "inhale": _settings["inhale"],
        "hold1": _settings["hold1"],
        "exhale": _settings["exhale"],
        "hold2": _settings["hold2"]
    }

# -------------------------
# Cycles
# -------------------------
def set_cycles(cycles):
    _settings["cycles"] = cycles

def get_cycles():
    return _settings["cycles"]

# -------------------------
# play_phase_sounds
# -------------------------

def set_play_phase_sounds_bool(bool):
    _settings["play_phase_sounds"] = bool

def get_play_phase_sounds_bool():
    return _settings["play_phase_sounds"]

# -------------------------
# speak_phases
# -------------------------

def set_speak_phases_bool(bool):
    _settings["speak_phases"] = bool

def get_speak_phases_bool():
    return _settings["speak_phases"]

# -------------------------
# Counts
# -------------------------

def set_speak_counts_bool(bool):
    _settings["speak_counts"] = bool
    # print(bool)

def get_speak_counts_bool():
    return _settings["speak_counts"]

# -------------------------
# Voice
# -------------------------
def set_voice(value):
    _voice_settings["voice"] = value

def get_voice():
    return _voice_settings["voice"]

# -------------------------
# Voice rate
# -------------------------
def set_voice_rate(value):
    _voice_settings["voice_rate"] = value

def get_voice_rate():
    return _voice_settings["voice_rate"]

# -------------------------
# Voice filler
# -------------------------
def set_voice_filler(self):
    #  " ,  " is about it, nothing extra pads speech in silence
    win = anvil.js.window
    ua = win.navigator.userAgent.lower()
    if "ipad" in ua:
        value = " ,  "
    elif "macintosh" in ua:
        value = " ,  "
    elif "iphone" in ua:
        value = " ,  "
    elif "windows" in ua:
        value = " ,  "
    elif "android" in ua:
        value = " ,  "
    else:
        value = " ,  "
    _voice_settings["voice_filler"] = value


def get_voice_filler():
    return _voice_settings["voice_filler"]
