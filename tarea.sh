#!/bin/bash


echo "Ud ha ingresado las siguientes direcciones $1 y $2"
echo "Evaluando."
for i in 1 2 3
do
 echo "."
 sleep 1
done

if [ -e "$1" ]
 then
  mkdir "$2"
  chmod 777 "$2"
  cp -r "$1/*" "$2"
  cd "$2"
  f=`date +%d-%m-%Y`
  full_path=$2
  file_name="${full_path##*/}"
  name="${file_name%.*}"
  tar cvf "$f$name.tar" "$1"
  echo "Copia Finalizada."
 else
  echo "Ruta de origen no válida"
  echo "Copia no realizada."
fi
