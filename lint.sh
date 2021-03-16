#!/bin/bash -e

li="\033[1;34m↪\033[0m "  # List item
ok="\033[0;32m✔️\033[0m "  # OK

while IFS="" read -r file_path
do
  echo -e "${li:?}${file_path:?}"
  shellcheck --check-sourced --enable=all --severity style -x "${file_path:?}"
done < <(find . -name "*.sh" -not -path "./.venv/*")

echo -e "${li:?}Linting YAML..."
yamllint . --strict

echo -e "${li:?}Sorting Python import definitions..."
if [[ "${CI:=}" == "true" ]]; then
  isort . --check-only --diff
else
  isort .
fi

echo -e "${li:?}Applying opinionated Python code style..."
if [[ "${CI:=}" == "true" ]]; then
  black . --check --diff
else
  black .
fi

echo -e "${li:?}Checking PEP8 compliance..."
flake8 .

echo -e "${li:?}Checking Python types..."
mypy progrow
mypy tests

echo -e "${ok:?}OK!"
