<?php
/**
 * Copyright (c) 2019,2345
 * 摘    要: 自动加载类
 * 作    者: wangb
 * 修改日期: 2019/5/9
 */
namespace Lib;

class Autoloader
{
    protected static $_autoloadRootPath = '';

    /**
     * 功能:
     * 修改日期: 2019/5/9 17:02
     *
     * @param string $root 设置根目录
     * @return void
     */
    public static function setRootPath($root)
    {
        self::$_autoloadRootPath = $root;
    }

    /**
     * 功能:
     * 修改日期: 2019/5/9 17:24
     *
     * @param string $name 类名
     * @return bool
     */
    public static function loadByNameSpace($name)
    {
        $class_path = str_replace('\\', DIRECTORY_SEPARATOR, $name);
        if (strpos($name, 'Lib\\') === 0) {
            $class_file = __DIR__ . substr($class_path, strlen('Lib')) . '.php';
        } else {
            if (self::$_autoloadRootPath) {
                $class_file = self::$_autoloadRootPath . DIRECTORY_SEPARATOR . $class_path . '.php';
            }

            if (empty($class_file) || ! is_file($class_file)) {
                $class_file = __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . "{$class_path}.php";
            }
        }

        if (is_file($class_file)) {
            require $class_file;
            if (class_exists($name, false)) {
                return true;
            }
        }

        return false;
    }
}

spl_autoload_register('\Lib\Autoloader::loadByNameSpace');
