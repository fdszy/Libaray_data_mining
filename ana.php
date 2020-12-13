<?php

header ( "Content-type:text/html;charset=utf-8" );

$name = $_POST['wd'];

echo "$name";

$cmd = exec("python analysis_data.py --userstring $name>error.txt",$ret);
echo "ret is $ret";
echo "数据处理中";
sleep(30);

echo "<script language='javascript' type='text/javascript'>window.location.href='./analysis_data'</script>";

?>