var number=document.getElementById("input");

number.onkeyup=function(){
  var isnum = /^\d+$/.test(number.value);
  var sz=number.length;

  if(isnum && sz==4){
    number.style.borderColor="green";
  }
  else{
    number.style.borderColor="red";
  }

}

function Validate(){
  var isnum = /^\d+$/.test(val);
  alert(isnum);
  return(isnum);
}
