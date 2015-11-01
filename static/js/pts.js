/**
 * Created by fp862 on 2015/10/28.
 */

function radioclick(id, opt){
    var ans_id = 'ans'+id;
    var ans = $('#'+ans_id).val()
    var id = ''+id+opt;
    if (opt == ans){
        document.getElementById(id).style.color="green";
    }else{
        document.getElementById(id).style.color="red";
        //$(this).css("backgroud-color","red"); 不太会用。。。
    }
}
