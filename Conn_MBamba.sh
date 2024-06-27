#!/bin/bash

Admin="M.BAMBA MAMADOU"
code="CISCO@@"



read -s -p "Entrez le code secret pour $Admin : " code_entre


if [ "$code_entre" = "$code" ]; then
    echo "Connexion réussie $Admin"

else
    echo "Le code saisi est incorrect."
fi