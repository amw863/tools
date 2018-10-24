package utils

import "sort"

type sortable struct {
	value []interface{}
	comparator Comparator
}

func (s sortable)Len() int {
	return  len(s.value)
}

func (s sortable)Swap(i, j int) {
	s.value[i], s.value[j] = s.value[j], s.value[i]
}

func (s sortable) Less(i, j int) bool  {
	return s.comparator(s.value[i], s.value[j])  < 0
}

func Sort(values []interface{}, comparator Comparator)  {
	sort.Sort(sortable{values, comparator})
}