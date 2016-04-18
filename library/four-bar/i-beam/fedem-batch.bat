@ECHO ON
fedem -f model.fmm -solve dynamics 
fedem_graphexp -curvePlotFile deformation.asc -curvePlotType 5 -modelfile model.fmm