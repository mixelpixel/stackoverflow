# http://stackoverflow.com/questions/33908465/errors-when-using-require-gosu-mac-os

# require 'rubygems'
require 'gosu'
 
# class Ball 
#   def initialize(the_window)
#     @x = 200
#     @y = 200
#     @w = 20
#     @h = 20
#     @image = Gosu::Image.new(the_window, "ball.png", false)
#   end
# end
# 
# def draw
#   @image.draw(@x, @y , 1)
# end

# end

class GameWindow < Gosu::Window
  def initialize
    super 800, 600, false
    self.caption = "Paddle Game"
#     @ball = Ball.new(self)
  end

  def update
  end

  def draw
#     @ball.draw
  end
end

window = GameWindow.new
window.show


