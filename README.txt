About
------
The mechanism system is an application for automating mechanism design.
It is written in the Adaptive Modeling Language (AML).


Integrating with AML (on Windows)
---------------------------------
In the folder where AML is installed, usually:
C:\Program Files\Technosoft\AML\AML5.85_x64 ,
add a line in logical.pth that looks like this:
:mechanism-system	path-to-the-mechanism-system-folder

The system requires the module 
aml-analysis-module-pack-type-3

To load this module, write 
(load-module "aml-analysis-module-pack-type-3" :path path-to-the-module-folder)

in aml-init.tsi, also found in the folder where AML is installed.

When in AML's Main Modeling Form, the new model from class has to be 
mechanism-collection

Optional:
For automatic compilation of the system on AML startup, write
(compile-system :mechanism-system)

in aml-init.tsi.


Authors
-------
Rasmus Korvald Skaare
Anders Kristiansen
Eivind Kristoffersen