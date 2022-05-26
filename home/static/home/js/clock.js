function digitalclock(){

    var date = new Date(); //defining an object
    
    var hours=date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    var per; //eathir AM or PM 
    var Name = "";
    hours = updateTime(hours);
    minutes = updateTime(minutes);
    seconds = updateTime(seconds);

    per = (hours>=12) ? "PM" : "AM"; 
    document.getElementById("clock").innerHTML = "<span>"+hours+"</span>" + ":" +"<span>"+minutes+"</span>" + ":" +"<span>"+ seconds+"</span>";
    document.getElementById("cl2").innerHTML =per;
    var time = setTimeout(function(){digitalclock();} , 1000);


//Printing the messages.. 
    if(hours <12 ){ var message ="Good Morning♡" + Name +""+"<br>"+""; }
    if (hours >= 12 && hours <=18){ var message = "Good Afternoor♡" + Name+""+"<br>"+""; }
    if (hours>= 18 && hours <= 24){ var message = "Good Evening♡" +Name+"<br>";}
    
    document.getElementById("message").innerHTML = message;


} //end of digitalclock() function..


function day(){

    date=new Date();
    document.getElementById("demo1").innerHTML=date.toLocaleDateString();
}


function updateTime(x){

    if (x <10 ){ return "0" + x; }
    else{ return x; }

}//end of updatetime function..

// calling the clock function.. 
digitalclock();
day();