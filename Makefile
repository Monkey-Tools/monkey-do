requirements:
	pipenv lock -r > requirements.txt

docker: requirements
	@docker build ./
