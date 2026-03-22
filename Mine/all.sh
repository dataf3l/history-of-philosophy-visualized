#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "--- Starting Philosophy Data Pipeline ---"

# 1. Extract the initial list
echo "[1/4] Extracting philosopher list..."
python get_philosopher_list_from_json.py

# 2. Get the references and claims
echo "[2/4] Parsing references and claims..."
python get_references_and_claims_list_from_json.py

# 3. Generate the TSV with names
echo "[3/4] Formatting claims TSV..."
python get_claims_plus_philosoper_name_tsv.py

# 4. Final refcount analysis
echo "[4/4] Calculating reference counts..."
python get_refcounts.py

echo "--- Pipeline Complete ---"