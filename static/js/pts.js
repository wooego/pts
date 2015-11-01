/**
 * Created by fp862 on 2015/10/28.
 *
 function radioclick(id, opt) {
            var ans_id = 'ans' + id;
            var ans = $('#' + ans_id).val()
            var id = '' + id + opt;
            if (opt == ans) {
                document.getElementById(id).style.color = "green";
            } else {
                document.getElementById(id).style.color = "red";
                //$(this).css("backgroud-color","red"); 不太会用。。。
            }
        }
 */
$(document).ready(function () {
    $(':radio').click(function (event) {
        var curVal = $(this).val(); // answer option
        var qid = $(event.target).attr('name');  //question_id
        var id = 'ans' + qid;
        var rightAns = $('#' + id).val();
        if (curVal == rightAns) {
            $('#'+qid+curVal).css("color","green");//style.color = "green";
        } else {
            $('#'+qid+curVal).css("color","red");
            //document.getElementById(qid+curVal).style.color = "red";
        }
    });
});