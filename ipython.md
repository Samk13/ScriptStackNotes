# Ipython

- [forgot the name of a function](https://youtu.be/3i6db5zX3Rw?t=301)

```ipython
import os
In [14]: os.*dir*?
os.__dir__
os.chdir
os.curdir
os.fchdir
os.listdir
os.makedirs
os.mkdir
os.pardir
os.removedirs
os.rmdir
os.scandir
os.supports_dir_fd
```

- Input command of previous sessions are stored with:

_i, -ii
-ih[<cell number>]
- add ";" to the end of the command will tell python to not cash the result

```python
In [16]: _i
Out[16]: '-i'
In [17]: _ii
Out[17]: '-i'
In [18]: _i14
Out[18]: 'os.*dir*?'
```

## Magic functions
Magic functions starts with `%` or `%%`, example: `%history`

magic functions don't require parenthesis when passing commands

if a function start with 2 percentage signs that means it is a cell magic function

You need to press enter twice when you run `%%` to tell that you are done typing the command
## List of magic functions you can find [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

`%who` will print all interactive available available


- you can write your own magic functions by decorate it with `@register_line_magic`
or `@register_cell_magic`

- any command that starts with `!` will be treated as a shell command

`rehashx`load all executables from $path int the alias table

## Config IPython
On fresh install the config file is not there so you need to create with the command: `ipython profile create`
- the configuration lives in: `~/.ipython/profile_default/ipython_config.py`

## set Ipython as your debugger:

you add this line where you want to poke around and see what's going on:
```python
from IPython import embed; embed()
```
when you are done you can exit the embed the code execution will continue, note that if you change some variables values, these changes will still exist after closing the session

this methode is not really debugging, to run the pdb:

```console
%run -d my-file.py
```

## Post mortem debugger
`%debug`

if you want the execution to stop when the exception happen you can use
`%pdb`

## masure time
`%time`

`%timeit`

`prun` -> will give nice overview of the function run information



