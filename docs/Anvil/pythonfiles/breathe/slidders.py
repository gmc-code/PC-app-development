# -------------------------
# Imports for Form1
# -------------------------
from ._anvil_designer import Form1Template  # The generated template for Form1
from anvil import *
import anvil.server

# Import other forms directly by their module names
from Sliders import Sliders
from Settings import Settings
from Info import Info
from Sounds import Sounds

 # path ..
from .. import voice_bootstrap

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Ensure a voice menu for windows exists immediately
        voice_bootstrap.ensure_voice_ready()
        # Go to Sliders ready to use
        self.sliders_link_click()

    # -------------------------
    # Helper methods
    # -------------------------
    def reset_links(self):
        self.info_link.role = ''
        self.settings_link.role = ''
        self.sliders_link.role = ''
        self.sounds_link.role = ''

    def _navigate_to(self, new_form_cls, link=None):
        """Stop current form, clear panel, and add new form."""
        # Stop any currently running form first
        current_components = self.content_panel.get_components()
        if current_components:
            current = current_components[0]
            if hasattr(current, "_hard_stop"):
                current._hard_stop()  # stops speech/audio/animation immediately

        # Clear panel and add new form
        self.content_panel.clear()
        self.content_panel.add_component(new_form_cls())

        # Update link role if provided
        if link:
            link.role = 'selected'


    # -------------------------
    # Link click methods
    # -------------------------
    def info_link_click(self, **event_args):
        self.reset_links()
        self._navigate_to(Info, link=self.info_link)

    def settings_link_click(self, **event_args):
        self.reset_links()
        self._navigate_to(Settings, link=self.settings_link)

    def sliders_link_click(self, **event_args):
        self.reset_links()
        self._navigate_to(Sliders, link=self.sliders_link)

    def sounds_link_click(self, **event_args):
        self.reset_links()
        self._navigate_to(Sounds, link=self.sounds_link)

    # Optional title links
    def Settings_title_link_click(self, **event_args):
        self.settings_link_click()

    def Info_title_link_click(self, **event_args):
        self.info_link_click()

    def Sliders_title_link_click(self, **event_args):
        self.sliders_link_click()

    def Sounds_title_link_click(self, **event_args):
        self.sounds_link_click()
