# Run containers
 - docker-compose up
 - Go to http://localhost:8080/main

# Siege
## Install
 - curl -C - -O http://download.joedog.org/siege/siege-latest.tar.gz
 - tar -xvf siege-latest.tar.gz
 - cd siege-2.70/
 - ./configure
 - make
 - make install
 - siege

## Stress testing
 - siege -d1 -c10 -r10 http://localhost:8080/main

# Additional hacks
## select * from
db.collection.find( {} )

## insert
db.collection.insertOne(
   { "item" : "canvas",
     "qty" : 100,
     "tags" : ["cotton"],
     "size" : { "h" : 28, "w" : 35.5, "uom" : "cm" }
   }
)
    
