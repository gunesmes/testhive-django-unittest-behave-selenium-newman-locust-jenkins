#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
	if [[ $line = \#* ]]; then
		echo -e "$line\n"
	else
		docker exec postgres-map psql -U postgres -c "$line"
	fi
done < "restore_database.sql"
