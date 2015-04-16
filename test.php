<?php
error_reporting(E_ALL);
echo 'hello'.'<br />';
for($i=1;$i <=9; $i++){
	echo '<br />';
	for($j=1;$j<=$i;$j++){
		echo $j,'x',$i,'=',$j*$i,'&nbsp;';
	}
}

$a=123;
$b=$c+1;
echo '<br />';
$arr=array('key1'=>'name','key2'=>'sex','gender');
print_r($arr);

$yang = array(1,0,0,0);
for($i=1;$i<=20;$i++){
	array_unshift($yang,0);
	array_pop($yang);
	$yang[0] = $yang[1] + $yang[3];
	echo '<br />';
	print_r($yang);
}
$str1 = '1234567';
$num = 123456789;

echo '<br />';
print_r($str1[4]);
#$str1[]=',';
echo number_format($num,0);
print_r('   '.$str1);
?>

