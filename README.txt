About
------
The mechanism system is an application for automating mechanism design.
It is written in the Adaptive Modeling Language (AML).


Integrating with AML (on Windows)
---------------------------------
In the folder where AML is installed, usually:
C:\Program Files\Technosoft\AML\"AML-version",
add a line in logical.pth that looks like this:
:mechanism-system	"path-to-the-mechanism-system-folder"

The system requires the module 
aml-analysis-module-pack-type-3

To load this module, write 
(load-module "aml-analysis-module-pack-type-3" :path "path-to-the-module-folder")
in aml-init.tsi, also found in the folder where AML is installed.

When in AML's Main Modeling Form, the new model from class has to be 
main-mechanism-class

If the paths from the :tmp and :temp entries in logical.pth does not exist,
change the paths or create the subsequent folder

For Nastran export:
Add the following entries in logical.pth:
1) :nastran-path, pointing to the \bin\ folder
in your Nastran installation folder, e.g: 
"C:\Program Files\Siemens\NX 10.0\NXNASTRAN\bin\"

2) :nastran-data, pointing to wherever the nastran output files shall be stored

For AMOpt:


Optional:
For automatic compilation of the system on AML startup, write
(compile-system :mechanism-system)

in aml-init.tsi.


Authors
-------
Anders Kristiansen
Eivind Kristoffersen
Rasmus Korvald Skaare