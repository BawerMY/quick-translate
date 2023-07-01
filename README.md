# Quick Translate(v1.0)
## Built with
* AHK
* libretranslate

## Getting Started
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
### Run
* Windows
```sh
python main.pyw
```
* MacOS & Linux
```sh
python3 main.pyw
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










