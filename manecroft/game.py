from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

#quit game
def input(key):
    if key == 'escape':
        quit()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')

current_texture = grass_texture

#what's in hand
palm = 'block'
slot = 1

#update function
def update():
    global current_texture
    global palm
    global slot

    if held_keys['0']: 
        palm = 'empty'
        slot = 0
        hand.empty_hand()

    if held_keys['1']: 
        palm = 'block'
        slot = 1
        current_texture = grass_texture
        hand.block_in_hand()

    if held_keys['2']: 
        palm = 'block'
        slot = 2
        current_texture = stone_texture
        hand.block_in_hand()

    if held_keys['3']: 
        palm = 'block'
        slot = 3
        current_texture = brick_texture
        hand.block_in_hand()

    if held_keys['4']:
        palm = 'block'
        slot = 4 
        current_texture = dirt_texture
        hand.block_in_hand()

    if slot == 1:
        item_bar.slot1.selected()
    else:
        item_bar.slot1.passive()

    if slot == 2:
        item_bar.slot2.selected()
    else:
        item_bar.slot2.passive()

    if slot == 3:
        item_bar.slot3.selected()
    else:
        item_bar.slot3.passive()

    if slot == 4:
        item_bar.slot4.selected()
    else:
        item_bar.slot4.passive()

    if (held_keys['left mouse'] or held_keys['right mouse']) and palm == 'block':
        hand.block_active()
    elif palm == 'block':
        hand.block_passive()
    
    if held_keys['left mouse'] and palm == 'empty':
        hand.empty_hand_active()
    elif palm == 'empty':
        hand.empty_hand_passive() 

#block class
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.color(0, 0, 0.9),
            scale = 0.5
        )
    
    def input(self, key):
        if self.hovered:
            distance = self.position - player.position
            if distance.length() <= 6:
                if key == 'right mouse down' and palm == 'block':
                    voxel = Voxel(position = self.position + mouse.normal, texture = current_texture)
                if key == 'left mouse down':
                    destroy(self)


#sky class
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True 
        )

#hand class           
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/block',
            texture = grass_texture,
            scale = 0.2,
            rotation = Vec3(-20,-20,0),
            position = Vec2(0.6,-0.57)
        )
    
    def empty_hand(self):
        palm = 'empty'
        self.model = 'assets/arm'
        self.texture = arm_texture
        self.rotation = Vec3(150,-20,0)
        self.position = Vec2(0.6,-0.6)

    def empty_hand_active(self):
        self.rotation = Vec3(160,-30,0)
        self.position = Vec2(0.5,-0.5)

    def empty_hand_passive(self):
        self.rotation = Vec3(150,-20,0)
        self.position = Vec2(0.6,-0.6)

    def block_in_hand(self):
        palm = 'block'
        self.model = 'assets/block'
        self.texture = current_texture
        self.rotation = Vec3(-20,-20,0)
        self.position = Vec2(0.6,-0.57)
    
    def block_active(self):
        self.rotation = Vec3(-10,-30,0)
        self.position = Vec2(0.5, -0.47)

    def block_passive(self):
        self.rotation = Vec3(-20,-20,0)
        self.position = Vec2(0.6,-0.57)

#item bar
class ItemBar(Entity):
    def __init__(self):
        x = -0.79
        y = 0.41
        dy = 0.1

        self.slot1 = self.slot(texture = grass_texture, position = Vec2(x,y))
        self.slot2 = self.slot(texture = stone_texture, position = Vec2(x,y-dy))
        self.slot3 = self.slot(texture = brick_texture, position = Vec2(x,y-2*dy))
        self.slot4 = self.slot(texture = dirt_texture, position = Vec2(x,y-3*dy))

    class slot(Entity):
        def __init__(self, texture, position):
            super().__init__(
                parent = camera.ui,
                model = 'assets/block',
                texture = texture,
                scale = 0.025,
                rotation = Vec3(-10,-45,-10),
                position = position
            )
        
        def passive(self):
            self.scale = 0.025

        def selected(self):
            self.scale = 0.031

for z in range(14):
    for x in range(14):
        voxel = Voxel(position = (x,0,z), texture = grass_texture)

player = FirstPersonController()
sky = Sky()
hand = Hand()
item_bar = ItemBar()


app.run()