Function.prototype._constructor = Function.prototype.constructor
Function.prototype.constructor = function (){
    if(arguments[0]==='debugger'){
        debugger;
        return function (){}
    }else {
        debugger;
        return Function.prototype._constructor.apply(this.arguments)
    }
}


Function_ = Function
Function = function (){
    console.log(123456);
    if(arguments[0]==='debugger'){
        return function (){};
    }
    console.log(112233);
    return Function_.apply(this.arguments);
}

Object_ = Object
Object = function (){
    debugger;
    console.log(112233);
    return Object_.apply(this.arguments);
}

var old_parse = JSON.parse;
JSON.parse = function (s){
    debugger;
    return old_parse(s);
}
