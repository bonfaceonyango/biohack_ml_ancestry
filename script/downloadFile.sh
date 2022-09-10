for i in `cat file`;
do
wget -c $i
echo "done"
done