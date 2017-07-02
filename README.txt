AML Mechanism system

Latest version: https://github.com/thorcc/RaMMS
========

RaMMS is an application for automating mechanism design.
It is written in the Adaptive Modeling Language (AML).

Features
========

- Automatic generation and meshing of 3D-models
- Export pre-processed files to FEDEM


Required software
=========

AML 6.31
Fedem


Required AML modules
=========

aml-analysis-module-pack-type-3-01-06
aml-analysis-module-pack-type-3_ui-01-06
amsketcher-module-04-48
AMOPT-03-00

Installation
=========

To install the AML mechanism system, the files logical.pth and aml-init.tsi
have to be modified, they are placed in the root of the AML isntallation folder,
usually:
    "C:\Program Files\Technosoft\AML\AML6.31.1_x64\"

--
Add the following entries in logical.pth

    :ramms "Path to the folder of the mechanism-system"
    :nastran-data, "Path to wherever the nastran output files is to be stored"
    :AMOpt-files, "Path to wherever the AMOpt output files is to be stored"

e.g.:

    :ramms "C:\AML\NTNU-IPM-KBE-d87408d\"
    :nastran-data "C:\AML\RAMMS\nastran-data\"
    :AMOpt-files "C:\AML\AMOpt\"

--

In aml-init.tsi replace the contents with the following:

  (in-package :tsi)

  (export '(
            right-click-menu-action
            )
          )

  (in-package :aml)

  ;; Loading patches
  (patch-system :aml)


  (load-module "aml-analysis-module-pack-type-3")
  (load-module "amopt")
  (load-module "amsketcher-module")
  (load-module "aml-analysis-module-pack-type-3_ui")

--
Create an environment variable for FEDEM

On windows 10
Right click on the start-menu -> System -> Advanced system settings -> Environment Variables
Under user variables, edit "Path" -> Add "C:\Program Files\Fedem Technology AS\FEDEM-R7\" to the list.

--

Create the folder "analysis" in the temp folder.
    "C:\temp\analysis\"

Note: If the paths from the :tmp and :temp entries in logical.pth does not exist,
      change the paths or create the subsequent folder

--

To start RaMMS do the following:

Compile the system, e.g. write:
    (compile-system :ramms)

Then start RaMMS by running the command:
    (start-ramms)

--

Authors
=======
Anders Kristiansen
Eivind Kristoffersen
Rasmus Korvald Skaare
Thor Christian Coward
