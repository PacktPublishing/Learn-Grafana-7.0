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

auto: build up-grafana up-prometheus down
