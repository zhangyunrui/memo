- find all files containing specific text
  `grep <--include=\*.{c,h}> -rnw '/path/to/somewhere/' -e 'pattern'`
  - `-r` or `-R` is recursive,
  - `-n` is line number, and
  - `-w` stands for match the whole word.
  - `-l` (lower-case L) can be added to just give the file name of matching files.
  - `--include=\*.{c,h}`
  - `--exclude=*.o`
  - `--exclude-dir={dir1,dir2,*.dst}`
