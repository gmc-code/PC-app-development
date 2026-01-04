# voice_bootstrap.py
# Loads voices asynchronously
# Picks the first English voice for windows
# Stores it in breathing_settings
# Runs automatically

import anvil.js
from . import breathing_settings

_initialized = False
_callbacks = []

def ensure_voice_ready(callback=None):
    """
    Ensures a voice is selected and stored.
    Calls callback(voice) when ready.
    """
    global _initialized

    voice = breathing_settings.get_voice()
    if voice:
        if callback:
            callback(voice)
        return

    if callback:
        _callbacks.append(callback)

    if _initialized:
        return

    _initialized = True

    win = anvil.js.window
    synth = win.speechSynthesis

    def select_default():
        voices = synth.getVoices()
        if not voices:
            return

        # Prefer English
        en = [v for v in voices if v.lang.lower().startswith("en")]
        chosen = en[0] if en else voices[0]    # 0  for first voice

        breathing_settings.set_voice(chosen)

        for cb in _callbacks:
            cb(chosen)
        _callbacks.clear()

    # Voices already loaded
    if synth.getVoices():
        select_default()
        return

    # Wait for async load
    def on_voices_changed(event):
        synth.removeEventListener("voiceschanged", on_voices_changed)
        select_default()

    synth.addEventListener("voiceschanged", on_voices_changed)

