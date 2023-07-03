# Quick Translate(v0.2)
### About The Project
A python app that translates texts by opening popups
### Built with
* AHK
* Libre Translate

## Run quick-translate.exe
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

Now you can translate text by selecting and press Ctrl+&lt;choosen key&gt;

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


## Run Python
### Download & Install
* Clone this repository
```sh
git clone https://github.com/BawerMY/quick-translate
```
* Enter in the project directory
```sh
cd quick-translate
```
* Install the required modules
```sh
pip install -r requirements.txt
```
### Configuration-Settings
Default settings:
* Output Language: English
* Run Shortcut: Ctrl+Q
* For change the settings open the config.json file in the project directory
it should be like:
```json
{
    "lang": "en",
    "key": "q"
}
```
* For change the output language edit the "lang" item to the acronym of the language desired(default = "en": English)
* For change the shortcut key change the "key" item to the key desired(the shortcut will be Ctrl+&lt;choosen key&gt;)(default = "q": Q)
### Run
#### Activate quick-translate
* Windows
```sh
python quick-translate(background).pyw
```
* MacOS & Linux
```sh
python3 quick-translate(background).pyw
```
#### Translate
* For translate a text select it and press the dedicated shortcut(Default: Ctrl+Q)
* For close the translation popup click it








