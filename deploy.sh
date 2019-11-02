docker image rm poi_api
docker image rm eu.gcr.io/engservicos2019/poi_api
docker build -t poi_api .
docker tag poi_api eu.gcr.io/engservicos2019/poi_api:latest
docker push eu.gcr.io/engservicos2019/poi_api:latest