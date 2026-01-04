
# ============================================================
# AUDIO PLAYBACK DESIGN (IMPORTANT – READ BEFORE CHANGES)
# ============================================================
#
# This app intentionally uses a "fire-and-forget" audio model
# for short MP3 cues, combined with SpeechSynthesis for spoken
# guidance. The design reflects REAL, tested limitations of
# iOS WebKit-based browsers.
#
# ------------------------------------------------------------
# CRITICAL PLATFORM REALITY (iOS)
# ------------------------------------------------------------
#
# On iOS Safari and iOS Chrome:
#
# 1. SpeechSynthesis and HTMLAudioElement (MP3) are
#    MUTUALLY EXCLUSIVE per page session.
#
#    - If SpeechSynthesis is used first:
#        * Speech works reliably
#        * ALL subsequent MP3 playback FAILS silently
#
#    - If an MP3 is played first:
#        * The first MP3 may play
#        * SpeechSynthesis NEVER works
#        * Further MP3 playback is unreliable or blocked
#
#    There is NO recovery, unlock, delay, or workaround.
#
# 2. HTMLAudioElement cannot play a SEQUENCE of MP3s
#    unless EACH play is directly user-gesture driven.
#
#    - First MP3 triggered by a click: works
#    - Timer- or loop-driven MP3 playback: blocked
#
#    This applies even if SpeechSynthesis is disabled.
#
# ------------------------------------------------------------
# iOS FIREFOX NOTE
# ------------------------------------------------------------
#
# Firefox on iOS uses WebKit but exhibits DIFFERENT,
# less restrictive behaviour for short MP3 playback.
#
# • Sequential MP3 playback may work when Speech is OFF
# • Behaviour is not guaranteed and may change
# • Firefox is therefore treated as a "best-effort" case
#
# The app intentionally does NOT rely on Firefox-specific
# behaviour for correctness.
#
# On iOS, Firefox’s container is unusually permissive: it can keep a web page’s JavaScript and media playing for 30+ minutes without going to sleep, as long as there’s some audio activity (even small MP3s).
# Key points
# Safari/Chrome/WebKit tabs: suspend after ~5 minutes of inactivity, no way around it.
# Firefox for iOS: sandboxed container allows much longer runtime, observed 30+ min with audio playback.
# Reason: Firefox’s container manages the page lifecycle differently; it delays iOS’s suspension of inactive tabs while media is playing.
# No other browsers currently match this behavior on iOS; all others are essentially Safari under the hood.
# Caveat: This isn’t guaranteed — low battery, screen lock, or iOS updates could still pause the page.
# Firefox is the only practical iOS browser where long breathing cycles (20–30+ min) can run reliably, and MP3 playback helps maintain the active state.

# ------------------------------------------------------------
# DESIGN CONSEQUENCES (INTENTIONAL)
# ------------------------------------------------------------
#
# • SpeechSynthesis is the ONLY reliable automated audio
#   system on iOS for timed / looping behaviour.
#
# • MP3 phase sounds are therefore:
#     - ENABLED on desktop browsers
#     - ENABLED on Android
#     - ENABLED on iPhone Firefox (when Speech is OFF)
#     - DISABLED on iOS when Speech is active
#
# This behaviour is intentional and unavoidable.
#
# ------------------------------------------------------------
# MP3 PLAYBACK MODEL (WHERE ALLOWED)
# ------------------------------------------------------------
#
# 1. _audio_map stores FILE PATHS ONLY (strings)
#    ------------------------------------------------
#    We do NOT store Audio() objects.
#
#    Each playback creates a FRESH Audio instance:
#        audio = window.Audio(path)
#        audio.play()
#
#     Reason:
#     - Reusing Audio objects causes dropped or blocked playback
#       due to overlapping play/pause/end state transitions,
#       especially on iOS WebKit.

