python3 q2_server.py > out1.txt &
sleep 2
python3 q2_client.py 12 > out2.txt &
sleep 2
DIFF=$(diff out1.txt out2.txt)
var=$(cat out1.txt)
if [ "$DIFF" = "" ] && [[ $var -le 32 ]] && [[ $var -ge 12 ]];
then
    echo "testcase passed"
else
    echo "testcase failed"
fi
rm -f out1.txt
rm -f out2.txt