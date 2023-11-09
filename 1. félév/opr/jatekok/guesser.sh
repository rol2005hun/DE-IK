number=$(( $RANDOM % 100 + 1 ))

echo "Talald ki a szamot! 0 es 100 kozott van"

guess=0
counter=0

while [ "0$guess" -ne $number ] ; do
	read guess
	let "counter+=1"
	[ "0$guess" -lt $number ] && echo "Kicsit feljebb :D"
	[ "0$guess" -gt $number ] && echo "Kicsit lejjebb :D"
done

echo "Kitalaltad $counter lepesbol!"
exit 0
