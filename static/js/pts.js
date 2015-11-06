/**
 * Created by fp862 on 2015/10/28.
 */

$(document).ready(function () {
    /* 处理选择答案时的颜色变化*/
    $(':radio').click(function (event) {
        var curVal = $(this).val(); // answer option
        var qid = $(event.target).attr('name');  //question_id
        var id = 'ans' + qid;
        var rightAns = $('#' + id).val();
        if (curVal == rightAns) {
            $('#' + qid + curVal).css("color", "green");//style.color = "green";
        } else {
            $('#' + qid + curVal).css("color", "red");
            //document.getElementById(qid+curVal).style.color = "red";
        }
    });
    /*处理勾选掌握框*/

    $('.answer').click(function (event) {
        var id = $(event.target).attr('id');
        var qid = $(event.target).attr("qid"); //question id
        var userid = $(event.target).attr("userid"); // user id
        var ck = $(this).is(':checked');
        if (ck) {//掌握框被选中
            $.get("/master/", {'qid': qid, 'userid': userid, 'ismaster': 1}, function (data, textStatus) {
                //$('#'+id).(ret)
                //alert(data);
            })
        } else {
            $.get("/master/", {'qid': qid, 'userid': userid, 'ismaster': 0}, function (data, textStatus) {
                //$('#'+id).(ret)
                //alert(data);
            })
        }
    });

    //键盘操作
    $(document).keydown(function (event) {
        //alert(window.location.href)
        alert(window.location.search)
        switch (event.keyCode) {
            case 37:
            case 81:
                //alert('前一个');
                break;
            case 39:
            case 88:
                //alert('后一个');
                break;
        }
        ;
        return false;
    });

});