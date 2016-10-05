AML Mechanism system (Updated 26.09.16)
https://github.com/NTNU-IPM/KBE

========

The mechanism system is an application for automating mechanism design.
It is written in the Adaptive Modeling Language (AML).

Features
========

- Automatic generation and meshing of 3D-models
- Exports pre-processed files to FEDEM


Required software
=========

AML 6.31
Siemens PLM Software NX (with NX Nastran)
Fedem

Installation
========

To install the AML mechanism system, the files logical.pth and aml-init.tsi
have to be modified, they are placed in the root of the AML isntallation folder,
usually:
    "C:\Program Files\Technosoft\AML\AML6.31.1_x64\"


In logical.pth add this line:
    :mechanism-system "Path to the folder of the mechanism-system "

e.g.:
    :mechanism-system "C:\AML\NTNU-IPM-KBE-d87408d\"

Create the folder "analysis" in the temp folder.
    "C:\temp\analysis\"

Note: If the paths from the :tmp and :temp entries in logical.pth does not exist,
      change the paths or create the subsequent folder


Modules
--------
Required modules:
    aml-analysis-module-pack-type-3
    aml-analysis-module-pack-type-3_ui
    amsketcher-module


To install, place the reqiured modules in the modules folder,
and add these lines in aml-init.tsi:

    (load-module "aml-analysis-module-pack-type-3")
    (load-module "amsketcher-module")
    (load-module "aml-analysis-module-pack-type-3_ui")


Modules folder: "C:\Program Files\Technosoft\AML\AML6.31.1_x64\modules\"


Nastran export
-----------
Add the following entries in logical.pth:

    :nastran-path, pointing to the \bin\ folder in your Nastran installation folder
    :nastran-data, pointing to wherever the nastran output files is to be stored

e.g.:
    :nastran-path "C:\Program Files\Siemens\NX 10.0\NXNASTRAN\bin\"
    :nastran-data "C:\AML\NTNU-IPM-KBE\nastran-data\"


Automatic startup (optional)
------------
For automatic startup of the mechanism system on AML startup,
add these lines in aml-init.tsi:

    (compile-system :mechanism-system)
    (create-model 'main-mechanism-class)
    (display-sketcher-main-form)


AMOpt
------------
???



Authors
=======
Anders Kristiansen
Eivind Kristoffersen
Rasmus Korvald Skaare
