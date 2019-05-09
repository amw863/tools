<?php
/**
 * Copyright (c) 2019,2345
 * 摘    要:
 * 作    者: wangb
 * 修改日期: 2019/5/9
 */
namespace Lib;

use Medoo\Medoo;

require __DIR__ . DIRECTORY_SEPARATOR . '../vendor/autoload.php';

class Model
{
    private static $instance;

    /**
     * Model constructor.
     */
    private function __construct()
    {
    }

    /**
     * 功能: 实例化DB 并返回
     * 修改日期: 2019/5/9 10:12
     *
     * @return object
     */
    public static function instance()
    {
        if (static::$instance === null) {
            static::$instance = new Medoo([
                'database_type' => 'mysql',
                'database_name' => 'sina_news',
                'charset' => 'utf8',
                'server' => 'localhost',
                'username' => 'root',
                'password' => ''
            ]);
        }

        return static::$instance;
    }

    /**
     * 功能:
     * 修改日期: 2019/5/9 17:44
     *
     * @return null
     */
    private function __clone()
    {
        // TODO: Implement __clone() method.
    }
}
