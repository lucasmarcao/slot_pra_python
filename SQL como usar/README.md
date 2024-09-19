53

python -m auto_py_to_exe
python -m auto_py_to_exe
python -m auto_py_to_exe
python -m auto_py_to_exe

I am not using Vue, but had the same problem.

I already had the settings

Editor: default formatter to prettier
Editor: Format on Save to true
I already had .eslintrc.js and .prettierrc files But nothing worked.
The solution to my problem was that I had all set properly, except I needed to:

Command + Shift + p

type format document with

select Configure Default Formatter...

select Prettier as default.

I don't know why the Editor:
Format on Save set to true was not enough.
I needed to select default
formatter using the above steps so it worked.

format document with

format document with
