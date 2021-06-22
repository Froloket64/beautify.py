# Beautify

`Beautify` provides (hopefully) an easy-to-use API to make output of your programs more colorful, and thus, **beautiful**.

**PS**: Tested only on `Python3` v3.8+ . No guarantees to work on `Python2`.
## Installation
### Using `pip`
_coming soon..._

### Manually
Clone the repo
``` sh
git clone https://github.com/Froloket64/beautify.py.git beautify/

cd beautify
```
then put the `beautify.py` in your project folder.
(yeah, that doesn't look too useful though)

## Usage
To import the module, simply add the line:
``` python
from beautify import beautify
```
this would import the `beautify` function which's all you need.

Invocation:
``` python
beautify(wholeText, {wordToMark: color, wordToMark2: color2})
```
This only **returns** the markupped text. To print, wrap it in `print()`

Also, unrequired arguments are:
``` python
bold     # Markup width (default: True)
position # Markup position relative to the text. Can be "fg" for foreground and "bg" for background (default: 'fg')
```

## Examples
_coming soon..._