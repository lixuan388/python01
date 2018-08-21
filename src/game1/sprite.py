import cocos
from cocos.actions import MoveBy

class Fly(cocos.layer.Layer):

    def __init__(self):
        super(Fly,self).__init__()

        rocket = cocos.sprite.Sprite('Images/rocket.png')
        rocket.position = 128,128
        rocket.scale = 0.5
        #在5秒内往右上方移动,最终横竖坐标分别增加50                                 
        rocket.do( MoveBy( (320,240), duration=2) )
        self.add(rocket, z=0)