mkdir -p -- "server_persistent_storage" && touch server_persistent_storage/mydata.txt
echo 'Hello. This is Neil Castellino.'>server_persistent_storage/mydata.txt
source calculate_hash.sh server_persistent_storage/mydata.txt
