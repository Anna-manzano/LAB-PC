#!/bin/bash
$(./scriptconerror.sh)> /dev/null 2>&1
if [ $(echo &?) !="0"]; then
	python email.py -to &1 -subj "Error en el script" -msj "Sea a detectado un error en el ultimo script ejecutado"
fi