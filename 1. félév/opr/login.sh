usrnm=$(who am i | awk '{print $1}')
printf "Welcome back, $usrnm, the date is: $(date "+%D %r")\n-> Online with you also: "
current_user=$(whoami)
online_users=$(who | awk -v user="$current_user" '$1 != user {print $1}' | paste -sd ", ")
echo $online_users
printf "Wolimby API:\n"
if ping -c 1 account.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Account online
else
    echo - Account offline
fi
if ping -c 1 account.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Account API online
else
    echo - Account API offline
fi
if ping -c 1 social.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Social online
else
    echo - Social offline
fi
if ping -c 1 account.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Social API online
else
    echo - Social API offline
fi
if ping -c 1 shortify.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Shortify online
else
    echo - Shortify offline
fi
if ping -c 1 account.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Shortify API online
else
    echo - Shortify API offline
fi
if ping -c 1 games.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Games online
else
    echo - Games offline
fi
if ping -c 1 account.wolimby.hu | grep -q " 0% packet loss"; then
    echo - Games API online
else
    echo - Games API offline
fi

cat << "EOF"

            _ ___   ___   ___  _____ _                 _          _____       _     _             
           | |__ \ / _ \ / _ \| ____| |               ( )        |  __ \     | |   (_)            
  _ __ ___ | |  ) | | | | | | | |__ | |__  _   _ _ __ |/ ___     | |  | | ___| |__  _  __ _ _ __  
 | '__/ _ \| | / /| | | | | | |___ \| '_ \| | | | '_ \  / __|    | |  | |/ _ \ '_ \| |/ _` | '_ \ 
 | | | (_) | |/ /_| |_| | |_| |___) | | | | |_| | | | | \__ \    | |__| |  __/ |_) | | (_| | | | |
 |_|  \___/|_|____|\___/ \___/|____/|_| |_|\__,_|_| |_| |___/    |_____/ \___|_.__/|_|\__,_|_| |_|
                                                                                                  
                                                                                                  
EOF
