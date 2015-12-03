/**
 * Created by fp862 on 2015/10/28.
 */

$(document).ready(function () {
    /*处理判题*/
    $('#judge').click(function (event) {
        var wrongNum = 0;
        $("li").removeClass("wrong-answer lost-answer"); //先去除所有的附加判断的类
        $('div#question_area>ul>li').each(function (index, element) { //获取包含每道题的li

            var eachLi = $(element);
            var ro = eachLi.find('input:hidden'); //注意children函数只会查找直接子元素
            //alert(ro.val());
            var doOrNot = false;
            /*判断是否选择答案 ，选择了的，判断是否正确*/
            eachLi.find(":radio").each(function (i, e) {
                var isChecked = $(e).is(":checked");
                if (isChecked == true) {
                    doOrNot = true;
                    if (ro.val() != $(e).val()) {
                        eachLi.addClass("wrong-answer");
                        wrongNum += 1;
                    }
                }
            });
            if (!doOrNot) {
                //alert(eachLi.attr("index") + " : 未做答");
                eachLi.addClass("lost-answer");
                wrongNum += 1;
            }
        });
        $("#score_area").empty();
        if (wrongNum != 0) {
            $("#score_area").append(" <b>你错了" + wrongNum + "道题</b>.");
        } else {
            $("#score_area").append(" <b>恭喜你！满分！</b>.");
        }
    });

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
        var view = window.location.pathname;
        if (view == '/question') {
            var ival = parseInt($.getUrlParam('page'));
            if (isNaN(ival)) {
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
                    window.location.href = view + '?page=' + (ival + 1);
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
