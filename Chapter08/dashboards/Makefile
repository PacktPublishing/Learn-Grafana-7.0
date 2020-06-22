SMALL=100
MEDIUM=1000
LARGE=10000

DATADIR=data
CSVFILE=$(DATADIR)/Current_FY_Cases.csv
INDEX=data-index

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

build-%:
	docker-compose pull $*

up-%:
	docker-compose up -d $*

start-%:
	docker-compose start $*

stop-%:
	docker-compose stop $*

$(CSVFILE):
	gunzip $(CSVFILE).gz

es-load-small: es-clean
	head -$(SMALL) $(CSVFILE) | docker-compose run logstash logstash

es-load-medium: es-clean
	head -$(MEDIUM) $(CSVFILE) | docker-compose run logstash logstash

es-load-large: es-clean
	head -$(LARGE) $(CSVFILE) | docker-compose run logstash logstash

es-load-all: es-clean
	docker-compose run logstash logstash < $(CSVFILE)

es-describe:
	curl -XGET localhost:9200/$(INDEX)/_mapping?pretty

es-query:
	curl -XGET http://localhost:9200/$(INDEX)/_search?pretty

es-clean:
	curl -X DELETE "localhost:9200/$(INDEX)?pretty"

auto: build up-grafana up-elasticsearch $(CSVFILE) es-load-all down
