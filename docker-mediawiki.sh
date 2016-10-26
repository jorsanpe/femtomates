#!/bin/bash

docker network inspect docker-mediawiki > /dev/null
if [ $? -ne 0 ]; then
  echo "error: docker-mediawiki network does not exist"
  echo "create it using 'docker network create docker-mediawiki"
  exit 1
fi

echo "Starting mysql docker container..."
docker run \
  --name mysql \
  --net docker-mediawiki \
  -e MYSQL_ROOT_PASSWORD=secure \
  -e MYSQL_USER=mediawiki \
  -e MYSQL_PASSWORD=secure \
  -v $(pwd)/mysql:/var/lib/mysql \
  -d mysql

sleep 3 

echo "Starting mediawiki docker container..."
docker run \
  --name mediawiki \
  --net docker-mediawiki \
  -p 8080:80 \
  -e MEDIAWIKI_DB_HOST=mysql:3306 \
  -e MEDIAWIKI_DB_USER=root \
  -e MEDIAWIKI_DB_PASSWORD=secure \
  -v $(pwd)/mediawiki:/var/www/html \
  synctree/mediawiki
