from ._anvil_designer import SoundsTemplate
from anvil import *
import anvil.js
import time

from ... import breathing_settings


class Sounds(SoundsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        # before voice manager gets voices since rate used for test speaking
        self.speech_rate = breathing_settings.get_voice_rate()
        self.set_speech_rate()
        # initialize voice then update it in voice manager
        self.selected_voice = None
        self.voices = []
        self.voice_manager = Sounds.VoiceManager()
        self.load_voices()
        # speech and sounds
        self.set_play_phase_sounds_bool()
        self.set_speak_phases_bool()
        self.set_speak_counts_bool()
        # so developer can check text in user agent
        self.ua_text.text = self._get_ua_text()
        # Audio map for testing
        self._audio_test_map = {
            "high": "./_/theme/high.mp3",
            "low": "./_/theme/low.mp3",
            "hold": "./_/theme/hold.mp3",
            "silence": "./_/theme/silence.mp3"
        }
        # clear errors
        self.audio_debug_label.text = ""
        self._apply_platform_voice_rules()

    def _apply_platform_voice_rules(self):
        if self._is_ios():
            # Disable voice selection on iOS
            self.voice_dropdown.enabled = False

            # Optional UX hint
            self.voice_dropdown.tooltip = (
                "On iPhone and iPad, the voice follows your system settings."
            )
        else:
            self.voice_dropdown.enabled = True


    # -------------------------
    # settings module speach rate
    # -------------------------


    def _is_ios(self):
        """
        Detect iOS devices (iPhone / iPad / iPod).
        Works across Safari, Chrome, Firefox iOS.
        """
        win = anvil.js.window
        ua = win.navigator.userAgent

        return (
            "iPhone" in ua
            or "iPad" in ua
            or "iPod" in ua
            # iPadOS 13+ reports as Mac
            or ("Macintosh" in ua and win.navigator.maxTouchPoints > 1)
        )


    # -------------------------
    # settings module speach rate
    # -------------------------

    def set_speech_rate(self):
        # print(self.speech_rate)
        self.voice_rate.selected_value = str(self.speech_rate)

    def voice_rate_change(self, **event_args):
        breathing_settings.set_voice_rate(self.voice_rate.selected_value)
        self.speech_rate = self.voice_rate.selected_value

    # -------------------------
    # settings module play_phase_sounds
    # -------------------------

    def set_play_phase_sounds_bool(self):
        # checked is property for enabled or not
        self.play_phase_sounds.checked = breathing_settings.get_play_phase_sounds_bool()

    def play_phase_sounds_change(self, **event_args):
        play_phase_sounds_bool = self.play_phase_sounds.checked
        breathing_settings.set_play_phase_sounds_bool(play_phase_sounds_bool)


    # -------------------------
    # settings module speak_phases
    # -------------------------

    def set_speak_phases_bool(self):
        # checked is property for enabled or not
        self.speak_phases.checked = breathing_settings.get_speak_phases_bool()

    def speak_phases_change(self, **event_args):
        speak_phases_bool = self.speak_phases.checked
        breathing_settings.set_speak_phases_bool(speak_phases_bool)


    # -------------------------
    # settings module speach rate
    # -------------------------

    def set_speak_counts_bool(self):
        # checked is property for enabled or not
        self.speak_counts.checked = breathing_settings.get_speak_counts_bool()

    def speak_counts_change(self, **event_args):
        speak_counts_bool = self.speak_counts.checked
        breathing_settings.set_speak_counts_bool(speak_counts_bool)

    # -------------------------
    # PLATFORM
    # -------------------------

    def _get_ua_text(self):
        win = anvil.js.window
        ua = win.navigator.userAgent
        return ua

    # =======================================================
    # Voice handling for windows
    # =======================================================
    def load_voices(self):
        """
        Loads voices asynchronously; waits for iOS/Chrome/Firefox to populate. alhtouh vocies do not work on phone
        Only after voices are loaded can the dropdown and speaking functions be used reliably.
        """
        win = anvil.js.window
        synth = win.speechSynthesis

        def got_voices(voices):
            # Keep only English voices
            en_voices = [(v.name, v.lang, v) for v in voices if v.lang.startswith("en")]
            if not en_voices:
                # fallback if none available
                en_voices = [(v.name, v.lang, v) for v in voices]
            self.voices = en_voices

            if self._is_ios():
                # Populate dropdown
                self.voice_dropdown.items = ["default for system"]
            else:
                # Populate dropdown
                self.voice_dropdown.items = [(f"{name} - {lang}", obj) for name, lang, obj in en_voices]

            # Restore stored voice or fallback
            stored_voice = breathing_settings.get_voice()
            if stored_voice in [v[2] for v in en_voices]:
                self.selected_voice = stored_voice
            else:
                self.selected_voice = en_voices[0][2]
                breathing_settings.set_voice(self.selected_voice)

            # Enable test button now that voices are ready
            self.speak_test.enabled = True

        # iOS may not have voices immediately
        voices_ready = synth.getVoices()
        if voices_ready and len(voices_ready) > 0:
            got_voices(voices_ready)
        else:
            # Listen for voiceschanged event
            def on_voices_changed(event):
                synth.removeEventListener("voiceschanged", on_voices_changed)
                got_voices(synth.getVoices())

            synth.addEventListener("voiceschanged", on_voices_changed)


    # ------------------------------------------------------
    # ------------------------------------------------------

    def voices_dropdown_change(self, **event_args):
        self.selected_voice = self.voice_dropdown.selected_value
        breathing_settings.set_voice(self.selected_voice)
        # self._speak_sample()

    def speak_test_click(self, **event_args):
        self._speak_sample()

    def _speak_sample(self):
        """
        Speak a test phrase
        Using selected voice for desktop, or system voice on iphone
        """
        # if not self.selected_voice:
        #     return
        win = anvil.js.window
        synth = win.speechSynthesis
        synth.cancel()  # stop any previous speech
        utter = win.SpeechSynthesisUtterance()
        utter.text = "Inhale, hold, exhale, 3, 2, 1"
        # voice has no effect on iphone
        utter.voice = self.selected_voice
        utter.rate = float(self.speech_rate)
        utter.pitch = 1.0
        synth.speak(utter)


    class VoiceManager:
        """Handles async loading of SpeechSynthesis voices."""
        def __init__(self):
            self.voices = None
            self._callbacks = []
            self._initialized = False

        def _load_voices(self):
            if self._initialized:
                return
            self._initialized = True

            win = anvil.js.window
            synth = win.speechSynthesis

            def deliver():
                # List of (name, lang, object)
                self.voices = [(v.name, v.lang, v) for v in synth.getVoices()]
                for cb in self._callbacks:
                    cb(self.voices)
                self._callbacks = []

            # Already available
            if synth.getVoices() and len(synth.getVoices()) > 0:
                deliver()
                return

            # Otherwise wait for voiceschanged
            def on_voices_changed(event):
                synth.removeEventListener("voiceschanged", on_voices_changed)
                deliver()

            synth.addEventListener("voiceschanged", on_voices_changed)

        def get_voices(self, callback=None):
            self._load_voices()

            if self.voices is not None:
                if callback:
                    callback(self.voices)
                return self.voices

            if callback:
                self._callbacks.append(callback)
            return None


    def _log_audio_error(self, msg):
        """Log errors to console and optionally to a label"""
        print(msg)
        if hasattr(self, "audio_debug_label"):
            self.audio_debug_label.text += msg + "\n"

    # -------------------------
    # SOUNDS TEST BUTTON
    # -------------------------
    def sounds_test_click(self, **event_args):
        """Test inhale, exhale, hold, and silence sounds sequentially."""
        win = anvil.js.window
        # Map of sounds; use the correct file paths
        sounds = {
            "inhale": "./_/theme/high.mp3",
            "exhale": "./_/theme/low.mp3",
            "hold":   "./_/theme/hold.mp3",
            "silence": "./_/theme/silence.mp3"
        }

        # Clear debug label
        if hasattr(self, "audio_debug_label"):
            self.audio_debug_label.text = ""

        # Recursive function to play the next sound
        def play_next(keys, index=0):
            if index >= len(keys):
                return  # all done

            key = keys[index]
            src = sounds[key]

            audio = win.Audio(src)
            audio.volume = 1
            audio.currentTime = 0

            # Log errors
            audio.onerror = lambda evt=None: self._log_audio_error(f"Failed to play {key}")

            # When the sound ends, play the next one
            audio.onended = lambda evt=None: play_next(keys, index + 1)

            try:
                p = audio.play()
                if p:
                    p.catch(lambda e: self._log_audio_error(f"Play blocked ({key}): {e}"))
            except Exception as e:
                self._log_audio_error(f"Exception ({key}): {e}")

        # Start the sequence
        play_next(list(sounds.keys()))
