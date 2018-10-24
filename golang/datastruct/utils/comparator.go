package utils

import "time"

type Comparator func (a, b interface{}) int

//确定比较的最小范围
//逐个比较字符大小
//当出现第一个不相等时则得出比较结果
//对于最小范围内都相等的，则看那个字符串的长度比较长
//对于比较长的字符串
//其值比较大
func StringComparator(a, b interface{}) int  {
	s1 := a.(string)
	s2 := b.(string)

	min := len(s2)
	if len(s1) < len(s2) {
		min = len(s1)
	}

	diff := 0
	for i := 0; i < min && diff ==0;i++ {
		diff = int(s1[i]) - int(s2[i])
	}

	if diff==0 {
		diff = len(s1) - len(s2)
	}

	if diff<0 {
		return -1
	}

	if diff >0 {
		return  1
	}

	return 0
}

func IntComparator(a, b interface{}) int  {
	aAssert := a.(int)
	bAssert := b.(int)

	switch  {
	case aAssert > bAssert:
		return 1
	case aAssert < bAssert:
		 return  -1
	default:
		return 0
	}
}

func Int8Comparator(a, b interface{}) int  {
	aAssert := a.(int8)
	bAssert := b.(int8)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Int16Comparator(a, b interface{}) int  {
	aAssert := a.(int16)
	bAssert := b.(int16)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}

}

func Int32Comparator(a, b  interface{}) int {
	aAssert := a.(int32)
	bAssert := b.(int32)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Int64Comparator(a, b interface{}) int  {
	aAssert := a.(int64)
	bAssert := b.(int64)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Uint8Comparator(a, b interface{}) int  {
	aAssert := a.(uint8)
	bAssert := b.(uint8)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Uint16Comparator(a, b interface{}) int {
	aAssert := a.(uint16)
	bAssert := b.(uint16)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Uint32Comparator(a, b interface{}) int {
	aAssert := a.(uint32)
	bAssert := b.(uint32)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func  Uint64Comparator(a, b interface{}) int  {
	aAssert := a.(uint64)
	bAssert := b.(uint64)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Float32Comparator(a, b interface{}) int {
	aAssert := a.(float32)
	bAssert := b.(float32)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func Float64Comparator(a, b interface{}) int {
	aAssert := a.(float64)
	bAssert := b.(float64)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func ByteComparator(a, b interface{}) int {
	aAssert := a.(byte)
	bAssert := b.(byte)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func RuneComparator(a, b interface{}) int {
	aAssert := a.(rune)
	bAssert := b.(rune)

	switch  {
	case aAssert > bAssert:
		return  1
	case aAssert < bAssert:
		return -1
	default:
		return 0
	}
}

func  TimeComparator(a, b interface{})int  {
	aAssert := a.(time.Time)
	bAssert := b.(time.Time)

	switch  {
	case aAssert.After(bAssert):
		return 1
	case aAssert.Before(bAssert):
		return -1
	default:
		return 0
	}
}