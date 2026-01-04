from ._anvil_designer import SettingsTemplate
from anvil import *


from ... import breathing_settings

class Settings(SettingsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.set_cycles()

    def set_cycles(self):
        self.cycles.selected_value = str(breathing_settings.get_cycles())

    def cycles_change(self, **event_args):
        cycles_val = int(self.cycles.selected_value)
        breathing_settings.set_cycles(cycles_val)

    # =================================
    # 3
    # =================================

    def relax_3_3_click(self, **event_args):
        breathing_settings.set_breath_pattern(3, 0, 3, 0)

    def relax_3_0_3_3_click(self, **event_args):
        breathing_settings.set_breath_pattern(3, 0, 3, 3)

    def relax_3_3_3_click(self, **event_args):
        breathing_settings.set_breath_pattern(3, 3, 3, 0)

    def box3_click(self, **event_args):
        breathing_settings.set_breath_pattern(3, 3, 3, 3)


    # =================================
    # 4
    # =================================

    def relax_4_4_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 0, 4, 0)

    def relax_4_0_4_4_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 0, 4, 4)

    def relax_4_4_4_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 4, 4, 0)

    def box4_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 4, 4, 4)

    # =================================
    # 5
    # =================================

    def relax_5_5_click(self, **event_args):
        breathing_settings.set_breath_pattern(5, 0, 5, 0)

    def relax_5_0_5_5_click(self, **event_args):
        breathing_settings.set_breath_pattern(5, 0, 5, 5)

    def relax_5_5_5_click(self, **event_args):
        breathing_settings.set_breath_pattern(5, 5, 5, 0)

    def box5_click(self, **event_args):
        breathing_settings.set_breath_pattern(5, 5, 5, 5)

    # =================================
    # 6
    # =================================

    def relax_6_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(6, 0, 6, 0)

    def relax_6_0_6_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(6, 0, 6, 6)

    def relax_6_6_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(6, 6, 6, 0)

    def box6_click(self, **event_args):
        breathing_settings.set_breath_pattern(6, 6, 6, 6)

    # =================================

    def box8_click(self, **event_args):
        breathing_settings.set_breath_pattern(8, 8, 8, 8)

    def box10_click(self, **event_args):
        breathing_settings.set_breath_pattern(10, 10, 10, 10)

    # =================================

    def energize_2_2_click(self, **event_args):
        breathing_settings.set_breath_pattern(2, 0, 2, 0)

    def energize_2_3_click(self, **event_args):
        breathing_settings.set_breath_pattern(2, 0, 3, 0)

    def relax_2_0_2_2_click(self, **event_args):
        breathing_settings.set_breath_pattern(2, 0, 2, 2)

    def relax_2_2_2_click(self, **event_args):
        breathing_settings.set_breath_pattern(2, 2, 2, 0)

    def box2_click(self, **event_args):
        breathing_settings.set_breath_pattern(2, 2, 2, 2)

    # =================================

    def relax_2_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(2, 0, 6, 0)

    def relax_3_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(3, 0, 6, 0)

    def relax_4_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 0, 6, 0)

    def relax_4_8_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 0, 8, 0)


    def relax_4_2_4_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 2, 4, 0)

    def relax_4_2_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 2, 6, 0)

    def relax_4_2_8_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 2, 8, 0)

    def relax_4_2_4_2_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 2, 4, 2)

    def relax_4_2_6_2_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 2, 6, 2)

    def relax_4_2_8_2_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 2, 8, 2)


    def relax_4_4_8_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 4, 8, 0)

    def relax_4_7_8_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 7, 8, 0)

    def relax_4_0_6_6_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 0, 6, 6)

    def relax_4_0_6_8_click(self, **event_args):
        breathing_settings.set_breath_pattern(4, 0, 6, 8)

