package containers

type JSONSerializer interface {
	ToJson() ([]byte, error)
}

type JSONDeserializer interface {
	FromJson([]byte) error
}
