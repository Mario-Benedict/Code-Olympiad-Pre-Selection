# Code Olympiad Pre-Selection

## (Mariar Air Quality Index Checker)

### Requirement

- _MongoDB on local machine installed_ **OR** _Cloud based MongoDB_
- _Redis on local machine installed_ **OR** _Cloud based Redis_
- _MongoDB Compass GUI on local machine_
- _python 3.10.6_ **OR** _newer_
- _python venv_
- _Makefile system_ (optional)
- _.editorconfig vscode extension_ (optional)

### Installation

- _Clone this repository_ **OR** _download as zip, rar, tar, etc (you need to extract them)_
- _Follow this instruction to install python venv_

  ```sh
  Mac
  $ cd Code-Olympiad-Pre-Selection
  $ python -m venv env
  $ source env/bin/activate
  $ pip install -r requirements.txt

  Linux
  $ cd Code-Olympiad-Pre-Selection
  $ python -m venv env
  $ . env/bin/activate
  $ pip install -r requirements.txt

  Windows
  $ cd Code-Olympiad-Pre-Selection
  $ python -m venv env
  $ env\Scripts\activate
  $ pip install -r requirements.txt
  ```

- _Create .env file in root directory_ (you can use my .env.example as a template)
- _Extract the data.zip file_ (you can use 7zip, winrar, etc)
- _Import CSV file to MongoDB Compass GUI_
- _Run the app_ (you can use makefile or run it manually)

  ```sh
  $ python main.py

  OR

  $ make run
  ```

- _Run the test_ (For Development)

  ```sh
  $ pytest

  OR

  $ make test
  ```

- _Press CTRL + C **OR** CMD + C to stop the app_
