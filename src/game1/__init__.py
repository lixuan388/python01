import cocos

from game1.demo2 import main_menu 
from game1.demo import HelloWorld 
from game1.sprite import Fly 

if __name__=='__main__':
    #初始化导演
    cocos.director.director.init(width=640,height=480,caption="hello world")
    #创建场景   添加层进来
    main_scence=cocos.scene.Scene()
    
    #创建层   的实例
    fly=Fly()
    main_scence.add(fly,0)
    
    #创建层   的实例
    mainmenu=main_menu()
    main_scence.add(mainmenu,1)
    
    #创建层   的实例
    HelloWorld=HelloWorld()
    main_scence.add(HelloWorld,2)
    
    #启动场景
    cocos.director.director.run(main_scence)
 