
let red_btn = document.getElementById("red_btn")
let blue_btn = document.getElementById("blue_btn")
let green_btn = document.getElementById("green_btn")
let content = document.getElementById("content")

red_btn.addEventListener("click", () => {
    alert("click U 🙌 red")
    content.style.backgroundColor = "red"
    content.style.color = "white"
})

blue_btn.addEventListener("click", () => {
    alert("click U 🙌 blue")
    content.style.backgroundColor = "blue"
    content.style.color = "plum"
})

green_btn.addEventListener("click", () => {
    alert("click U 🙌 green")
    content.style.backgroundColor = "green"
    content.style.color = "yellow"
})

let a = "안녕 ?"            // 변수선언
const b = "Bear-U ?"       // 상수선언
alert(a); alert(b)
a = "잘가 !"
alert(a)
b = "Bye !" // 여기부턴 실행 X 상수를 변경하려 해서 Error
alert(b); alert(a)
/*  F12 개발자도그 들어가서 보면 Console에서 Error 내용 확인 가능
    Uncaught TypeError: Assignment to constant variable.
    at web_page.html:51:15

    function func_name() {
    }
    const func_const_name = () => {
        화살표 함수는 함수를 변수에 할당하여 사용하는 JavaScript의 기능 중 하나입니다.
        주로 익명 함수(anonymous function)를 만들거나 함수를 변수에 저장할 때 사용됩니다.
        간결한 문법으로 함수를 정의할 수 있으며, 주로 콜백 함수나 고차 함수를 작성할 때 활용됩니다.

        나는 이게.. 함수포인터랑 비슷하게 보임
        함수 포인터 (Function Pointer) - C 언어:
        함수 포인터는 C 언어에서 함수를 가리키는 포인터 변수입니다.
        함수 포인터를 사용하여 함수를 저장하고, 이 함수를 다른 함수에 전달하거나 동적으로 선택하여 호출할 수 있습니다.
        주로 콜백 함수 또는 함수를 배열 또는 구조체 멤버로 저장할 때 사용됩니다.                    
    }
*/