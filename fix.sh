#!/bin/bash

# Process from the deepest levels up so parent directory 
# names don't change before we process their children.
find . -depth -not -path '*/.*' | while read -r item; do
    # Get the directory and the base name separately
    dir=$(dirname "$item")
    base=$(basename "$item")

    # 1. Convert to lowercase
    # 2. Replace spaces, dashes, dots, and parens with underscores
    # 3. Replace any non-alphanumeric (except /) with underscores
    # 4. Squeeze multiple underscores into one
    # 5. Remove trailing underscores
    new_base=$(echo "$base" | tr '[:upper:]' '[:lower:]' | \
               sed -e 's/[[:space:]-]/_/g' \
                   -e 's/[^a-z0-9._]/_/g' \
                   -e 's/_\+/_/g' \
                   -e 's/_$//g')

    # Only rename if the name actually changed
    if [ "$base" != "$new_base" ]; then
        new_path="$dir/$new_base"
        if [ -e "$new_path" ]; then
            echo "SKIPPING: $new_path already exists"
        else
            echo "RENAMING: $item -> $new_path"
            mv "$item" "$new_path"
        fi
    fi
done
