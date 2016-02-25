    //<![CDATA[ 

function Line(startX, startY, endX, endY, raphael) {
    var start = {
        x: startX,
        y: startY
    };
    var end = {
        x: endX,
        y: endY
    };
    var getPath = function() {
        return "M" + start.x + " " + start.y + " L" + end.x + " " + end.y;
    };
    var redraw = function() {
        node.attr("path", getPath());
    }

    var node = raphael.path(getPath());
    return {
        updateStart: function(x, y) {
            start.x = x;
            start.y = y;
            redraw();
            return this;
        },
        updateEnd: function(x, y) {
            end.x = x;
            end.y = y;
            redraw();
            return this;
        }
    };
};



$(document).ready(function() {
    var tutorial_image = $('#animate_img');
    console.log(tutorial_image.offset().width)
    console.log(tutorial_image.offset().height)

    var paper = Raphael("raphaelContainer", 900, 200);
    var x = 50,
    y = 20,
    width = 500,
    height = 50;

    $("#raphaelContainer").mousedown(

    function(e) {
        x = e.offsetX;
        y = e.offsetY;
        line = Line(x, y, x, y, paper);
        $("#raphaelContainer").bind('mousemove', function(e) {
            x = e.offsetX;
            y = e.offsetY;
            line.updateEnd(x, y);
            console.log(x)
            console.log(y)
        });

    });

    $("#raphaelContainer").mouseup(

    function(e) {
        $("#raphaelContainer").unbind('mousemove');
    });
});
    //]]> 