build:
	docker-compose pull

up:
	docker-compose up -d grafana

down:
	docker-compose down

start:
	docker-compose start grafana

stop:
	docker-compose stop grafana

restart:
	docker-compose restart grafana

clean:
	docker-compose rm -vs

ldap-reset: ldap-stop ldap-clear ldap-start

ldap-stop:
	docker-compose down

ldap-clear:
	rm -rf ldap slapd.d

ldap-start:
	docker-compose up -d ldap

ldap-query:
	docker-compose exec ldap \
 		ldapsearch -x -w admin \
 			-H ldap://localhost \
 			-b dc=grafana,dc=org -D "cn=admin,dc=grafana,dc=org"

ldap-ssha-password:
	docker-compose exec ldap \
		slappasswd -h {SHA} -s mypassword

ldap-adduser:
	mkdir -p slapd.d/assets/test
	cp ldif/new-user.ldif slapd.d/assets/test
	docker-compose exec ldap \
 		ldapadd -x -w admin \
 			-H ldap://localhost \
 			-D "cn=admin,dc=grafana,dc=org" \
			-f /etc/ldap/slapd.d/assets/test/new-user.ldif

auto: build up ldap-start ldap-query ldap-ssha-password ldap-adduser down

