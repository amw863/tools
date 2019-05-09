- 实现按照 namespace 自动加载
- 封装了传参 和 json 输出
- 实现了 Medoo 简单集成


开箱即用:

```
<?php
/**
 * Copyright (c) 2019,2345
 * 摘    要: 首页类
 * 作    者: wangb
 * 修改日期: 2019/5/9
 */

require_once 'Lib/Autoloader.php';

use Lib\Input;
use Lib\Output;

class Index
{
    const DEV = 'development';

    public $flag;

    /**
     * 功能:
     * 修改日期: 2019/5/9 10:48
     *
     * @param array $args 参数
     * @return bool
     */
    public function run($args = [])
    {
        $act = Input::get('act');


        Output::json(Output::JSON_SUCC, 'ok', $act);
    }
}

$instance = new Index();
$instance->run();

```
