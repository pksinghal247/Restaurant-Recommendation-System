(function($) {
    // 本函数每次调用只负责一个轮播图的功能
    // 也就是说只会产生一个轮播图，这个函数的作用域只能分配给一个轮播图
    // 要求在调用本函数的时候务必把当前轮播图的根标签传递过来
    // 这里的形参 ele 就是某个轮播的根标签
    var slide = function(ele,options) {
        var $ele = $(ele);
        // 默认设置选项
        var setting = {
        		// 控制轮播的动画时间
            speed: 1000,
            // 控制 interval 的时间 (轮播速度)
            interval: 2000,
            
        };
        // 对象合并
        $.extend(true, setting, options);
        // 规定好每张图片处于的位置和状态
        var states = [
            { $zIndex: 1, width: 170, height: 130, top: 69, left: 124, $opacity: 0.2 },
            { $zIndex: 2, width: 190, height: 140, top: 59, left: 60, $opacity: 0.4 },
            { $zIndex: 3, width: 238, height: 180, top: 49, left: 110, $opacity: 0.6 },
            { $zIndex: 4, width: 308, height: 234, top: 35, left: 200, $opacity: 0.8 },
            { $zIndex: 5, width: 378, height: 260, top: 25, left: 330, $opacity: 1 },
            { $zIndex: 4, width: 308, height: 234, top: 35, left: 550, $opacity: 0.8 },
            { $zIndex: 3, width: 238, height: 180, top: 49, left: 700, $opacity: 0.6 },
            { $zIndex: 2, width: 190, height: 140, top: 59, left: 820, $opacity: 0.4 },
            { $zIndex: 1, width: 170, height: 130, top: 69, left: 750, $opacity: 0.2 }
        ];

        var $lis = $ele.find('li');
        var timer = null;

        // 事件
        $ele.find('.hi-next').on('click', function() {
            next();
        });
        $ele.find('.hi-prev').on('click', function() {
            states.push(states.shift());
            move();
        });
        $ele.on('mouseenter', function() {
            clearInterval(timer);
            timer = null;
        }).on('mouseleave', function() {
            autoPlay();
        });

        move();
        autoPlay();

        // 让每个 li 对应上面 states 的每个状态
        // 让 li 从正中间展开
        function move() {
            $lis.each(function(index, element) {
                var state = states[index];
                $(element).css('zIndex', state.$zIndex).finish().animate(state, setting.speed).find('img').css('opacity', state.$opacity);
            });
        }

        // 切换到下一张
        function next() {
            // 原理：把数组最后一个元素移到第一个
            states.unshift(states.pop());
            move();
        }

        function autoPlay() {
            timer = setInterval(next, setting.interval);
        }
    }
    // 找到要轮播的轮播图的根标签，调用 slide()
    $.fn.hiSlide = function(options) {
        $(this).each(function(index, ele) {
            slide(ele,options);
        });
        // 返回值，以便支持链式调用
        return this;
    }
})(jQuery);
