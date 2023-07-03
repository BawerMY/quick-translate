# Quick Translate(v0.2)
**[About The Project](#about-the-project)**<br>
**[Run quick-translate.exe](#run-quick-translate-exe)**<br>
**[Run With Python](#run-with-python)**<br>
**[How To Translate](#translate)**<br>
## About The Project
A python app that translates texts by opening popups
### Built with
* AHK
* Libre Translate

## Run quick translate exe
* Go to https://github.com/BawerMY/quick-translate/tree/main/exe/
* Download the prefered version (console-background)
### quick-translate(console):
* Run quick-translate(console).exe (if the console remains blank press enter on the keyboard)
* Choose the output language:
```
Enter quick-translate output language(acronym)(default en):
```
* Choose the keyboard shortcut:
```
Enter quick-translate shortcut key(default q):
```
The shortcut will be Ctrl+&lt;choosen key&gt;

* For translate a text select it and press the dedicated shortcut(Default: Ctrl+Q)
* For close the translation popup click it

### Run quick-translate(background).exe
* Download or create quick-translate(background).config.json
* edit "lang" and "key" fields by your preferences:
* "lang": output languages acronym(default "en")
* "key": translate shortcut key(the shortcut will be Ctrl+&lt;choosen key&gt)(default "q")
```json
{
  "lang": "en",
  "key": "q"
}
```
 Run quick-translate(background).exe
* For translate a text select it and press the dedicated shortcut(Default: Ctrl+Q)
* For close the translation popup click it

## Run With Python
### Download & Install
* Clone this repository
```sh
git clone https://github.com/BawerMY/quick-translate/
```
* Enter in the project directory
```sh
cd quick-translate
```
* Install the required modules
```sh
pip install -r requirements.txt
```

### Setup & Run
* Select the prefered version (console-background):
#### quick-translte(console).py
* Run quick-translate(console).py (if the console remains blank press enter on the keyboard)
* Choose the output language:
```
Enter quick-translate output language(acronym)(default en):
```
* Choose the keyboard shortcut:
```
Enter quick-translate shortcut key(default q):
```
The shortcut will be Ctrl+&lt;choosen key&gt;


* For translate a text select it and press the dedicated shortcut(Default: Ctrl+Q)
* For close the translation popup click it
#### quick-translate(background).pyw
* Edit quick-translate(background).config.json
* edit "lang" and "key" fields by your preferences:
* "lang": output languages acronym(default "en")
* "key": translate shortcut key(the shortcut will be Ctrl+&lt;choosen key&gt)(default "q")
```json
{
  "lang": "en",
  "key": "q"
}
```
* Run quick-translate(background).pyw
* Windows
```sh
python quick-translate(background).pyw
```
* MacOS & Linux
```sh
python3 quick-translate(background).pyw
```
* For translate a text select it and press the dedicated shortcut(Default: Ctrl+Q)
* For close the translation popup click it
## Translate
* For translate a text select it and press the dedicated shortcut(Default: Ctrl+Q)
* For close the translation popup click it








