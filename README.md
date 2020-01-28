## Cisco Live Europe 2020

The goal of this script is to download all cisco live presentations without clicking everywhere.

## You might have to install couple of extra modules if it's not the case yet

        # python -m pip install --upgrade pip & python -m pip install requests

## To run the script
        
        # python3 getPresentionsCLEUR.py

## DOCKER Commands

Buil the container and copy the script to /app

        # docker build --tag cleur-presentations .

Run the container and create directory /app/pdfs with all presentation from cisco live europe 

        # docker run --name cleur-presentations my-cleur-presentations

Once all presentations downloaderd copy the the /app/pdfs directory from container to local drive.

        # docker cp $(docker ps -q --filter "ancestor=my-cleur-presentations"):/apps/pdf pdf-from-docker
        