/**
 * Created by fp862 on 2015/10/28.
 */

$(document).ready(function () {
    /* 处理选择答案时的颜色变化*/
    $('.option').click(function (event) {
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
        var view = window.location.pathname;
        if (view == '/question') {
            var ival = parseInt($.getUrlParam('page'));
            if (isNaN(ival)){
                ival = 1;
            }
            switch (event.keyCode) {
                case 37:
                case 81:
                    if (ival > 1) {
                        window.location.href = view + '?page=' + (ival - 1);
                    }
                    break;
                case 39:
                case 88:
                    window.location.href = view+'?page='+(ival+1);
                    break;
            }
            return false;
        }
    });
});

//获取url中的参数
(function ($) {
    $.getUrlParam = function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
        var r = window.location.search.substr(1).match(reg);  //匹配目标参数
        if (r != null) return decodeURI(r[2]);
        return null; //返回参数值
    }
})(jQuery);
