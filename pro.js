let num = 50;
function hello(){
    console.log("你好!!")
}
console.log(num);
console.log(this.num);
console.log(window.num);
hello();
this.hello();
window.hello();