# mvc-dj-bpm

This project is to my own implementation of DJ MVC presented in chapter 12 of Head First Pattern (p. 528)

## Using virtual environment

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment:

In windows:

    . ./.venv/Scripts/activate

In linux:

    source .venv/bin/activate

## Install the libraries

    pip install .

or

    pip install .[test]

## Run the application

    python main.py

## Run the tests

    pytest -v

## Run Docker container

    docker build -t mvc-dj-bpm . && docker run --rm --name "mvc-dj-bpm" mvc-dj-bpm
