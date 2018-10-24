package lists

import (
	"datastruct/containers"
	"datastruct/utils"
)

type List interface {
	Get(index int) (interface{}, bool)
	Remove(index int)
	Add(values ...interface{})
	contains(values ...interface{})bool
	Sort(comparator utils.Comparator)
	Swap(index1, index2 int)
	Insert(index int, values ...interface{})
	Set(index int, value interface{})

	containers.Container
}