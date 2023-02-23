<br />
<br />

<h1 align="center">
RTF-to-CSV
</h1>

<br />
<br />

<p align="center">
This program reads analyzed report file with <code>.rtf</code> and extracts necessary values & inputs in a created <code>.csv</code> file. This simple program is built using python and can be run via any UNIX/LINUX environment.
</p>

<br />
<br />

## About this program

If you have question or find bugs in the main program, please send the issue via [hanchoi@ucdavis.edu](mailto:hanchoi@ucdavis.edu).

Please read teh documentations carefully to run the program.

<br />
<br />

### Documentations

<br />

#### Requirements

This program requires that you have python version `>3.8`. All the necessary dependencies have been listed in the `requirements.txt` file. Because this program has path resolving functions that is based on the Unix/Linux path pattern, it is likely that you will encounter program bugs if you are on window or any other OS other than Unix/Linux.

<br />

#### Installations

> **Option 1. Installing Source Via `.zip`**

Click the download as `.zip` in the repositories top right button. Then, integrate in your code editor & integrated terminal to run the program.

<br />

> **Option 2. Installing Source Via Cloning Repo**

```bash
# bash
git clone rtf-csv https://github.com/haneulab/blozis-lab-rtf-csv.git
# instantiate virtual environment
python -m venv env
# install required packages
pip install -u requirements.txt
# source bashrc
source .bashrc
```

Once you've done that, check with version command,

```bash
rtf-csv --version # or rtf-csv -v
# you can also find list of flag commands to be ran with the 'run' command when running the program
rtf-csv run --help # or run -h
```

<br />

#### Topics

<br />

##### Injecting Initial Dataset

In the `src` directory, you should create a directory called `data` where you will collect the set of data `rtf` files.

```
# root
- src
    - data
        - C300_40_10
        - C100_40_10
            - timingML.rtf
            - timingREML.rtf
            ...
```

<br />

##### Running The Program

In order to run the program, assuming that you've already sources `.bashrc` file into the working directory, you need the command as a combination of

- `rtf-csv run`
- `--flag`
  - `--help | -h` : Lists a list of flag commands and explanations
  - `--test | -t` : Running comparison test between actual output vs expected output of `.csv` inputs.
  - `--build | -b` : Builds from `src/data` to `build` a `.csv` file.

<br />

##### Customizing Program Functions

<br />

###### Default Structure

<br />

###### Customizations

<br />

##### Building The `.csv` File

<br />
<br />
