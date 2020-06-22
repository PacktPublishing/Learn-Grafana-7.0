IMAGE=sensors
INDEX=cpu_metrics

build:
	docker-compose pull

up:
	docker-compose up -d

down:
	docker-compose down

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose restart

clean:
	docker-compose rm -vs

up-logstash:
	docker-compose up -d logstash

up-elasticsearch:
	docker-compose up -d elasticsearch

es-describe:
	curl -XGET localhost:9200/$(INDEX)/_mapping?pretty

es-query:
	curl -XGET http://localhost:9200/$(INDEX)/_search?pretty

es-clean:
	curl -X DELETE "localhost:9200/$(INDEX)?pretty"

run-powermetrics:
	sudo powermetrics -i 60000 --format plist --samplers smc -u data/sample.plist

auto1: build up down
auto2: run-powermetrics