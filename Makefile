.PHONY: lint format test

lint:
	pylint src/ tests/

format:
	black src/ tests/

test:
	pytest
