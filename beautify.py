## TODO:
## 1. Make an "advanced" mode functionality, which would allow to set the color manually


def wrap(line, toFind, left = 'k', right = '\033[0m'):
	wrapped = []

	for word in line.split():
		if word == toFind:
			wrapped.append( left + word + right )
		else:
			wrapped.append(word)
		# print(wrapped)
	
	return ' '.join(wrapped)


def beautify(text: str, markups: dict, bold: bool = True, position: str = 'fg'):
	## Colors
	colors = {
		'red': '230;18;33',
		'pink': '224;93;175',
		'purple': '178;16;235',
		'blue': '36;100;255',
		'teal': '16;235;186',
		'green': '19;209;29',
		'yellow': '242;240;48',
		'orange': '242;139;48'
	}

	assert type(markups) == dict, "`markups` should be a dictionary"
	# assert mode in ['basic', 'advanced'], "Unknown value for `mode` (May be: \"basic\", \"advanced\")"
	assert position in ['fg', 'bg'], "Unknown value for `position` (May be: \"fg\", \"bg\")"

	text = text.split('\n')

	for markupWord in markups.keys():
		for pos, line in enumerate(text):
			if markupWord in line:
				text[pos] = wrap(line, markupWord, f'\033[{"38" if position == "fg" else "48"};2;{colors[markups[markupWord]]}{";1" if bold else ""}m')
	
	return '\n'.join(text)