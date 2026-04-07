file=user.tsv
pref=$1
if [[ $pref = "NONE" ]];then
pref="2"
fi
for game in Othello Tic-Tac-Toe Connect4;do

touch tp.txt
echo "------------------------------"
echo -e "\t$game"
echo "------------------------------"	
echo
if [[ -f $file ]];
then
while read line;do
echo $line > temp.tsv
name=$(cut -f1 -d " " temp.tsv)
win=$(grep -cE "^$name,.*,$game" history.csv)
#win=$(echo "$win*1.0" | bc -l)
lose=$(grep -cE "^.*,$name,.*,$game" history.csv )
if [[ $lose -ne 0 ]];then
ratio=$(echo "scale=2; $win / $lose" | bc -l)
else
ratio=INF
fi

#echo "this is where their supposed to print name"
#echo $ratio
echo -e "$name\t$win\t$lose\t$ratio" >> tp.txt


done < $file
fi
if [[ $pref -eq 1 ]];then

sort -k1 tp.txt -r
elif [[ $pref -eq 2 ]];then
sort -k2 -n tp.txt -r
elif [[ $pref -eq 3 ]];then
sort -k3 -n tp.txt -r
elif [[ $pref -eq 4 ]];then
sort -k4 -n tp.txt -r
fi
rm tp.txt
echo
done

rm temp.tsv