#
# 2. Fire-and-forget playback
#    ------------------------------------------------
#    Audio objects are NOT stored, paused, or reused.
#    They are allowed to finish naturally and be garbage collected.
#
# 3. No global audio stop / pause
#    ------------------------------------------------
#    Because Audio instances are short-lived and not tracked,
#    we intentionally DO NOT attempt to stop or pause them.
#
#    _stop_all_audio() is intentionally empty.
#
#    This avoids iOS WebKit bugs and timing races.
#
# ------------------------------------------------------------
# SPEECH MODEL
# ------------------------------------------------------------
#
# • SpeechSynthesis is managed independently
# • speechSynthesis.cancel() is safe and immediate
# • Speech is the PRIMARY audio channel on iOS
#
# ------------------------------------------------------------
# DO NOT REFACTOR WITHOUT RE-TESTING ON REAL iOS DEVICES
# ------------------------------------------------------------
#
# Desktop browser behaviour is NOT representative of iOS.
# If audio or speech behaviour changes, test on:
#   - iOS Safari
#   - iOS Chrome
#   - iOS Firefox
#
# This design is intentional, tested, and platform-constrained.
# ============================================================



from ._anvil_designer import SlidersTemplate
from anvil import *
import anvil.server
import time
import anvil.js

from ... import breathing_settings


def error_handler(err):
    # Silent error handling for iOS speech quirks
    return


set_default_error_handling(error_handler)


