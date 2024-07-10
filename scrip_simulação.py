import bpy
import random
import numpy as np
import os

#Dicionarios --------------------------------------------------------------------------------------------
soil_materials = {
    1 solo_vermelho,
    2 solo_floresta,
    3 solo_marrom
}

hdri = {
    1 rCUsersmarcoDesktopTCCHDIRceu.exr,
    2 rCUsersmarcoDesktopTCCHDIRmeio_dia.exr,
    3 rCUsersmarcoDesktopTCCHDIRfinal_tarde.exr,
    4 rCUsersmarcoDesktopTCCHDIRnublado.exr
}

folhas_daninha = {
    1 Brassicaceae - Lelidium virginum,
    2 Brassicaceae - Lelidium virginum2,
    3 Solanaceae - Physalis angulata,
    4 Solanaceae - Physalis angulata2,
    5 Amaranthaceae - Amaranthus hybridos,
    6 Amaranthaceae - Amaranthus hybridos2,
    7 Apiaceae - Cyclospermum leptophyllum,
    8 Apiaceae - Cyclospermum leptophyllum2,
    9 Asteraceae - Bidens pilosa,
    10 Asteraceae - Bidens pilosa2,
    11 Asteraceae - Sonchus oleraceus,
    12 Asteraceae - Sonchus oleraceus2,
    13 Asteraceae - Tridax procumbens,
    14 Asteraceae - Tridax procumbens2,
    15 Convolvulaceae - Ipomoeae purpurea,
    16 Convolvulaceae - Ipomoeae purpurea2,
    17 Lamiaceae - Leonurus sibiricus,
    18 Lamiaceae - Leonurus sibiricus2,
    19 Poaceae - Cenchus echinatus,
    20 Poaceae - Cenchus echinatus2,
    21 Poaceae - Sorghum arundinaceum,
    22 Poaceae - Sorghum arundinaceum2,
    23 Poaceae - Rhynchelytrumrepens,
    24 Poaceae - Rhynchelytrumrepens2,
    25 Poaceae - Choris barbata,
    26 Poaceae - Choris barbata2,
    27 Poaceae - Digitaria insularis,
    28 Poaceae - Digitaria insularis2
    

}

caminho_salvar = {
    1 rendersSimulação,
    2 rendersMascara_milho,
    3 rendersMascara_daninha   
}



#--------------------------------------------------------------------------------------------------------



def create_plane(x,y,material,mat_size) #Criar SOLO
    material_value = soil_materials.get(material)
    mat = bpy.data.materials[material_value] #Definindo Material do Solo - Ele deve estar dentro do Blender
    bpy.ops.mesh.primitive_plane_add(size = x+2, calc_uvs=True, enter_editmode=False, align='WORLD', location=(x2, y2, 0.0), rotation=(0.0, 0.0, 0.0), scale=(15.0, 50, 0.0)) #Cria Plano
    bpy.context.active_object.data.materials.append(mat) #Aplica Textura
    bpy.data.materials[material_value].node_tree.nodes[Mapping].inputs[3].default_value[0] = mat_size #diminuindo textura direto do Shades Nodes
    
    if material_value == solo_floresta
        bpy.data.materials[solo_floresta].node_tree.nodes[Mapping].inputs[1].default_value[1] = random.uniform(0.1,3)
        bpy.data.materials[solo_floresta].node_tree.nodes[Mapping].inputs[1].default_value[2] = random.uniform(0.1,3)


    # !!!! TALVEZ VALE A PENA CRIAR ONDULAÇÕES NO PLANO PARA DAR MAIS REALISMO NO 3D OU CRIAR UM LANDSCAPE E NÃO UM PLANO
  
def create_hdir(luz_hdri)  #Cria LUZ HDRI por Geometry Nodes
    path = hdri.get(luz_hdri)
    C = bpy.context
    scn = C.scene

    # Get the environment node tree of the current scene
    node_tree = scn.world.node_tree
    tree_nodes = node_tree.nodes

    # Clear all nodes
    tree_nodes.clear()

    # Add Background node
    node_background = tree_nodes.new(type='ShaderNodeBackground')

    # Add Environment Texture node
    node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
    # Load and assign the image to the node property
    
    node_environment.image = bpy.data.images.load(path) # Relative path
    #node_environment.image = bpy.data.images.load(UsersmarcosfridriscvskiDesktopTCCHDIRceu.exr) # Relative path
    node_environment.location = -300,0

    # Add Output node
    node_output = tree_nodes.new(type='ShaderNodeOutputWorld')   
    node_output.location = 200,0

    # Link all nodes
    links = node_tree.links
    link = links.new(node_environment.outputs[Color], node_background.inputs[Color])
    link = links.new(node_background.outputs[Background], node_output.inputs[Surface])
    

