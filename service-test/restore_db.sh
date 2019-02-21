#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
	if [[ $line = \#* ]]; then
		echo -e "$line\n"
	else
		docker exec testhive-postgres psql -U postgres -c "$line"
	fi
done < "restore_database.sql"
