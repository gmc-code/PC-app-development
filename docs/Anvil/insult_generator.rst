====================================================
Insult generator
====================================================

This app generates a random insult.

A useful tool for formatting long lists is at: https://www.xhcode.com/pythonformat/

| Working app at: https://pc-insult-generator.anvil.app

----

Design
---------

| Use a Column panel.
| Use a label field, 2 buttons and a textbox.

.. image:: images/insults/random_insults.png
    :scale: 80

----

Get started
------------------------------

#. Go to: https://anvil.works/new-build
#. Click: Blank App.
#. Choose: Material Design

----

Settings
------------------------------

#. Click on the cog icon to show the settings tab.
#. Enter an App name. **Insult generator**
#. Enter an App title. **Insult generator**
#. Enter an App description. **This app generates a random insult.**
#. Close the settings tab.

----

Build interface
-------------------

Title
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the **Drop title here** container.
| In the properties panel: name section, set the **name** to **title**.
| In the properties panel: text section, set the **text** to **Random Insults**.

----

Column panel
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *column panel* component onto the form.

----

Instructions
~~~~~~~~~~~~~~~~~~~

| Drag and drop a *label* component onto the column panel.
| In the properties panel: name section, set the **name** to **instructions**.
| In the properties panel: text section, set the **text** to text below.

.. code-block::
    
    Choose an insult style.

----

Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Drag and drop a *Button* component onto the column panel.
| In the properties panel: name section, set the **name** to **get_old_insult**.
| In the properties panel: text section, set the **text** to **Shakespearean Insult**.
| In the properties panel: text section, set the **font_size** to **28**.
| In the properties panel: appearance section, set the **role** to **secondary-color**.
| In the properties panel: Events section, click on the blue icon to the right of the **click** label.
| This will add a default script, **get_old_insult_click**, to the code. This will be coded later to generate the output.

| Drag and drop a *Button* component onto the column panel.
| In the properties panel: name section, set the **name** to **get_insult**.
| In the properties panel: text section, set the **text** to **Modern Insult**.
| In the properties panel: text section, set the **font_size** to **28**.
| In the properties panel: appearance section, set the **role** to **primary-color**.
| In the properties panel: Events section, click on the blue icon to the right of the **click** label.
| This will add a default script, **get_insult_click**, to the code. This will be coded later to generate the output.

----

Output 
~~~~~~~~~~~~~~~~~~~


| Drag and drop a *TextBox* component onto the column panel to the right of the label.
| Click and drag the divider between the label and textbox to resize them.
| In the properties panel: name section, set the **name** to **output**.
| In the properties panel: text section, set the **font_size** to **24**.

----

Initial Code & Event Code 
---------------------------

| The event, **get_old_insult_click**, calls the **make_old_insult** function.
| The event, **get_insult_click**, calls the **make_insult** function.

.. code-block:: python

    from ._anvil_designer import Form1Template
    from anvil import *
    import anvil.tables as tables
    import anvil.tables.query as q
    from anvil.tables import app_tables
    from random import choice

    class Form1(Form1Template):

        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

        def get_old_insult_click(self, **event_args):
            self.make_old_insult()
            
        def get_insult_click(self, **event_args):
            self.make_insult()

----

Insult maker 
---------------------------

| **make_old_insult** places a random Shakespearean insult in the output textbox.
| **choice(insult1)** picks a random element from the list, **insult1**.