def create_camera(x,y)  #Cria Camera
    cam1 = bpy.data.cameras.new(Camera 1)
    cam1.lens = 30 - x #Distancia Focal feita de forma empirica
    cam_obj1 = bpy.data.objects.new(Camera 1, cam1)
    cam_obj1.location = (x2, y2, 7) #Colocada no centro com altura empirica
    cam_obj1.rotation_euler = (0, 0, 0)
    bpy.context.scene.collection.objects.link(cam_obj1)
    bpy.context.scene.camera = cam_obj1   #Liga camera do scenario
    

def create_milho(x,y,contador_linha)
    for a in range(x)
        distancia_milho = 0
        z = 0
        for i in range(y)
            folhas_milho = random.randint(3,4)
            altura_milho = random.uniform(0.1,0.3)
            seed_milho = random.randint(1,30)
            erro_milho_x = random.uniform(0.0, 0.3)
            erro_milho_y = random.uniform(0.0, 0.3)
            bpy.ops.object.add_named(linked = True, name = 'Milho',matrix=((2, 0.0, 0.0, 0.0), (0.0, 2, 0.0, 0.0), (0.0, 0.0, 2, 0.0), (contador_linha + erro_milho_x + z, distancia_milho + erro_milho_y + 1, 0.0, 0.0)),drop_x = 0, drop_y = 0)
            bpy.context.object.modifiers[GeometryNodes][Input_2] = altura_milho
            bpy.context.object.modifiers[GeometryNodes][Input_3] = folhas_milho
            bpy.context.object.modifiers[GeometryNodes][Input_4] = seed_milho
            obj = bpy.context.active_object
            obj.data.update()
            distancia_milho = distancia_milho + 3
            z = 1.5
        contador_linha = contador_linha + 1

def create_dainha(x,y,qtd_dainha,daninha)
    #bpy.ops.object.add_named(session_uuid=225,matrix=((0.08, 0.0, 0.0, 0.0), (0.0, 0.08, 0.0, 0.0), (0.0, 0.0, 0.08 + z  , 0.0), (x, y, 0.0, 0.0)),drop_x = 0, drop_y = 0)
    folha = folhas_daninha.get(daninha)
    for b in range(qtd_dainha)
        rand_dainha_x = random.uniform(0,x)
        rand_dainha_y = random.uniform(0,y)
        rand_altura = random.uniform(0,0.08)
        bpy.ops.object.add_named(linked = True, name = 'Galho',matrix=((1, 0.0, 0.0, 0.0), (0.0, 1, 0.0, 0.0), (0.0, 0.0, 1 + rand_altura  , 0.0), (rand_dainha_x, rand_dainha_y, 0.0, 0.0)),drop_x = 0, drop_y = 0)
        bpy.context.object.modifiers[GeometryNodes][Input_3] = bpy.data.objects[folha]
        bpy.context.object.modifiers[GeometryNodes][Input_2] = random.uniform(0.2,0.55)
        bpy.context.object.modifiers[GeometryNodes][Input_4] = random.uniform(1,5)
        bpy.context.object.modifiers[GeometryNodes][Input_5] = random.uniform(0.2,0.5)
        #bpy.context.object.modifiers[GeometryNodes][Input_6] = random.uniform(0.2,0.5)
        obj = bpy.context.active_object
        obj.data.update() 


def render_and_save(type,moves, tipo_render)
    path = caminho_salvar.get(type)
    if str(tipo_render) == 'CYCLES'
        bpy.context.scene.render.engine = 'CYCLES' 
        bpy.context.scene.cycles.device = 'GPU' # Oculte essa linha caso o computador não tenha uma GPU Ou rode tudo em EEVEE!!!!
        bpy.context.scene.cycles.preview_samples = 10
        bpy.context.scene.cycles.samples = 10
    if str(tipo_render) == 'BLENDER_EEVEE'
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.render.filepath = path+str(moves)+.png
    bpy.ops.render.render( write_still=True)
   
    
def select(nome,state)
    for obj in bpy.context.scene.objects
        if obj.name.startswith(str(nome))
            obj.select_set(state)


def hide_show(state)
    selection = bpy.context.selected_objects 

    for obj in selection 
        bpy.data.objects[obj.name].hide_render = state


