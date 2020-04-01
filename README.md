# Translation-GUI

> Under construction

Currently there's a commandline tool available which gets the missing keys from one file to another.

Manually add values only for missing keys that are in src-file but not in dst-file.

```bash
./translate.py <src-file-path> <dst-file-path>
```

Automatically add key-values that are not in dst-file.

```bash
./translate.py <src-file-path> <dst-file-path>
```

To find differences between src-file and dst-file and select for each value which to use.
Add all keys distinct in each file.

```bash
./translate.py --diff <src-file-path> <dst-file-path>
```

Write to out-file-path (Default: `./data/out/out.json`)

```bash
./translate.py --out <out-file-path> <src-file-path> <dst-file-path>
```

---

## Todos

### For commandline

- [] offer more arguments via command line
- [] * dst-file storage-location
- [] check if there are childnodes
- [] improve UI
- [] autoremove duplicate keys with same values
- [] sort alphabetically


### For GUI

- [] build the GUI
- [] display list of unmatched keys
- [] display translation of unmatched keys
- [] add input the user can enter the new value
- [] add a save-button
- [] add an abort-button
- [] add auto-save onChange?
- [] add two fields to load source and destination files

---

## Goal
Just a little interface to diff between translation files from react-intl