.. code-block:: python

    def make_old_insult(self):
        insult1 = ['artless', 'bawdy', 'beslubbering', 'bootless',
            'burly-boned', 'caluminous', 'churlish', 'clouted',
            'cockered', 'craven', 'cullionly', 'currish', 'dankish',
            'dissembling', 'droning', 'errant', 'fawning', 'fishified',
            'fobbing', 'frothy', 'froward', 'fusty', 'gleeking',
            'goatish', 'gorbellied', 'impertinent', 'infectious',
            'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
            'mewling', 'misbegotten', 'odiferous', 'paunchy', 'poisonous',
            'pribbling', 'puking', 'puny', 'qualling', 'rank', 'reeky',
            'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly',
            'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous',
            'warped', 'Wart-necked', 'wayward', 'weedy', 'wimpled',
            'yeasty'
        ]
        insult2 = ['base-court', 'bat-fowling', 'beef-witted',
            'beetle-headed', 'boil-brained', 'brazen-faced',
            "bunch-back'd", 'clapper-clawed', 'clay-brained',
            'common-kissing', 'crook-pated', 'dismal-dreaming',
            'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing',
            'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed',
            'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
            'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born',
            'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured',
            'knotty-pated', 'leaden-footed', 'lily-livered',
            'malmsey-nosed', 'milk-livered', 'motley-minded',
            'muddy-mettled', 'onion-eyed', "pigeon-liver'd",
            'plume-plucked', 'pottle-deep', 'pox-marked', 'rampallian',
            'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed',
            'scale-sided', 'scurvy-valiant', 'shard-borne',
            'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited',
            'tickle-brained', 'toad-spotted', 'unchin-snouted',
            "unwash'd", 'weather-bitten', 'whoreson'
        ]
        insult3 = ['apple-john', 'baggage', 'barnacle', 'Basket-Cockle',
            'bladder', 'blind-worm', 'boar-pig', 'bugbear', 'bum-bailey',
            'canker-blossom', 'clack-dish', 'clotpole', 'codpiece',
            'coxcomb', 'death-token', 'devil-monk', 'dewberry',
            'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker',
            'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy',
            'hedge-pig', 'horn-beast', 'hugger-mugger', 'joithead',
            'jolt-head', 'knave', 'lewdster', 'lout', 'maggot-pie',
            'malcontent', 'malt-worm', 'mammet', 'measle', 'minnow',
            'miscreant', 'moldwarp', 'mumble-news', 'nut-hook',
            'pigeon-egg', 'pignut', 'popinjay', 'pumpion', 'puttock',
            'rascal', 'ratsbane', 'scullian', 'scut', 'skainsmate',
            'strumpet', 'toad', 'varlot', 'vassal', 'wagtail',
            'whey-face'
        ]
        self.output.text = ("Thou art a " + choice(insult1) + " " +
            choice(insult2) + " " + choice(insult3) + ".")


| **make_insult** places a random insult in the output textbox.
| **choice(insult1)** picks a random element from the list, **insult1**.

.. code-block:: python

    def make_insult(self):
        insult1 = ['animalistic', 'appalling', 'awful', 'bad-looking',
            'beastly', 'deformed', 'disfigured', 'foul', 'frightful',
            'grisly', 'gross', 'grotesque', 'hard-featured', 'hideous',
            'horrid', 'ill-favored', 'loathsome', 'misshapen',
            'monstrous', 'not much to look at', 'repelling', 'repugnant',
            'repulsive', 'revolting', 'unbeautiful', 'uncomely',
            'uninviting', 'unlovely', 'unsightly',
        ]
        insult2 = ['abrupt', 'abusive', 'bad-mannered', 'barbaric',
            'barbarous', 'blunt', 'boorish', 'brusque', 'brutish',
            'cheeky', 'churlish', 'coarse', 'crabbed', 'crude', 'curt',
            'discourteous', 'graceless', 'gross', 'gruff', 'ignorant',
            'illiterate', 'impertinent', 'impolite', 'impudent',
            'inconsiderate', 'insolent', 'insulting', 'intrusive',
            'loutish', 'obscene', 'raw', 'savage', 'scurrilous', 'surly',
            'uncivil', 'uncivilized', 'uncouth', 'uncultured',
            'uneducated', 'ungracious', 'unmannerly', 'unpolished',
            'unrefined', 'vulgar', 'wild',
        ]
        insult3 = ['bad guy', 'bad person', 'baddie', 'baddy',
            'black marketeer', 'blackmailer', 'blockhead', 'bonehead',
            'clodpoll', 'con', 'convict', 'cretin', 'crook', 'culprit',
            'delinquent', 'desperado', 'deuce', 'dimwit', 'dork',
            'dumbbell', 'dunce', 'evildoer', 'ex-con', 'felon', 'fool',
            'fugitive', 'gangster', 'guerilla', 'hood', 'hoodlum',
            'hooligan', 'hustler', 'ignoramus', 'imbecile',
            'inside person', 'jailbird', 'jerk', 'lawbreaker',
            'malefactor', 'mobster', 'moron', 'mug', 'muttonhead',
            'nincompoop', 'ninny', 'nitwit', 'offender', 'outlaw',
            'pinhead', 'racketeer', 'simpleton', 'sinner', 'slippery eel',
            'thug', 'tomfool', 'twit', 'wrongdoer', 'yardbird',
        ]
        self.output.text = ("You are a " + choice(insult1) + " " +
            choice(insult2) + " " + choice(insult3)+ ".")