def append_material(daninha,object)
    folha = folhas_daninha.get(daninha)
    obj = bpy.data.objects.get(object)
    bpy.context.view_layer.objects.active = obj
    mat_name =  folha +_masc
    mat = bpy.data.materials.get(mat_name)
    obj.data.materials.append(mat)
    obj.data.update()
    
def set_material(daninha)    ## Ficou bem confuso essa função na real para mim ta invertido mas Fé! Parece ta funfante
    folha = folhas_daninha.get(daninha)
    obj = bpy.data.objects.get(folha)
    bpy.context.view_layer.objects.active = obj
    #bpy.context.object.active_material_index = index
    #mat_name =  folha +_masc
    mat_name_1 = obj.material_slots[0].name
    mat_name_2 = obj.material_slots[1].name
    mat_1 = bpy.data.materials.get(mat_name_1)
    mat_2 = bpy.data.materials.get(mat_name_2)       
    bpy.context.view_layer.objects.active.data.materials[1] = mat_1
    bpy.context.view_layer.objects.active.data.materials[0] = mat_2
    bpy.context.view_layer.update()

def delete_selected_objects()
    # Get a list of all selected objects
    selected_objects = bpy.context.selected_objects
    
    # Iterate over each selected object and delete it
    for obj in selected_objects
        bpy.data.objects.remove(obj, do_unlink=True)
        
def finish()
    
    
    for obj in bpy.context.scene.objects
        if obj.name == Milho
            obj.select_set(False)
        if obj.name == Galho
            obj.select_set(False)
        if obj.name == Plane.001
            obj.select_set(True)
        if obj.name == Camera 1
            obj.select_set(True)
    delete_selected_objects()
    


def mascara_daninha(folha_daninha)
    
    for num in range(len(folha_daninha))
        
        folhas = folha_daninha[num]
        folhas_count = 0
        
        for _ in range(2)
            
             set_material(folhas + folhas_count)
             folhas_count += 1
            
            
                
            
            
    
def daninha(folha_daninha)
    
    for num in range(len(folha_daninha))
         
        folhas_daninha = folha_daninha[num]
        folhas = 0
        
        for a in range(qtd_dainha)
            
            rand_x = random.uniform(0,x)
            rand_y = random.uniform(0,y)
            cria_daninha(rand_x, rand_y, num, folhas_daninha + folhas)
            
            if folhas == 0
                
                folhas = folhas + 1
                
            else
                
                folhas = folhas - 1 
                
    

def cria_daninha(x0,y0, num, daninha)
     folha = folhas_daninha.get(daninha)
     rand_altura = random.uniform(0.4,1)
     bpy.ops.object.add_named(linked = True, name = Galho ,matrix=((1, 0.0, 0.0, 0.0), (0.0, 1, 0.0, 0.0), (0.0, 0.0, 1 + rand_altura  , 0.0), (x0, y0, 0.0, 0.0)),drop_x = 0, drop_y = 0)
     new_object = bpy.context.object

     # Change the name of the copied object
     new_object.name = new_object.name + folha #Coloca o nome da Folha no Gaalho
     bpy.context.object.modifiers[GeometryNodes][Input_3] = bpy.data.objects[folha]
     bpy.context.object.modifiers[GeometryNodes][Input_2] = random.uniform(0.2,0.55)
     bpy.context.object.modifiers[GeometryNodes][Input_4] = random.uniform(1,5)
     bpy.context.object.modifiers[GeometryNodes][Input_5] = random.uniform(0.2,0.5)
     obj = bpy.context.active_object
     obj.data.update() 
    

def render_and_save_daninha(type,loop,folha_daninha)

    path = caminho_salvar.get(type)
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    
    
    folder_path = rCUsersmarcoDesktopTCCrendersMascara_daninha 
    try
        os.makedirs(folder_path +  + str(loop)  , exist_ok=True)
        print(Folder created successfully!)
    except OSError as e
        print(fFailed to create folder {e})
    
    for z in range(len(folha_daninha))
        
        folha = folhas_daninha.get(folha_daninha[z])
        
        
        for obj in bpy.context.scene.objects
            if str(folha) in obj.name
                obj.select_set(True)
                
        selection = bpy.context.selected_objects 

        for obj in selection 
            bpy.data.objects[obj.name].hide_render = False
        
        
        folder_path2 = os.path.join(folder_path, str(loop))
        file_path = os.path.join(folder_path2, str(folha) + .png)
        bpy.context.scene.render.filepath = file_path
        
        text_name = folha + _masc
        bpy.data.node_groups[Geometry Nodes.005].nodes[Set Material].inputs[2].default_value = bpy.data.materials[text_name] #Define textura do Galho das Daninha

        bpy.ops.render.render( write_still=True)
        
        
        for obj in selection 
            bpy.data.objects[obj.name].hide_render = True
            
            
        for obj in bpy.context.scene.objects
            if str(folha) in obj.name
                obj.select_set(False)

