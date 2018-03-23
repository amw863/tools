###PHP PSR

[PSR-[0-4]](https://www.kancloud.cn/thinkphp/php-fig-psr/3141)
### 导读
Proposing a Standards Recommendation (PSR)是由PHP互操作性框架制定小组(PHP-FIG:PHP Framework Interoperability) 制定的PHP编码规范.

目前官方已经制定的方案包括以下六份文件:
- PSR-0(已废弃)
- PSR-1
- PSR-2
- PSR-3
- PSR-4
### PSR-1 基本代码规范
本篇规范制定了代码基本元素的相关标准,以确保共享的PHP代码间给予较高 的技术互通性.

#### 1.概览
---
- PHP代码文件必须以```<?php```或```<?=```标签开始;
- PHP代码必须以不带```BOM```的```UTF-8```编码;
- PHP代码中应该只定义类、函数、常量等声明,或其他会产生```从属效应``` 的操作(如:生产文件输出以及修改```.ini```配置文件等),二者只能选其一;
- 命名空间以及类必须符合PSR的自动加载规范:PSR-0或PSR-4中的一个;
- 类的名称必须遵循```StudlyCaps```大写开头的驼峰命名规则;
- 类中的常量所有字母都必须大写，单词间用下划线分割;
- 方法名称必须符合```camleCase```式的小写开头的驼峰命名规则.

#### 2 文件
---
##### 2.1 PHP标签
PHP代码必须使用```<?php ?>```长标签或者```<?= ?>``` 短标签输出；一定不可以使用其他自定义标签.
##### 2.2字符编码
PHP代码``必须且只可```使用```不带BOM```的```UTF-8编码```.
##### 2.3从属效应(副作用)
一份PHP文件应该要不就只定义新的声明，入类，函数或常量等不产生从属效应的操作,要不就只有会产生从属效应的逻辑操作，但不应该同事具有两者.

"从属效应"(side effects) 一词的意思是，仅仅通过包含文件，不直接声明类，函数和常量，而执行的逻辑操作。

“从属效应”包含却不仅限于：生产输出,直接的```require```或```include```，链接外部服务,修改ini配置、抛出错误或者异常、修改全局或静态变量、读写文件等。

以下是一个反例，一份包含声明的以及产生从属效应的代码。
```
<?php
//从属效应:修改ini配置
ini_set('error_reporting', E_ALL);

//从属效应:引入文件
include "file.php";

//从属效应:生产输出
echo "<html>\n";

//函数声明
function foo () {
    //函数主题部分
}
```

以下是一个范例，一份只包含声明不产生从属效应的代码:
```
//函数声明
function foo () {
    //函数主题部分
}

//条件声明** 不**属于从属效应
if (!function_exists('bar') {
    function bar () {
        //函数主题部分
    }
}

```

#### 3 命名空间和类
---
命名空间以及类的命名必须遵守PSR-0.

根据规范，每个类都独立为一个文件，且命名空间至少有一个层次:顶级组织名称(Vendor name).

类的名称必须遵守```StudlyCaps```大写开头的驼峰命名规范.

PHP 5.3以及以后的代码必须使用正式的命名空间.
如：
```
<?php

namespace Vendor\Model;

class Foo
{
    
}
```
#### 4.类的产量、属性和方法
---
##### 4.1常量
类的常量中所有的字母都必须大写，词间以下划线分割。
```
<?php
namespace Vendor\Model;

class Foo
{
    const VERSION = '1.0';
    const DATE_APPROVED = '2012-06-01';
}
```

##### 4.2属性
类的属性命名可以遵循大写开头的驼峰式、小写开头的驼峰式或下划线分割式($under_sorce)。本规范不做强制要求，但是无论遵循那种命名方式，都应该在一定的范围内保持一致。这个范围可以是整个团队、整个包、整个类或者整个方法。
##### 4.3方法
方法名必须符合```camlCase()```式的小写开头的驼峰命名规范.

本篇式PSR-1基本代码规范的继承和扩展.

本规范希望通过制定一些列的规范化PHP代码规则，以减少在浏览不同作者代码时，因代码风格不同造成的不便。

## 1.概览
- 代码必须遵守PSR-1中的编码规范.
- 代码必须使用4个空格符而不是tab键进行缩进.
- 每行的字符数应该保持在80个之内,理论上不可以多余120个，但一个不能有硬性的限制.
- 每个namespace命名空间声明预计和use声明语句块后面，必须插入一行空白.
- 类的开始花括号({})必须写在函数声明后自成一行，结束花括号也必须写在函数主题后自成一行.
- 方法的开始花括号必须写在函数声明后自成一行，结束花括号也必须写在函数主题后自成一行。
- 类的属性和方法添加方位修饰符(private,protected, public),abstract以及final必须声明在访问修饰符之前，而static必须在访问修饰符之后.
- 控制结构的开始花括号必须写在声明的同一行，而结束花括号必须写在主题后自成一行。
- 控制结构的开始括号和结束括号前，都一定不能有空格。
#### 1.1 实例
以下实例简单的展示了以上的大部分规范:
```
<?php
namesapce  Vendor\Package;

use FooInterface;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class Foo extends Bar implements FooInterface
{
    public function sampleFunction($a, $b = null) {
        if ($a === $b) {
            bar();
        } elseif ($a > $b) {
            $foo->bar($arg1);
        } else {
            BazClass::bar($agr2, $arg3);
        }
    }
    
    final public static function bar () {
        //
    }
}
```

## 2.通则
### 2.1 基本编码准则
必须符合PSR-1中的所有规范.
### 2.2 文件
所有PHP文件必须使用Unix LF(linefeed) 作为行的结束符.

所有PHP文件必须以一个空白行结束.

纯PHP代码文件必须省略```?>```结束标签.

### 2.3 行

行的长度一定不能有硬性的约束.

软性的长度约束一定要限制在120个字符以内。若超过此长度，代码规范检查的编辑器要发出警告.

每行不应该多余80个字符，大于80个字符的行，应该折成多行。

非空行后一定不能有多余的空格符号。

空行可以使得代码更加方便以及有助于代码的分块。

每行一定不能存在多于一条语句。

### 2.4缩进
代码必须使用4个空格符而不是tab键进行缩进.
        
        备注：使用空格而不是tab的好处在于，避免比较代码差异，打补丁，重阅以及注释时产生混淆。并且，使用空格缩进使得对其变得方便。
#### 2.5 关键字 以及 true/false/null

PHP所有关键字都必须小写，包括以上。

### 3 namespace以及use声明
namespace 声明后必须插入一个空白行。
所有use必须在namspace 后声明.
每条use 声明语句后必须只有一个use关键字。
use 声明语句块后必须有一个空白行。
```
<?php
namesapce  Vendor\Package;

use FooInterface;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;



```
### 4.类、属性和方法
----
此处的类泛指class类、接口以及rtait可服用代码块。
#### 4.1扩展和继承
关键词extends 和implements必须写在类名的同一行。

类的开始花括号必须单独占一行，结束花括号也必须在类主题后独占一行。
```
<?php
namesapce  Vendor\Package;

use FooInterface;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;


class ClassName extends ParentClass implements \ArrayAccess, \Countable
{
    //constants, properties, methods
}
```

implements 也可以分成多列，这样的话，每个继承接口名称都必须分开独立成行，包括第一个。
```
<?php
namesapce  Vendor\Package;

use FooInterface;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;


class ClassName extends ParentClass implements \ArrayAccess,
\Countable,
\Serializable
{
    //constants, properties, methods
}
```

#### 4.2属性
每个属性都必须加访问修饰符。

一定不可以使用关键字var 声明一个属性。

每条语句一定不可定义超过一个属性。


不要使用下划线作为前缀，来区分属性是protected或private。

```
<?php
namespace Vendor\Package;

class ClassName
{
    public $foo = null;
}
```

#### 4.3方法

所有的方法都要添加访问修饰符。

不要使用下划线作为前缀，来区分方法是private或protected.

方法名称后面一定不要有空格，其开始花括号必须独占一行。结束花括号也必须在方法主体后独占一行。参数左括号和右括前一定不能有空格。

```
<?php

namspace Vendor\Package;
class ClassName
{
    public function fooBarBaz($arg1, &$arg2, $arg3 = [])
    {
        //method body
    }
}
```

#### 4.4 方法的参数

参数列表中，每个参数后面必须要有一个空格，而前面一定不能有空格。

有默认参数，必须放到参数列表的末尾。


参数列表可以分成多行，这样，包括第一个参数在内的每个参数都必须单独成行。

拆分成多行的参数列表后，结束括号以及方法开始花括号必须写在同一行，中间用一个空格分割。

#### 4.5 abstract,final以及static

需要添加

报表合并

本文制定了日志类库的通用接口规范。

本规范的主要目的，是为了让日志类库以简单通用的方式，通过接收一个 ```Psr\Log\LoggerInterface```对象，来记录日志信息。 框架以及CMS内容管理系统如有需要，可以对此接口进行扩展，但需遵循本规范， 这才能保证在使用第三方的类库文件时，日志接口仍能正常对接。

本文中的```实现者```指的是实现了 ```LoggerInterface``` 接口的类库或者框架，反过来讲，他们就是 ```LoggerInterface``` 的 ```使用者```。
## 1.规范说明
### 1.1基本规范
- LoggerInterface接口对外定义了八个方法，分别用来记录RFC5424中定义的八个等级的日志:debug,info,notice,warning,error,critical,alert以及emergency。
- 第九个方法```log```,其第一个参数为记录的等级。可以使用一个预先定义的的等级常量作为参数来调用此方法，必须与直接调用以上八个方法具有相同的效果。如果传入的等级常量参数没有预先定义，则必须抛出```Psr\Log\InvalidArgumentException```类型的异常。在不确定的情况下，使用者不该使用为支持的等级常量来调用此方法。

### 1.2记录信息
- 以上每个方法都接受一个字符串类型或者是由```__toString()```方法的对象作为记录信息参数，这样，实现者就能把它当成字符串来处理，否则实现者必须自己把它转化成字符串。
- 记录信息参数可以携带占位符，实现者可以根据上下文将其替换成相应的值。

其中占位符必须与上下文数组中的键名保持一致。

占位符的名称必须由一个左花括号 { 以及一个右括号 } 包含。但花括号与名称之间一定不能有空格符。

占位符的名称应该只由 A-Z、 a-z,0-9、下划线 _、以及英文的句号 .组成，其它字符作为将来占位符规范的保留。

实现者可以通过对占位符采用不同的转义和转换策略，来生成最终的日志。 而使用者在不知道上下文的前提下，不该提前转义占位符。
```
/** * 用上下文信息替换记录信息中的占位符 */

function interpolate($message, array $context = array())
{
        // 构建一个花括号包含的键名的替换数组
    $replace = array();
    foreach ($context as $key => $val) {
        $replace['{'.$key.'}'] = $val;
    }
    
    return strtr($message, $replace);
}

$message = "User {username} created";

$context = array('username' => 'bolivar');

echo interpolate($message, $context);
```
### 1.3上下文
- 每个记录函数都接受一个上下文数组参数，用来装载字符串类型无法表示的信息。它可以装载任何信息，所以实现者必须确保能正确处理其装载的信息，对于其装载的数据，一定不能 抛出异常，或产生PHP出错、警告或提醒信息（error、warning、notice）。
- 如需通过上下文参数传入了一个 Exception 对象， 必须以 'exception' 作为键名。 记录异常信息是很普遍的，所以如果它能够在记录类库的底层实现，就能够让实现者从异常信息中抽丝剥茧。 当然，实现者在使用它时，必须确保键名为 'exception' 的键值是否真的是一个 Exception，毕竟它可以装载任何信息。

### 1.4 助手类和接口
- ```Psr\Log\AbstactLogger```类使得只需继承它和实现其中的 log 方法，就能够很轻易地实现 LoggerInterface 接口，而另外八个方法就能够把记录信息和上下文信息传给它。
- 同样地，使用```Psr\Log\LoggerTrait```也只需实现其中的 log 方法。不过，需要特别注意的是，在traits可复用代码块还不能实现接口前，还需要 implement LoggerInterface。
- 在没有可用的日志记录器时， ```Psr\Log\NullLogger``` 接口可以为使用者提供一个备用的日志“黑洞”。不过，当上下文的构建非常消耗资源时，带条件检查的日志记录或许是更好的办法.
- ```Psr\Log\LoggerAwareInterface  ```接口仅包括一个 ```setLogger(LoggerInterface $logger)``` 方法，框架可以使用它实现自动连接任意的日志记录实例。
- ```Psr\Log\LoggerAwareTrait```trait可复用代码块可以在任何的类里面使用，只需通过它提供的 ```$this->logger```，就可以轻松地实现等同的接口。
- ```Psr\Log\LogLevel```类装载了八个记录等级常量。
- 包。
- 上述的接口、类和相关的异常类，以及一系列的实现检测文件，都包含在 psr/log 文件包中。
## 2. Psr\Log\LoggerInterface
```
<?php
namespace Psr\Log;
/**
 * 日志记录实例 
 * 日志信息变量 —— message， **必须**是一个字符串或是实现了 __toString() 方法的对象。
 *  日志信息变量中**可以**包含格式如 “{foo}” (代表foo) 的占位符， * 它将会由上下文数组中键名为 "foo" 的键值替代。 
 * 上下文数组可以携带任意的数据，唯一的限制是，当它携带的是一个 exception 对象时，它的键名 必须 是 "exception"。
 * * 详情可参阅： https://github.com/PizzaLiu/PHP-FIG/blob/master/PSR-3-logger-interface-cn.md
 */
interface LoggerInterface
{
	//系统不可用
	public function emergency ($message, array $context = array());
	//必须**立刻采取行动 * * 例如：在整个网站都垮掉了、数据库不可用了或者其他的情况下，**应该**发送一条警报短信把你叫醒。
	public function alert ($message, array $context = array());
	//紧急情况 * * 例如：程序组件不可用或者出现非预期的异常。
	public function critical ($message, array $context = array());
	//运行时出现的错误，不需要立刻采取行动，但必须记录下来以备检测。
	public function error ($message, array $context = array());
	//出现非错误性的异常。 * * 例如：使用了被弃用的API、错误地使用了API或者非预想的不必要错误。
	public function warning ($message, array $context = array());
	//一般性重要的事件。 
	public function notice ($message, array $context = array());
	//重要事件 * * 例如：用户登录和SQL记录。
	public function info ($message, array $context = array());
	// debug 详情 
	public function debug ($message, array $context = array());
	//任意等级的日志记录
	public function log ($level, $message, array $context = array());
}

```

## 4.Psr\Log\LoggerAwareInterface

```
<?php

namspace Psr\Log;

interface LoggerAwareInterface
{
    //设置一个日志记录实例
    public function setLogger(LoggerInterface $logger);
}
```

## 5.Psr\Log\LogLevel
```
<?php
namspace Psr\Log;

class LogLevel
{
    const EMERGENCY = 'emergency';
    const ALET = 'alert';
    const CRITICAL = 'critical';
    const ERROR = 'error';
    const WARNING = 'warning';
    const NOTICE = 'notice';
    const INFO = 'info';
    const DEBUG = 'debug';
}

```
# 1.概述
本 PSR 是关于由文件路径 [自动载入](http://tools.ietf.org/html/rfc2119) 对应类的相关规范， 本规范是可互操作的，可以作为任一自动载入规范的补充，其中包括 PSR-0，此外， 本 PSR 还包括自动载入的类对应的文件存放路径规范。
# 2.详细说明
1. 此处的“类”泛指所有的class类、接口、traits可复用代码块以及其它类似结构。
2. 一个完整的类名需具有以下结构:
```
\<命名空间>(\<子命名空间>)*\<类名>
```
    1.完整的类名必须要有一个顶级命名空间，被称为 "vendor namespace"
    2.完整的类名可以有一个或多个子命名空间；
    3.完整的类名必须有一个最终的类名；
    4.完整的类名中任意一部分中的下滑线都是没有特殊含义的；
    5.完整的类名可以由任意大小写字母组成；
    6.所有类名都必须是大小写敏感的。
    7.当根据完整的类名载入相应的文件……
    8.完整的类名中，去掉最前面的命名空间分隔符，前面连续的一个或多个命名空间和子命名空间，作为“命名空间前缀”，其必须与至少一个“文件基目录”相对应；
    9.紧接命名空间前缀后的子命名空间必须与相应的”文件基目录“相匹配，其中的命名空间分隔符将作为目录分隔符。
    10.末尾的类名必须与对应的以 .php 为后缀的文件同名。
    11.自动加载器（autoloader）的实现一定不能抛出异常、一定不能触发任一级别的错误信息以及不应该有返回值。
    
# 3.例子
下表展示了符合规范完整类名、命名空间前缀和文件基目录所对应的文件路径。

完整类名 | 命名空间前缀 | 文件基目录|文件路径
---|---|--|--|--

\Acme\Log\Writer\File_Writer | Acme\Log\Writer|./acme-log-writer/lib/|./acme-log-writer/lib/File_Writer.php
\Aura\Web\Response\Status|Aura\Web|/path/to/aura-web/src/|/path/to/aura-web/src/Response/Status.p
\Symfony\Core\Request|Symfony\Core|./vendor/Symfony/Core/|	./vendor/Symfony/Core/Request.ph
\Zend\Acl|Zend|/usr/includes/Zend/|	/usr/includes/Zend/Acl.php

关于本规范的实现，可参阅 [相关实例](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader-examples.md)
注意：实例并不属于规范的一部分，且随时会有所变动
