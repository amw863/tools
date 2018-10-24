package containers

type IteratorWithIndex interface {
	Next() bool
	Value() interface{}
	Index() int
	Begin() ()
	First() bool
}

type IteratorWithKey interface {
	Next() bool
	Value() interface{}
	Key() int
	Begin() ()
	First() bool
}

type ReverseIteratorWithIndex interface {
	Prev() bool
	End()
	Last() bool
	IteratorWithIndex
}

type ReverseIteratorWithKey interface {
	Prev() bool
	End()
	Last() bool
	IteratorWithKey
}