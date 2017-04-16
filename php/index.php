<?php
$path = 'C:\Users';

function getParams() {
	$rawParams = [];
	if(isset($_SERVER['argv'])) {
		$rawParams = $_SERVER['argv'];
		array_shift($rawParams);
	}

	$params = [];
	var_dump($rawParams);
}

getParams();
function getFileList($root, $basePath = '')
{
    $files = [];
    $handle = opendir($root);
    while (($path = readdir($handle)) !== false) {
        if ($path === '.git' || $path === '.svn' || $path === '.' || $path === '..') {
            continue;
        }
        $fullPath = "$root/$path";
        $relativePath = $basePath === '' ? $path : "$basePath/$path";
        if (is_dir($fullPath)) {
            $files = array_merge($files, getFileList($fullPath, $relativePath));
        } else {
            $files[] = $relativePath;
        }
    }
    closedir($handle);
    return $files;
}
var_dump(getFileList($path));
exit();
$handle = opendir($path);
$filename = '';
while ($p = readdir($handle)) {
	if(is_dir($p)) {
		$filename .= $filename.'/'.$p;
	}else {
		echo $filename . '<br/>';
	}
	
}
closedir($handle);
//读取文件
//判断文件类型
//如果是文件则打印出文件名和文件大小
//如果不是是文件夹则记录文件名打开文件