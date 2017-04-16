<style type="text/css">
	a{
		margin: 5px;
	}
	.active {
		color: red;
	}
	.page {
		background-color: #f0f0f0;
	}
</style>
<?php

class Pagination
{
    private $__total;
    private $__row;
    private $__index;
    private $__count;

    public function __construct($total, $index, $row)
    {
        $this->__total = $total;
        $this->__row   = $row;
        $this->__index = $index;
        $this->__count = $total / $row;
    }

    public function page($index)
    {
        $last = $index - 1 > 0 ? $index - 1 : 1;
        $next = $index + 1 > $this->__count ? $this->__count : $index + 1;

        $__page = '<a href="?p=' . $last . '"> << </a>';
        for ($i = 1; $i <= $this->__count; $i++) {
            $active = $index == $i ? 'active' : '';
            if ($index > 5) {
                if (($i < $index - 5) || ($i > $index + 4)) {
                    continue;
                }
                $__page .= '<a href="?p=' . $i . '" class="page ' . $active . '"> ' . $i . '</a>';
            } else {
                if ($i > 10) {
                    continue;
                }
                $__page .= '<a href="?p=' . $i . '" class="page ' . $active . '"> ' . $i . '</a>';
            }
        }
        $__page .= '<a href="?p=' . $next . '">>></a>';

        return $__page;
    }
}

$p = isset($_GET['p']) ? $_GET['p'] : 1;
$page = new Pagination(1001, $p, 10);
echo $page->page($p);
?>