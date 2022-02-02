# Wordle Solver

This is a small Python script that helps to solve a [Wordle](https://www.powerlanguage.co.uk/wordle/) (so not really a complete solver).

Of course this is cheating and takes the fun out of the actual game.
On the other hand, it was fun for me to write it, as a little exercise.
So there you go.

The solver works by starting with a word list and then applying list comprehension with [`all()`](https://docs.python.org/3/library/functions.html#all), [`any()`](https://docs.python.org/3/library/functions.html#any) and a regex match.

## Requirements

You need Python 3 and a dictionary file such as the one usually found at `/usr/share/dict/words`.

## Usage

```
usage: suggest_words.py [-h] [-d DICTIONARY] [-p PRESENT] [-n NOT_PRESENT] [-r PATTERN]
                        [-i] [--no-interactive]

Suggest solutions to Wordle based on some constraints.

optional arguments:
  -h, --help            show this help message and exit
  -d DICTIONARY, --dictionary DICTIONARY
                        Dictionary file to use as the starting point. Default is
                        '/usr/share/dict/words'.
  -p PRESENT, --present PRESENT
                        All letters that we know are in the word, all in one string.
                        Default is '' (emtpy string).
  -n NOT_PRESENT, --not-present NOT_PRESENT
                        All letters that we know are not in the word, all in one
                        string. Default is '' (emtpy string).
  -r PATTERN, --pattern PATTERN
                        Regex pattern we know the word must match. Default is '.....'.
  -i, --interactive     Run in interactive mode.
  --no-interactive      Run in non-interactive mode (default).
```

## Example (interactive mode)

In interactive mode, you're prompted to enter the word you tried in Wordle, and then the answer that Wordle gave you.
Based on these inputs, the wordle solver will define the constraints and suggest a list of matching words.
This goes on until you enter `+++++` as Wordle's answer.

```
$ python suggest_words.py --interactive
running in interactive mode
Enter Wordle's answer as follows:
- '+' for: letter is in word and in correct spot (green)
- '?' for: letter is in word but not in correct spot (yellow)
- '-' for: letter is not in word (grey)
What is your word?        noise
What is Wordle's answer?  ?+---
May I suggest the following options:
bogan  Bonbo  Bongo  bongo  Bonny  bonny  boonk  Boran  boron  bound  bourn  codon  cogon  Colan
colon  Coman  conal  conch  conga  Congo  conky  Conor  Conoy  conto  coony  cornu  corny  count
Cowan  coyan  Donal  Donar  donax  donga  Donna  donna  donor  donum  downy  fogon  fondu  fonly
found  fount  goban  gonad  gonal  goran  gowan  hogan  Hokan  honda  hondo  honor  Honzo  horny
hound  Iowan  Johan  Jonah  koban  kokan  konak  Kongo  kongu  Koran  koyan  lohan  longa  loony
loran  lowan  monad  monal  Mongo  monny  month  Montu  Monty  moony  moorn  Mopan  Moran  moron
mound  mount  mourn  Norna  pohna  Pokan  Ponca  Pondo  pondy  ponga  Pongo  ponja  ponto  pound
rogan  rohan  rohun  Roman  ronco  rondo  Ronga  rotan  round  rowan  Solon  Songo  Sonja  Sonny
tolan  toman  tonal  Tonga  tonga  Tonna  Tonto  Toona  toran  tourn  towan  towny  toxon  toyon
woman  wonga  wonky  wonna  wound  xoana  yojan  young  yourn  zogan  zonal  zonar  Zonta
What is your word?        month
What is Wordle's answer?  ++??-
May I suggest the following options:
mount
What is your word?        mount
What is Wordle's answer?  +++++
Congratulations!
```

## Example (non-interactive mode)

In non-interactive mode, you need to pass all constraints as parameters.

### Attempt 1

Start with any word, e.g. `saint`. Wordle might answer this:

⬛⬛⬛⬛🟩

This means that we know that the last letter is indeed a `t`. 
We also know that `s`, `a`, `i` and `n` are not present in the word.

### Attempt 2

We can now run the solver to suggest possible words for our next attempt.

```shell
$ python suggest_words.py --present t --not-present sain --pattern "....t"

['Ahmet', 'Aleut', 'becut', 'bedot', 'beget', 'begut', 'beret', 'bewet', 'blout', 'bluet', 'blurt', 'boort', 'bowet', 'Brett', 'brett', 'buret', 'Burut', 'cheet', 'chert', 'chort', 'chott', 'cleft', 'cloot', 'clout', 'comet', 'court', 'covet', 'crept', 'croft', 'crout', 'cruet', 'crypt', 'culet', 'debut', 'delft', 'depot', 'dompt', 'doubt', 'dropt', 'duvet', 'dwelt', 'educt', 'egret', 'Egypt', 'eject', 'elect', 'Eleut', 'elvet', 'emmet', 'epopt', 'erect', 'erept', 'ergot', 'eruct', 'erupt', 'evert', 'exert', 'exult', 'fleet', 'flout', 'freet', 'frett', 'fumet', 'gemot', 'gleet', 'glout', 'godet', 'greet', 'groot', 'grout', 'Helot', 'humet', 'kempt', 'lerot', 'loket', 'lucet', 'motet', 'mpret', 'mulct', 'Murut', 'octet', 'orlet', 'ortet', 'ought', 'overt', 'owght', 'owlet', 'pecht', 'plout', 'poult', 'queet', 'rebut', 'recut', 'reget', 'relet', 'relot', 'repot', 'revet', 'rewet', 'robot', 'rovet', 'rowet', 'royet', 'Scott', 'Soyot', 'Tebet', 'tellt', 'tempt', 'theet', 'theft', 'thoft', 'thort', 'thowt', 'thurt', 'troft', 'troot', 'trout', 'tweet', 'upcut', 'upget', 'upjet', 'veldt', 'volet', 'wecht', 'wevet', 'wheft', 'whewt', 'whort']
```

Let's try `crypt`.
Wordle answers:

⬛🟨⬛⬛🟩

Now we know that `r` is one of the letters in the solution, but not in  second position.
`c`, `y` and `p` are not letters in the solution.

### Attempt 3

We can run the solver again, this time with updated constraints:

```shell
$ python suggest_words.py --present rt --not-present saincyp --pattern ".[^r]..t"

['beret', 'blurt', 'boort', 'buret', 'Burut', 'egret', 'evert', 'exert', 'lerot', 'Murut', 'overt', 'rebut', 'reget', 'relet', 'relot', 'revet', 'rewet', 'robot', 'rovet', 'rowet', 'thort', 'thurt', 'whort']
```

Let's try another one, this time `exert` (not smart, I know...).
Wordle answers:

⬛⬛⬛🟨🟩

Now we know even more: `r` is also not in fourth position, `e` and `x` are not present.

### Attempt 4

Translated to solver parameters this means:

```shell
$ python suggest_words.py --present rt --not-present saincypex --pattern ".[^r].[^r]t"

['Burut', 'Murut', 'robot']
```

Out of these three, only `robot` looks like a good choice, so let's try that.

And to this Wordle says:

🟩🟩🟩🟩🟩

Hooray!

---

2022, Knud Möller