----

Final  Code 
--------------------

| The full code is below.

.. code-block:: python

    from ._anvil_designer import Form1Template
    from anvil import *
    import anvil.tables as tables
    import anvil.tables.query as q
    from anvil.tables import app_tables
    from random import choice

    class Form1(Form1Template):

        def __init__(self, **properties):
            # Set Form properties and Data Bindings.
            self.init_components(**properties)

        def get_old_insult_click(self, **event_args):
            self.make_old_insult()
            
        def get_insult_click(self, **event_args):
            self.make_insult()
            
        def make_old_insult(self):
            insult1 = ['artless', 'bawdy', 'beslubbering', 'bootless',
                'burly-boned', 'caluminous', 'churlish', 'clouted',
                'cockered', 'craven', 'cullionly', 'currish', 'dankish',
                'dissembling', 'droning', 'errant', 'fawning', 'fishified',
                'fobbing', 'frothy', 'froward', 'fusty', 'gleeking',
                'goatish', 'gorbellied', 'impertinent', 'infectious',
                'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
                'mewling', 'misbegotten', 'odiferous', 'paunchy', 'poisonous',
                'pribbling', 'puking', 'puny', 'qualling', 'rank', 'reeky',
                'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly',
                'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous',
                'warped', 'Wart-necked', 'wayward', 'weedy', 'wimpled',
                'yeasty'
            ]
            insult2 = ['base-court', 'bat-fowling', 'beef-witted',
                'beetle-headed', 'boil-brained', 'brazen-faced',
                "bunch-back'd", 'clapper-clawed', 'clay-brained',
                'common-kissing', 'crook-pated', 'dismal-dreaming',
                'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing',
                'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed',
                'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
                'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born',
                'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured',
                'knotty-pated', 'leaden-footed', 'lily-livered',
                'malmsey-nosed', 'milk-livered', 'motley-minded',
                'muddy-mettled', 'onion-eyed', "pigeon-liver'd",
                'plume-plucked', 'pottle-deep', 'pox-marked', 'rampallian',
                'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed',
                'scale-sided', 'scurvy-valiant', 'shard-borne',
                'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited',
                'tickle-brained', 'toad-spotted', 'unchin-snouted',
                "unwash'd", 'weather-bitten', 'whoreson'
            ]
            insult3 = ['apple-john', 'baggage', 'barnacle', 'Basket-Cockle',
                'bladder', 'blind-worm', 'boar-pig', 'bugbear', 'bum-bailey',
                'canker-blossom', 'clack-dish', 'clotpole', 'codpiece',
                'coxcomb', 'death-token', 'devil-monk', 'dewberry',
                'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker',
                'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy',
                'hedge-pig', 'horn-beast', 'hugger-mugger', 'joithead',
                'jolt-head', 'knave', 'lewdster', 'lout', 'maggot-pie',
                'malcontent', 'malt-worm', 'mammet', 'measle', 'minnow',
                'miscreant', 'moldwarp', 'mumble-news', 'nut-hook',
                'pigeon-egg', 'pignut', 'popinjay', 'pumpion', 'puttock',
                'rascal', 'ratsbane', 'scullian', 'scut', 'skainsmate',
                'strumpet', 'toad', 'varlot', 'vassal', 'wagtail',
                'whey-face'
            ]
            self.output.text = ("Thou art a " + choice(insult1) + " " +
                choice(insult2) + " " + choice(insult3) + ".")
            
        def make_insult(self):
            insult1 = ['animalistic', 'appalling', 'awful', 'bad-looking',
                'beastly', 'deformed', 'disfigured', 'foul', 'frightful',
                'grisly', 'gross', 'grotesque', 'hard-featured', 'hideous',
                'horrid', 'ill-favored', 'loathsome', 'misshapen',
                'monstrous', 'not much to look at', 'repelling', 'repugnant',
                'repulsive', 'revolting', 'unbeautiful', 'uncomely',
                'uninviting', 'unlovely', 'unsightly',
            ]
            insult2 = ['abrupt', 'abusive', 'bad-mannered', 'barbaric',
                'barbarous', 'blunt', 'boorish', 'brusque', 'brutish',
                'cheeky', 'churlish', 'coarse', 'crabbed', 'crude', 'curt',
                'discourteous', 'graceless', 'gross', 'gruff', 'ignorant',
                'illiterate', 'impertinent', 'impolite', 'impudent',
                'inconsiderate', 'insolent', 'insulting', 'intrusive',
                'loutish', 'obscene', 'raw', 'savage', 'scurrilous', 'surly',
                'uncivil', 'uncivilized', 'uncouth', 'uncultured',
                'uneducated', 'ungracious', 'unmannerly', 'unpolished',
                'unrefined', 'vulgar', 'wild',
            ]
            insult3 = ['bad guy', 'bad person', 'baddie', 'baddy',
                'black marketeer', 'blackmailer', 'blockhead', 'bonehead',
                'clodpoll', 'con', 'convict', 'cretin', 'crook', 'culprit',
                'delinquent', 'desperado', 'deuce', 'dimwit', 'dork',
                'dumbbell', 'dunce', 'evildoer', 'ex-con', 'felon', 'fool',
                'fugitive', 'gangster', 'guerilla', 'hood', 'hoodlum',
                'hooligan', 'hustler', 'ignoramus', 'imbecile',
                'inside person', 'jailbird', 'jerk', 'lawbreaker',
                'malefactor', 'mobster', 'moron', 'mug', 'muttonhead',
                'nincompoop', 'ninny', 'nitwit', 'offender', 'outlaw',
                'pinhead', 'racketeer', 'simpleton', 'sinner', 'slippery eel',
                'thug', 'tomfool', 'twit', 'wrongdoer', 'yardbird',
            ]
            self.output.text = ("You are a " + choice(insult1) + " " +
                choice(insult2) + " " + choice(insult3)+ ".")
            
