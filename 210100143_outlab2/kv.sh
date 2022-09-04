#! /bin/bash

if [ $1 == "storeInfo" ]; then
  echo "$2_$(date '+%d/%m/%y-%T') $3">>store.txt
elif [ $1 == "displayInfo" ]; then
  cat store.txt
elif [ $1 == "getOrderID" ]; then
  order_count=$(grep -c "^$2" store.txt)
  echo "OrderID's found are:"
  grep "^$2" store.txt|grep -oe "[0-9]*$"
  echo "$2 ordered $order_count times"
fi
