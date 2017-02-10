var number=document.getElementById("input");
var myDropzone = new Dropzone("#mydropzone", {
  url : '{% url phast.views.index %}'
});
//password!!

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
