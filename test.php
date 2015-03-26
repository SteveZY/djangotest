<?php
echo hello.'<br />';
for($i=1;$i <=9; $i++){
	echo '<br />';
	for($j=1;$j<=$i;$j++){
		echo $j,'x',$i,'=',$j*$i,'&nbsp;';
	}
}
?>

