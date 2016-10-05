# http://stackoverflow.com/questions/39313159/background-image-is-not-showing-up-on-gosu 

require 'gosu'
#require_relative 'player'
#require_relative 'enemy'
#require_relative 'bullet'
#require_relative 'eb_bullet'
#require_relative 'explosion'

class SectorFive < Gosu::Window
#  ENEMY_FREQUENCY = 0.03
#  ENEMY_BULLET_FREQUENCY = 0.009

  def initialize(width=800, height=400)
    @width     = width
    @height    = height
    super width, height, false
    self.caption = "Sector Five"
    @background_image = Gosu::Image.new('images/start_screen.png')
  end

  def update              # <-- updates @60hZ; game logic goes here
  end

  def draw
    @background_image.draw(0, 0, 0)
  end

end

window = SectorFive.new
window.show


