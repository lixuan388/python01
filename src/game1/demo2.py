import cocos
#自定义菜单类
class main_menu(cocos.menu.Menu):
    def __init__(self):
        super(main_menu, self).__init__()
        #文本菜单项  （文字，回掉函数）
        item1=cocos.menu.MenuItem('开始',self.item1_callback)
        # 开关菜单项  （文字，回掉函数，状态）
        item2 = cocos.menu.ToggleMenuItem('音效', self.item2_callback,False)
        #创建菜单（添加项的列表，选中效果，未选中效果）
        self.create_menu([item1,item2],
                         selected_effect=cocos.menu.shake(),
                         unselected_effect=cocos.menu.shake_back(),
                                    )
 
        #改变字体
        self.font_item['font_size']=22
        #选中时
        self.font_item_selected['font_size']=33
 
 
    def item1_callback(self):
        print('item1')
    def item2_callback(self,value):
        print('item2')
if __name__=='__main__':
    #初始化导演
    cocos.director.director.init(width=640,height=480,caption="hello world")
    #创建层   的实例
    mainmenu=main_menu()
    #创建场景   添加层进来
    main_scence=cocos.scene.Scene(mainmenu)
    #启动场景
    cocos.director.director.run(main_scence)
 