##########################################################
# DEV : SHA4T0
# Facebook : https://www.facebook.com/SHA4TO
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,

# THANKS TO ALLAH
# WELCOME HOME
# 
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################



a='\033[1;30m'
rc='\033[1;31m'
g='\033[1;32m' 
y='\033[1;33m'
b='\033[1;34m'
p='\033[1;35m'
c='\033[1;36m' 
w='\033[1;37m'
m='\033[1;94m'
n='\033[0;00m' 

update(){
  echo -e "${p} A UPDATE AVAILABLE"
  sleep 0.1
  echo -e "${m} MMAIL IS UPDATING"
  sleep 1
  xdg-open https://www.facebook.com/SHA4TO
  echo -e "${b} PLEASE WAIT..." 
  cd ; 
  rm -rf mmail ; 
  apt update ; 
  apt install python3 -y ; 
  apt install git -y ; 
  pip install requests ; 
  git clone https://github.com/SHA4T0/mmail
  


  echo
  echo -e "${g} NOW YOUR TOOL UPDATED."
  echo
  echo -e "${y} THANKS FOR UPDATE ME."
  echo
  echo -e "${g}<==> NOW TYPE <==>"
  echo
  echo -e "${b} cd ; cd mmail ; python mmail.py${n}" ;
  sleep 3


}
update
echo 
echo
exit





##########################################################
# DEV : SHA4T0
# Github : https://github.com/SHA4T0
# IF YOU WANNA TAKE CREADITS FOR THIS TOOL,,,LOOK YOUR SELF AGAIN AND AGAIN,,
# THANKS TO ALLAH
# WELCOME HOME
# SHA4T0
#####################৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳৳################
