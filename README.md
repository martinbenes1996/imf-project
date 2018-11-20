
# Description #
Project ImplyPlot was done for subject Fuzzy Logic Foundations.
It demonstrates fuzzy implication forms, it was done for educational
purposes.

# Usage #
There are three functions prepared for you:

* plotImplication(<implicator>, <negator>)
* plotNegator(<negator>)
* plotClassicImplication()

## Implicators ##
There are 4 different implicator types implemented in the project. They are given to the plotter functions
at the <implicator> parameters. The parameter must be replaced by one of the following method names:

* Implicator.maximum (default)
* Implicator.probsum
* Implicator.drastic
* Implicator.lukasiewicz

For more information, read the specific method documentation.

## Negators ##
There are 5 different negator types implemented in the project. THey are given to the plotter functions
at the <negator> parameters. The parameter must be replaced by one of the following method names:

* Negator.standard (default)
* Negator.godel
* Negator.dualgodel
* Negator.sugen
* Negator.yager

Sugen and Yager negator coefficients are defaultly 2. This might be set by methods:

* Negator.setSugenCoef(newvalue)
* Negator.setYagerCoef(newvalue)

For more information, read the specific method documentation.

# Credits #
Author: Martin Benes.


