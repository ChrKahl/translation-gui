# Translation-GUI

> Under construction

Currently there's a commandline tool available which gets the missing keys from one file to another.

**Pay attention: The dst-file will be overwritten!**

```bash
./translate.py <src-file-path> <dst-file-path>
```

---

## Todos

### For commandline

* offer more arguments via command line
  * dst-file storage-location
* check if there are childnodes
* improve UI
* autoremove duplicate keys with same values
* sort alphabetically


### For GUI

* build the GUI
* display list of unmatched keys
* display translation of unmatched keys
* add input the user can enter the new value
* add a save-button
* add an abort-button
* add auto-save onChange?
* add two fields to load source and destination files

---

## Goal
Just a little interface to diff between translation files from react-intl