----

.. admonition:: Tasks

    #. Create a random compliment maker. Use the lists below as a starting point.

        .. code-block:: python

            term1 = ['affectionate', 'altruistic', 'amiable', 'amicable',
                'beneficent', 'benevolent', 'bounteous', 'charitable',
                'compassionate', 'congenial', 'considerate', 'cordial',
                'courteous', 'friendly', 'gentle', 'good-hearted', 'gracious',
                'humane', 'humanitarian', 'kindhearted', 'kindly', 'loving',
                'neighborly', 'obliging', 'philanthropic', 'softhearted',
                'sympathetic', 'tenderhearted', 'thoughtful', 'tolerant',
                'understanding'
            ]
            term2 = ['able', 'adept', 'agile', 'alert', 'astute',
                'bold', 'brainy', 'bright', 'brilliant', 'brisk', 'canny',
                'clever', 'consummate', 'cool', 'crafty', 'cultivated',
                'effective', 'eggheaded', 'expert', 'fresh', 'genius',
                'gifted', 'good', 'hip', 'ingenious', 'keen', 'knowing',
                'masterly', 'nimble', 'on the ball', 'polished', 'practiced',
                'proficient', 'quick', 'quick-witted', 'ready', 'resourceful',
                'sassy', 'savvy', 'sharp', 'shrewd', 'skillful', 'slick',
                'talented', 'wise', 'wised up', 'with it'
            ]
            term3 = ['academician', 'architect', 'author', 'brain', 'builder',
                'child genius', 'creator', 'designer', 'egghead', 'Einstein',
                'experimenter', 'founder', 'freak', 'genius', 'good egg',
                'good guy', 'good person', 'highbrow', 'innovator',
                'intellect', 'intellectual', 'maker', 'man of his word',
                'man of honor', 'marvel', 'mastermind', 'miracle',
                'moonwalker', 'natural', 'nice guy', 'one in a million',
                'originator', 'phenomenon', 'pioneer', 'polished man',
                'prodigy', 'rarity', 'refined man', 'rocket scientist',
                'sage', 'scholar', 'sensation', 'spectacle', 'star person',
                'stunner', 'talent', 'whiz', 'whiz kid', 'wizard', 'wonder',
                'wonder child', 'wunderkind'
            ]