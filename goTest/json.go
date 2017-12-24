package main

import (
	"fmt"
	"unsafe"
	"github.com/go-macaron/macaron"
	"net/http"
	"os"
//	"strings"
//	"encoding/json"
)




type ss struct {
	a int
	b string
	c float64
}

func main() {
	//var s string
	//var i int
	var b ss
	var a, bb, cc string = "1111111111111111111111", "222", "333"
	//fmt.Print(s=="")
	//fmt.Print(&i)
	//fmt.Print(&s)
	fmt.Print(unsafe.Sizeof(b))
	fmt.Print(&b)
	fmt.Print(a)
	fmt.Print(bb)
	fmt.Print(cc)
	fmt.Print(b.b=="")
	testCoxType()
	testMap()
	testLog()

	//
	var iiii int = 11
	testInj(func(i int){
		fmt.Println(i)
		fmt.Println("I am called!!------")
	}).Invoke(interface{}(iiii))

	//server()
	//测试：方法转换为函数后，
	//是否可访问接收器
	var cov = Cov{1}
	fmt.Println(cov.a) // 1
	testInj(cov.testCov).Invoke(interface{}(iiii))
	fmt.Println(cov.a) //11
	fmt.Println(os.Stdout)
	var tt Type2
	tt.func1()
	Type1(tt).func2()
	Type1(tt).func1()

	var ttt = Type1Chile{}
	ttt.func1()
	//func value
	//ttt.Type1.func1=ttt.func1
	ttt.func2()
}

type Type1Chile struct {
	Type1
}

func (t Type1Chile)func1(){
	fmt.Println("cild")
}

type Type1 struct {}

func (t Type1)func1(){
	fmt.Println("tpye1 func1")
}
func (t Type1)func2(){
	t.func1()
}

type Type2 Type1
func (t Type2)func1(){
	fmt.Println("type2")
}

func testLog(){
	Println("ff")
}

type testInj func(i int)

type Cov struct{
	a int
}

func (p * Cov)testCov(a int){
	p.a = a
}

func (invoke testInj) Invoke(param interface{}) {
	invoke(param.(int))
}

func server(){
	m := macaron.Classic()
	m.Group("/books", func() {
		m.Get("/:id", GetBooks)
	})
	m.Run("0.0.0.0", 8080)
}

func GetBooks(rw http.ResponseWriter, req *http.Request) {
	fmt.Println(req.URL.Path)
	rw.WriteHeader(200)
	rw.Write([]byte("Handsome boy!!\n"))
}

func testCoxType(){
	var arr1 = [2]int{1,2}
	fmt.Println(fmt.Sprintf("\ntestCoxTyp:  \n%d", arr1[0]))
	fmt.Println(&arr1[0])
	cleanArr(&arr1)
	fmt.Println(&arr1[0])
	var arr2 = arr1[:]
	fmt.Println(fmt.Sprintf("\n%T", arr2))
	months := [...]string{1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6: "December"}
	Q2 := months[4:5]
	fmt.Println(fmt.Sprintf("%d---%d---%d\n", &Q2[0], len(Q2), cap(Q2)))
	months[4]="changeFour"
	Q2[0]="notFour"
	fmt.Println(fmt.Sprintf("%d---%s---%d\n", &Q2[0], Q2[0], cap(Q2)))
	Q2=append(Q2, "seven")
	Q2=append(Q2, "seven")
	str := "123456"
	s1 := str[:3]
	println("s1 is:" + string(s1[:]))
	Q2[1] = "changeFive"
	fmt.Println(fmt.Sprintf("%d---%q---%d\n", &Q2[0], Q2[0], cap(Q2)))
	fmt.Println(months[5])
	var tslice []int
	fmt.Println(fmt.Sprintf("slice: %d--%d", len(tslice), cap(tslice)))
	tslice = append(tslice, 1)
	fmt.Println(fmt.Sprintf("slice: %d--%d", len(tslice), cap(tslice)))
	var tp *[]string = &Q2
	fmt.Println(len(*tp))
	var sl1 []int
	var sl2 = []int{}
	var sl3 = make([]int, 0)
	//0  0  0
	fmt.Println(fmt.Sprintf("%d--%d--%d\n", cap(sl1), cap(sl2), cap(sl3)))
	//t  f  f
	fmt.Println(fmt.Sprintf("%t--%t--%t\n", sl1==nil, sl2==nil,sl3==nil ))
	sl4 := make([]int, 0)
	fmt.Println(fmt.Sprintf("%d--%d\n", len(sl4), cap(sl4)))
	sl5 := append(sl4, 1)
	fmt.Println(fmt.Sprintf("%d--%d\n", len(sl4), len(sl5)))
}

func testMap(){
	var m1 map[string]int
	m2 := map[string]int{}
	m3 := make(map[string]int, 0)
	//t  f  f
	fmt.Println(fmt.Sprintf("%t--%t--%t\n", m1==nil, m2==nil, m3==nil ))
}

func cleanArr(p *[2]int){
	*p = [2]int{}
}

func fetch(url string, ch chan<-string){
	ch<-"test"
	fmt.Print(url)
}
