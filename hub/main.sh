#Reading the username of the first user
read -p "Enter the username for USER1 " usr1

#read -sp"Enter the password for USER1 " pswd1
#echo
#hash1=$(echo "$pswd1" | sha256sum | awk '{print $1}')
#add="false"
found="false"
exp_hash=""
found=$(awk -v usr=$usr1 -f check.awk users.tsv)
#username exists then password validation

if [[ $found == "true" ]]; then
#reading the password for username and also getting expected hash
read -sp"Enter the password for $usr1 " pswd1
echo
hash1=$(echo "$pswd1" | sha256sum | awk '{print $1}')
exp_hash=$(awk -v usr=$usr1 -f pswd.awk users.tsv)
c=0
while [[ $exp_hash != $hash1 ]];do 
#run iff incorrect password entered
((c++))
read -sp"Enter the CORRECT password for $usr1 ($c chance)" pswd1
echo
hash1=$(echo "$pswd1" | sha256sum | awk '{print $1}')
if [[ $c -eq 3 ]]; then 
echo "Seems like you don't remember your password, make a new account"
found="cantremember"
break
fi
done
fi

if [[ $found != "true" ]]; then
#sign up process
if [[ $found == "false" ]]; then 
echo "Username not found."
fi
echo "Initiating sign-up process" 
exists="true"
read -p "Enter the new username " usr1
exists=$(awk -v usr=$usr1 -f check.awk users.tsv)
while [[ $exists == "true" ]];do
read -p "Username already exists, enter new username " usr1
exists=$(awk -v usr=$usr1 -f check.awk users.tsv)
done;
read -sp "Enter the new password " pswd1
echo
hash1=$(echo "$pswd1" | sha256sum | awk '{print $1}')
echo -e "$usr1\t$hash1" >> users.tsv



fi

#everything done for the first user



# Reading the username and passwords of the second user
read -p "Enter the username for USER2 " usr2
# Taking care of the situation in which the second user enters the same password as the first user
while [[ $usr1 == $usr2 ]];
do
echo "ERROR:Second username must be different from the first!"
read -p "Enter the CORRECT username for USER2 " usr2
done

found="false"
exp_hash=""
found=$(awk -v usr=$usr2 -f check.awk users.tsv)
#username exists then password validation
if [[ $found == "true" ]]; then
#reading the password for username and also getting expected hash
read -sp"Enter the password for $usr2 " pswd2
echo
hash2=$(echo "$pswd2" | sha256sum | awk '{print $1}')
exp_hash=$(awk -v usr=$usr2 -f pswd.awk users.tsv)
c=0
while [[ $exp_hash != $hash2 ]];do #run iff incorrect password entered
((c++))
read -sp"Enter the CORRECT password for $usr2 ($c chance)" pswd2
echo
hash2=$(echo "$pswd2" | sha256sum | awk '{print $1}')

if [[ $c -eq 3 ]]; then 
echo "Seems like you don't remember your password, make a new account"
found="cantremember"
break
fi
done
fi
if [[ $found != "true" ]]; then
#sign up process
if [[ $found == "false" ]]; then 
echo "Username not found."
fi
echo "Initiating sign-up process" 
exists="true"
read -p "Enter the new username " usr2
exists=$(awk -v usr=$usr2 -f check.awk users.tsv)
while [[ $exists == "true" ]];do
read -p "Username already exists, enter new username " usr2
exists=$(awk -v usr=$usr2 -f check.awk users.tsv)
done;
read -sp "Enter the new password " pswd2
echo
hash2=$(echo "$pswd2" | sha256sum | awk '{print $1}')
echo -e "$usr2\t$hash2" >> users.tsv


fi

#everything done for the second user


python3 game.py $usr1 $usr2


                