def print(data)
    for window in bpy.context.window_manager.windows
        screen = window.screen
        for area in screen.areas
            if area.type == 'CONSOLE'
                override = {'window' window, 'screen' screen, 'area' area}
                bpy.ops.console.scrollback_append(override, text=str(data), type=OUTPUT)  
                  
    
def main(folha_daninha, loop)
    
    create_plane(x,y,tipo_solo,2)  #Cria o Solo com a Textura ecolhida
    create_hdir(luz_hdri)    #Define a Luz ambiente
    create_camera(x,y)      #Cria camera no centro da Simulação
    create_milho(x,y,contador_linha)   #Cria os Milhos
    daninha(folha_daninha)    #Crias as naninhas
    
    render = 'CYCLES'       #Cycles e o modo de Renderização com Ray Tracing
    bpy.data.node_groups[Geometry Nodes.005].nodes[Set Material].inputs[2].default_value = bpy.data.materials[caule] #Define textura do Galho das Daninha
    render_and_save(1,loop,render) #Renderiza Simulação
    
    estado = True
    nome = Galho
    
    select(nome,estado) #Seleciona todas as daninhas
    hide_show(estado) #Esconde daninhas
    
    estado = False
    select(nome,estado) #Deseleciona todas as daninhas
    
    bpy.data.node_groups[Geometry Nodes].nodes[Set Material].inputs[2].default_value = bpy.data.materials[milho_masc]  #Muda Textura do Milho para Textura Mascara
    bpy.data.objects['Plane.001'].active_material = bpy.data.materials[solo_mascara] #Muda Textura do Solo para Textura Mascara
    render = 'BLENDER_EEVEE' #Modo de Renderização Simples
    render_and_save(2,loop,render) #Renderiza Simulação
    
    bpy.data.node_groups[Geometry Nodes].nodes[Set Material].inputs[2].default_value = bpy.data.materials[folha milho.001] #Volta Textura do Mulho para Textura Padrão

    
    nome = Milho
    estado = True
    select(nome,estado) #Seleciona Milho
    hide_show(estado) #Esconde Milho
    
    estado = False
    select(nome,estado) #Deseleciona Milho
    
    mascara_daninha(folha_daninha) #Troca a Textura das Daninhas para suas Mascaras
    # Colocar mascara no galho
    
    render_and_save_daninha(3,loop,folha_daninha)
    
    #render_and_save(3,a,render) # Renderiza
    
    mascara_daninha(folha_daninha) #Troca a Textura das Daninhas para textura original
    
    for obj in bpy.context.scene.objects
        obj.select_set(True)
        
    selection = bpy.context.selected_objects 
        
    for obj in selection 
            bpy.data.objects[obj.name].hide_render = False
    
    for obj in bpy.context.scene.objects
        obj.select_set(False)
        
    nome = Milho
    estado = True
    select(nome,estado) #Seleciona Milho
    nome = Galho
    select(nome,estado) #Seleciona Daninhas
    
    
    finish() #Deleta os Objetos
    
    
    
     

#Variaveis Setaveis de Simulaçãoaa
#------------------------------------------------------------------------------------------------------
x = 15
y = 15
tipo_solo = 3 # Material Solo
luz_hdri = 2 # Define HDRI
#random.seed(123)
contador_linha = -1 # Ir colocando os Milho Linha a Linha
qtd_dainha = 40
folha = [11,17,5,13]  # Folha Daninha
loop = 366 # Numero de Interações
contador = 0
lista_folhas = [1,3,5,7,9,11,13,15,17,19,21,23,25,27]
tipos_daninhas = [3,1,2,5,3,4,3,4,3,4,5,6,7,8,9,10,11,12,13,14]
tipos_solo = [2,3]


#-------------------------------------------------------------------------------------------------------------- 

#Loop Prinicpal
for contador in range(355,loop)
    
    qtd_dainha = 35
    tipo_solo = random.choice(tipos_solo)
    qtds = random.choice(tipos_daninhas)
    qtd_dainha = qtd_dainha - 2 qtds
    folha.clear()
    while len(folha)  qtds
        new_folha = random.choice(lista_folhas)
        if new_folha not in folha
            folha.append(new_folha)
    main(folha,contador)

#folhas = folhas_daninha.get(folha[1])


#mascara_daninha(folha)


