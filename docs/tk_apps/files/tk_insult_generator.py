import tkinter as tk
from random import choice

# Constants
BG_COLOR = "#ffffff"
TITLE_COLOR = "#212121"
TEXT_COLOR = "#444444"
PRIMARY_COLOR = "#2196f3"  # blue
SECONDARY_COLOR = "#e91e63"  # pink
BUTTON_FG_COLOR = "#ffffff"
OUTPUT_BG_COLOR = "#f5f5f5"
TITLE_FONT = ("Arial", 28, "bold")
FONT_STYLE = ("Arial", 16)
BUTTON_FONT = ("Arial", 18)
OUTPUT_FONT = ("Arial", 20)

# Word lists for the Shakespearean insult
OLD_INSULT1 = ['artless', 'bawdy', 'beslubbering', 'bootless',
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
               'yeasty']
OLD_INSULT2 = ['base-court', 'bat-fowling', 'beef-witted',
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
               "unwash'd", 'weather-bitten', 'whoreson']
OLD_INSULT3 = ['apple-john', 'baggage', 'barnacle', 'Basket-Cockle',
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
               'whey-face']

# Word lists for the modern insult
MODERN_INSULT1 = ['animalistic', 'appalling', 'awful', 'bad-looking',
                  'beastly', 'deformed', 'disfigured', 'foul', 'frightful',
                  'grisly', 'gross', 'grotesque', 'hard-featured', 'hideous',
                  'horrid', 'ill-favored', 'loathsome', 'misshapen',
                  'monstrous', 'not much to look at', 'repelling', 'repugnant',
                  'repulsive', 'revolting', 'unbeautiful', 'uncomely',
                  'uninviting', 'unlovely', 'unsightly']
MODERN_INSULT2 = ['abrupt', 'abusive', 'bad-mannered', 'barbaric',
                  'barbarous', 'blunt', 'boorish', 'brusque', 'brutish',
                  'cheeky', 'churlish', 'coarse', 'crabbed', 'crude', 'curt',
                  'discourteous', 'graceless', 'gross', 'gruff', 'ignorant',
                  'illiterate', 'impertinent', 'impolite', 'impudent',
                  'inconsiderate', 'insolent', 'insulting', 'intrusive',
                  'loutish', 'obscene', 'raw', 'savage', 'scurrilous', 'surly',
                  'uncivil', 'uncivilized', 'uncouth', 'uncultured',
                  'uneducated', 'ungracious', 'unmannerly', 'unpolished',
                  'unrefined', 'vulgar', 'wild']
MODERN_INSULT3 = ['bad guy', 'bad person', 'baddie', 'baddy',
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
                  'thug', 'tomfool', 'twit', 'wrongdoer', 'yardbird']


def show_output(message):
    """Replaces the text in the output box with message."""
    output_text.delete(1.0, "end")
    output_text.insert(1.0, message)


def make_old_insult():
    """Builds a random Shakespearean insult from one word in each list."""
    insult = ("Thou art a " + choice(OLD_INSULT1) + " " +
              choice(OLD_INSULT2) + " " + choice(OLD_INSULT3) + ".")
    show_output(insult)


def make_insult():
    """Builds a random modern insult from one word in each list."""
    insult = ("You are a " + choice(MODERN_INSULT1) + " " +
              choice(MODERN_INSULT2) + " " + choice(MODERN_INSULT3) + ".")
    show_output(insult)


# Create the main window
root = tk.Tk()
root.title("Insult generator")
root.geometry("680x360")
root.configure(bg=BG_COLOR)

# Create widgets
title_label = tk.Label(root, text="Random Insults", bg=BG_COLOR,
                       fg=TITLE_COLOR, font=TITLE_FONT)
instructions_label = tk.Label(root, text="Choose an insult style.", bg=BG_COLOR,
                              fg=TEXT_COLOR, font=FONT_STYLE)
old_insult_button = tk.Button(root, text="Shakespearean Insult", width=18,
                              bg=SECONDARY_COLOR, fg=BUTTON_FG_COLOR,
                              font=BUTTON_FONT, command=make_old_insult)
insult_button = tk.Button(root, text="Modern Insult", width=18,
                          bg=PRIMARY_COLOR, fg=BUTTON_FG_COLOR,
                          font=BUTTON_FONT, command=make_insult)
# Text widget: 3 lines high, 40 characters wide, long text wraps at whole words
output_text = tk.Text(root, height=3, width=40, wrap="word",
                      bg=OUTPUT_BG_COLOR, fg=TEXT_COLOR, font=OUTPUT_FONT)

# Share any spare width equally between the 2 columns, so the widgets stay centred
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Place widgets in the window
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 5))
instructions_label.grid(row=1, column=0, columnspan=2, pady=5)
old_insult_button.grid(row=2, column=0, padx=10, pady=15)
insult_button.grid(row=2, column=1, padx=10, pady=15)
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
