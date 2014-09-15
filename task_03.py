#!/usr/bin/env python

"""task_03.py: Homework Task 3."""

__author__      = "Joe Graham"

# constants
COLOR_TYPES = ['Base', 'Accent', 'Highlight']
COLOR_PROMPT = "Please enter {} color:"
CHOICES_PROMPT = "Choices are: {}"
INVALID_CHOICE = "Invalid choice, please select again."
COLORS = {
    'Seattle Gray': {
        'Ceramic Glaze': {
            'Basically White',
            'White'
        },
        'Cumulus Nimbus': {
            'Off-White',
            'Paper White'
        }
    },
    'Manatee': {
        'Platinum Mist': {
            'Bone White',
            'Just White'
        },
        'Spartan Sage': {
            'Fractal White',
            'Not White'
        }
    }
}


# members
colorTypeIdx = 0
isBaseValid = False
isAccentValid = False
isHighlightValid = False

BASE = ""
ACCENT = ""
HIGHLIGHT = ""
answer = ""
colorList = COLORS.keys()

while not isBaseValid:
    print COLOR_PROMPT.format(COLOR_TYPES[colorTypeIdx])
    print CHOICES_PROMPT.format(', '.join(colorList))
    baseColor = raw_input()
    if baseColor in colorList:
        isBaseValid = True
        colorList = COLORS[baseColor].keys()
        colorTypeIdx += 1
        BASE = baseColor
        while not isAccentValid:
            print COLOR_PROMPT.format(COLOR_TYPES[colorTypeIdx])
            print CHOICES_PROMPT.format(', '.join(colorList))
            accentColor = raw_input()
            if accentColor in colorList:
                isAccentValid = True
                colorList = list(COLORS[baseColor][accentColor])
                colorTypeIdx += 1
                ACCENT = accentColor
                while not isHighlightValid:
                    print COLOR_PROMPT.format(COLOR_TYPES[colorTypeIdx])
                    print CHOICES_PROMPT.format(', '.join(colorList))
                    highlightColor = raw_input()
                    if highlightColor in colorList:
                        isHighlightValid = True
                        HIGHLIGHT = highlightColor
                    else:
                        print INVALID_CHOICE
                        continue
            else:
                print INVALID_CHOICE
                continue
    else:
        print INVALID_CHOICE
        continue

print "Thanks, your color choices are Base: {}, Accent: {}, Highlight: {}".format(BASE, ACCENT, HIGHLIGHT)