class Sliders(SlidersTemplate):
    # -------------------------
    # INIT
    # -------------------------
    def __init__(self, **properties):
        self.init_components(**properties)
        self.timer_sleep = 0.095     # at 0.1 seems to be about 10% too slow
        self.run = False
        self.paused = False
        self.set_sliders_from_settings()
        self.get_runner_settings()
        self.set_audio_settings()
        # Cache for full speech strings (cue + numbers)
        self._speech_cache = {}

    # -------------------------
    # SETTINGS
    # -------------------------

    def set_audio_settings(self):
        """
        Store only file paths.
        We intentionally DO NOT store Audio objects here.
        Each play creates a fresh Audio() instance to avoid iOS Safari playback bugs.
        """
        self._audio_map = {
            "inhale": "./_/theme/high.mp3",
            "exhale": "./_/theme/low.mp3",
            "hold": "./_/theme/hold.mp3",
            "silence": "./_/theme/silence.mp3",
        }

    def set_sliders_from_settings(self):
        # set values
        self.breath_settings = breathing_settings.get_breath_pattern()
        self.inhale_slider.value = self.breath_settings["inhale"]
        self.hold1_slider.value = self.breath_settings["hold1"]
        self.exhale_slider.value = self.breath_settings["exhale"]
        self.hold2_slider.value = self.breath_settings["hold2"]
        # set colours
        self.slider_color_settings = breathing_settings.get_slider_color_settings()
        self.inhale_slider.color = self.slider_color_settings["inhale"]
        self.hold1_slider.color = self.slider_color_settings["hold1"]
        self.exhale_slider.color = self.slider_color_settings["exhale"]
        self.hold2_slider.color = self.slider_color_settings["hold2"]

    def get_runner_settings(self):
        self.cycles_to_go.text = breathing_settings.get_cycles()
        self.play_phase_sounds = breathing_settings.get_play_phase_sounds_bool()
        self.speak_phases = breathing_settings.get_speak_phases_bool()
        self.speak_counts = breathing_settings.get_speak_counts_bool()
        self.filler = breathing_settings.get_voice_filler()

    # -------------------------
    # speak text
    # -------------------------

    def _speak(self, text):
        if not text:
            return
        win = anvil.js.window
        synth = win.speechSynthesis
        # synth.cancel()  # prevents queue drift (important!)
        utt = win.SpeechSynthesisUtterance(str(text))
        voice = breathing_settings.get_voice()
        if voice:
            utt.voice = voice
        utt.rate = breathing_settings.get_voice_rate()
        synth.speak(utt)

    # -------------------------
    # play mp3 reliably
    # -------------------------

    def _play_audio(self, cue_word="silence"):
        win = anvil.js.window
        src = self._audio_map.get(cue_word, self._audio_map["silence"])

        # for testing
        # self._log_audio(f"[AUDIO] Attempt play: {cue_word} -> {src}")

        audio = win.Audio(src)
        audio.currentTime = 0
        # audio.volume = 1

        # for testing
        # audio.onplay = lambda evt=None: self._log_audio(f"[AUDIO] onplay: {cue_word}")
        # audio.onended = lambda evt=None: self._log_audio(f"[AUDIO] ended: {cue_word}")
        # audio.onerror = lambda evt=None: self._log_audio(f"[AUDIO] onerror: {cue_word}")

        try:
            p = audio.play()
            if p:
                pass
                # p.then(lambda _: self._log_audio(f"[AUDIO] play() promise resolved: {cue_word}")) \
                #     .catch(lambda e: self._log_audio(f"[AUDIO] play() promise rejected: {cue_word} -> {e}"))
        except Exception as e:
            pass
            # self._log_audio(f"[AUDIO] Exception calling play(): {cue_word} -> {e}")


    # -------------------------
    # _speech_cache and run phase
    # -------------------------

    # not yet implemented so cache will grow with changes to patterns etc
    def refresh_settings_cache(self):
        self.filler = breathing_settings.get_voice_filler()
        self.speak_phases = breathing_settings.get_sounds()
        self.speak_counts = breathing_settings.get_counts()
        self._speech_cache.clear()


    def _get_phase_speech(self, phase, seconds):
        """
        Return cached speech string for a phase.
        - phase: the slider component to animate, 'inhale', 'hold', 'exhale', 'hold', .
        - seconds: duration of the phase in seconds
        Only four entries cached for each play, depends on settings:
        self.speak_phases, self.speak_counts, self.filler
        # Cache only full phrase strings (not utterances).
        # We do NOT cache SpeechSynthesisUtterance objects because
        # voice/rate can change dynamically.
        """
        # key depends on settings that affect text
        # Cache key includes all settings that affect spoken output
        # so cache remains valid when user toggles options
        key = (phase, seconds, self.speak_phases, self.speak_counts, self.filler)
        if key in self._speech_cache:
            return self._speech_cache[key]

        parts = []
        if self.speak_phases and phase:
            parts.append(phase)

        if seconds > 1 and self.speak_counts:
            if self.speak_phases:
                numbers = range(int(seconds-1), 0, -1)
            else:
                numbers = range(int(seconds), 0, -1)
            # numbers = range(int(seconds-1), 0, -1)
            parts.append(self.filler.join(str(i) for i in numbers))

        full_text = " ".join(parts)
        self._speech_cache[key] = full_text
        #testing, comment out
        # print(full_text)
        return full_text

    # -------------------------
    # RUN PHASE
    # -------------------------
    def _run_phase(self, slider, seconds, slider_name, cue_word):
        if not self.run or seconds == 0:
            return
        # for testing
        # self._log_audio(f"[PHASE] {cue_word} for {seconds}s")

        # Play audio
        if self.play_phase_sounds:
            self._play_audio(cue_word)
        else:
            self._play_audio("silence")

        # Speak
        full_speech = self._get_phase_speech(cue_word, seconds)
        if full_speech:
            self._speak(full_speech)

        # Animate slider
        original_color = slider.color
        slider.color = breathing_settings.get_slider_animate_color(slider_name)
        slider.handle_size = 16
        slider.value = seconds

        ticks = int(seconds * 10)
        for i in range(ticks, -1, -1):
            if not self.run:
                break
            while self.paused and self.run:
                time.sleep(0.05)
            slider.value = round(i / 10, 1)
            time.sleep(self.timer_sleep)

        slider.color = original_color
        slider.handle_size = 32
        slider.value = seconds

    # -------------------------
    # BREATH PHASES
    # -------------------------
    def inhale(self, val=4):
        self._run_phase(self.inhale_slider, val, "inhale", "inhale")

    def hold1(self, val=0):
        self._run_phase(self.hold1_slider, val, "hold1", "hold")

    def exhale(self, val=4):
        self._run_phase(self.exhale_slider, val, "exhale", "exhale")

    def hold2(self, val=0):
        self._run_phase(self.hold2_slider, val, "hold2", "hold")

    # -------------------------
    # CONTROL BUTTONS
    # -------------------------

    def start_breathing_click(self, **event_args):
        # for testing
        # self._log_audio_clear()
        self.run = True
        # Snapshot current slider values and number of cycles
        inhale_val = self.inhale_slider.value
        hold1_val = self.hold1_slider.value
        exhale_val = self.exhale_slider.value
        hold2_val = self.hold2_slider.value
        reps = int(self.cycles_to_go.text)

        # Speak "Get ready" at the start
        self._speak("Get ready.")
        time.sleep(3)

        # Main breathing loop
        for i in range(reps):
            if not self.run:
                break
            self.inhale(inhale_val)   # inhale phase with audio + slider
            self.hold1(hold1_val)     # first hold
            self.exhale(exhale_val)   # exhale
            self.hold2(hold2_val)     # second hold
            # Update cycles remaining in UI
            self.cycles_to_go.text = reps - (i + 1)

        # Reset cycles display at end
        self.cycles_to_go.text = breathing_settings.get_cycles()



    # ------------------------------------------------------
    # _log_audio for testing
    # ------------------------------------------------------

    def _log_audio_clear(self):
        if hasattr(self, "audio_debug_label"):
            self.audio_debug_label.text = ""

    def _log_audio(self, msg):
        print(msg)
        if hasattr(self, "audio_debug_label"):
            self.audio_debug_label.text += msg + "\n"

    def _log_audio_error(self, msg):
        print(msg)
        if hasattr(self, "audio_debug_label"):
            self.audio_debug_label.text += msg + "\n"

    # ------------------------------------------------------
    # pause and stop
    # ------------------------------------------------------

    def pause_toggle_click(self, **event_args):
        if not self.run:
            return
        if self.paused:
            self._resume_all()
        else:
            self._pause_all()

    def _pause_all(self):
        self.paused = True
        # Stop speech immediately
        self._stop_speech()
        # Stop all audio immediately
        # self._stop_all_audio()

    def _resume_all(self):
        self.paused = False

    # def _pause_all_audio(self):
    #     # # LEGACY — not used.
    #     # _audio_map stores file paths, not Audio objects.
    #     # Pausing audio is intentionally unsupported.
    #     for audio in self._audio_map.values():
    #         audio.pause()

    def stop_click(self, **event_args):
        self.run = False
        self.paused = False
        # Stop speech immediately
        self._stop_speech()
        # Stop all audio immediately
        # self._stop_all_audio()
        # reset sliders
        self._reset_all_sliders()

    def _stop_speech(self):
        win = anvil.js.window
        synth = win.speechSynthesis
        synth.cancel()   # IMMEDIATE stop + clears queue

    def _stop_all_audio(self):
        # Let short sounds finish naturally
        # Intentionally empty.
        # Audio is played via fresh, short-lived Audio() instances.
        # We cannot (and should not) stop past instances.
        # This avoids iOS Safari playback bugs.
        pass

    def _reset_all_sliders(self):
        for slider_name in ("inhale", "hold1", "exhale", "hold2"):
            slider = getattr(self, f"{slider_name}_slider")
            slider.value = slider.value
            slider.color = breathing_settings.get_slider_color_settings()[slider_name]

    # ------------------------------------------------------
    # leave form
    # ------------------------------------------------------

    def form_hide(self, **event_args):
        """Called automatically when this form is removed from the page"""
        self._hard_stop()

    def _hard_stop(self):
        self.run = False
        self.paused = False
        self._stop_speech()
        # self._stop_all_audio()
        self._reset_all_sliders()

    # ------------------------------------------------------
    # sliders
    # ------------------------------------------------------


    def inhale_slider_change(self, handle, **event_args):
        """This method is called when the slider has finished sliding"""
        pass

    def inhale_slider_slide(self, handle, **event_args):
        """This method is called when the slider is sliding or dragging"""
        pass

    def hold1_slider_change(self, handle, **event_args):
        """This method is called when the slider has finished sliding"""
        pass

    def hold1_slider_slide(self, handle, **event_args):
        """This method is called when the slider is sliding or dragging"""
        pass

    def exhale_slider_change(self, handle, **event_args):
        """This method is called when the slider has finished sliding"""
        pass

    def exhale_slider_slide(self, handle, **event_args):
        """This method is called when the slider is sliding or dragging"""
        pass

    def hold2_slider_change(self, handle, **event_args):
        """This method is called when the slider has finished sliding"""
        pass

    def hold2_slider_slide(self, handle, **event_args):
        """This method is called when the slider is sliding or dragging"""
        pass









