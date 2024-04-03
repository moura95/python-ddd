.PHONY: db-up
db-up:
	docker-compose up -d db

.PHONY: db-down
db-down:
	docker-compose down --volumes && docker volume prune -f
	docker-compose up -d db
	rm -rf alembic/versions/*
	sleep 10
	psql "postgresql://postgres:postgres@localhost:5431/driver_vehicles" -f infrastructure/database/modeling/drop.sql
	poetry run alembic revision --autogenerate -m "init"
	poetry run alembic upgrade head
	psql "postgresql://postgres:postgres@localhost:5431/driver_vehicles" -f infrastructure/database/modeling/seed/seed.sql

.PHONY: create-migration
create-migration:
	@read -p "Please, name of migration: " Name; \
	if [ -z "$$Nome" ]; then \
		Nome="migrate"; \
	fi; \
	poetry run alembic revision --autogenerate -m "$$Name"

.PHONY: migrate
migrate:
	poetry run alembic upgrade head

