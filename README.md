# IMF project

## Description
Project ImplyPlot was done for subject Fuzzy Logic Foundations.
It demonstrates fuzzy implication forms, it was done for educational
purposes.

## Usage
Library is written in Python3 and uses *numpy* and *matplotlib*. To run it,
change directory to the main project file and type one of the following commands:

* $ python3 -i implyplot.py
* $ ./run.sh
* $ make run

All of them imports the library at Python3 interactive mode and then waits for the
user input. There are three functions prepared for you:

* plotImplication(<implicator>, <negator>)
* plotNegator(<negator>)
* plotClassicImplication()

For more information, read the specific method documentation.

### Implicators
There are 4 different implicator types implemented in the project. They are given to the plotter functions
at the <implicator> parameters. The parameter must be replaced by one of the following method names:

* Implicator.maximum (default)
* Implicator.probsum
* Implicator.drastic
* Implicator.lukasiewicz

For more information, read the specific method documentation.

### Negators
There are 5 different negator types implemented in the project. THey are given to the plotter functions
at the <negator> parameters. The parameter must be replaced by one of the following method names:

* Negator.standard (default)
* Negator.godel
* Negator.dualgodel
* Negator.sugen
* Negator.yager
* Negator.circle
* Negator.parabolic

Sugen and Yager negator coefficients are defaultly 2. This might be set by methods:

* Negator.setSugenCoef(newvalue)
* Negator.setYagerCoef(newvalue)

For more information, read the specific method documentation.



