PYTHON ?= python3

.PHONY: help validate validate-quick pycheck lint test tree

help:
	@printf "Targets:\n"
	@printf "  make validate        Run full repository validation\n"
	@printf "  make validate-quick  Run quick repository validation\n"
	@printf "  make pycheck         Python syntax checks across labs/tests\n"
	@printf "  make lint            Shell + Python syntax + repo validation prep checks\n"
	@printf "  make test            Run pytest suite (requires dependencies)\n"
	@printf "  make tree            Print directory tree (fallback if tree missing)\n"

validate:
	./validate_repo.sh

validate-quick:
	./validate_repo.sh --quick

pycheck:
	find labs tests capstone -type f -name '*.py' -exec $(PYTHON) -m py_compile {} \;

lint:
	bash -n validate_repo.sh
	find tools labs -type f -name '*.sh' -exec bash -n {} \;
	$(MAKE) pycheck

test:
	pytest -q tests

tree:
	@if command -v tree >/dev/null 2>&1; then tree -a -I '.git|.venv'; else find . -path './.git' -prune -o -path './.venv' -prune -o -print | sort; fi
