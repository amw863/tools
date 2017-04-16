<?php
require_once './pagination.php';
Pagination::$index = isset($_REQUEST['cd']) ? $_REQUEST['cd'] : 1;
Pagination::$row   = 10;
Pagination::$total = 10001;

echo Pagination::page();
?>