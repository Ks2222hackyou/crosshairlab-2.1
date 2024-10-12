import dearpygui.dearpygui as gui
import glfw, threading
import win32gui
import OpenGL.GL as gl
import win32con, time
import math,mouse
import tkinter, os
import dearpygui.dearpygui as gui
from OpenGL.GL import *
from PIL import Image
import pygetwindow as gw
#https://www.rapidtables.com/web/color/RGB_Color.html


title = 'CrosshairLab v2.3'
screenx = tkinter.Tk().winfo_screenwidth()
screeny = tkinter.Tk().winfo_screenheight()

modes = ['+','x','o']
def load():
    try:
        pics = os.listdir('customcross')
    except:
        os.makedirs('customcross')
        pics = os.listdir('customcross')

    try:
        saves = os.listdir('saves')
    except:    
        os.makedirs('saves')
        saves = os.listdir('saves')
    return pics,saves

pics,saves = load()

def load():
    file = 'saves/'+gui.get_value('file')
    file = open(file=file)
    file = file.readlines()
    print(file)
    modules = []
    for i in file:
        modules.append(i.replace('\n',''))
    
    gui.set_value('t',modules[0])
    gui.set_value('size',int(modules[1]))
    gui.set_value('gap',int(modules[2]))
    gui.set_value('thick',int(modules[3]))
    gui.set_value('posx',int(modules[4]))
    gui.set_value('posy',int(modules[5]))
    gui.set_value('color',[float(modules[6]),float(modules[7]),float(modules[8]),255.0])
    gui.set_value('rep',bool(int(modules[9])))
    gui.set_value('dot',bool(int(modules[10])))

def save():
    with open('saves/'+gui.get_value('savename')+'.Clab', 'w') as x:

        x.write(str(gui.get_value('t'))+'\n')
        x.write(str(gui.get_value('size'))+'\n')
        x.write(str(gui.get_value('gap'))+'\n')
        x.write(str(gui.get_value('thick'))+'\n')
        x.write(str(gui.get_value('posx'))+'\n')
        x.write(str(gui.get_value('posy'))+'\n')
        x.write(str(gui.get_value('color')[0])+'\n')
        x.write(str(gui.get_value('color')[1])+'\n')
        x.write(str(gui.get_value('color')[2])+'\n')
        if gui.get_value('rep')==True:
            x.write('1'+'\n')
        else:
            x.write('0'+'\n')
        if gui.get_value('dot')==True:
            x.write('1'+'\n')
        else:
            x.write('0'+'\n')


def open_folder():
    os.startfile('customcross')

def reset_pos():
    gui.set_value('posx',screenx/2)
    gui.set_value('posy',screeny/2)

def reset():
    gui.set_value('t','+')
    gui.set_value('size',6)
    gui.set_value('gap',4)
    gui.set_value('thick',2)
    gui.set_value('posx',screenx/2)
    gui.set_value('posy',screeny/2)
    gui.set_value('color',[255.0,255.0,255.0,255.0])
    gui.set_value('rep',False)
    gui.set_value('dot',False)

def corshair():
    glfw.init()
    glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, True)
    glfw.window_hint(glfw.FLOATING, True)
    glfw.window_hint(glfw.DECORATED, False)

    window = glfw.create_window(screenx, screeny, 'Crosshairlabrender', None, None)
    glfw.make_context_current(window)
    gl.glOrtho(0, screenx, 0, screeny, -1, 1)

    handle = win32gui.FindWindow(0, 'Crosshairlabrender')

    exStyle = win32gui.GetWindowLong(handle, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(handle, win32con.GWL_EXSTYLE, exStyle | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

    def dot(x, y, dot_size):
    
        if dot_size > 0:
            half_dot_size = dot_size/2
        
        gl.glVertex2f(x - half_dot_size, y - half_dot_size)
        gl.glVertex2f(x - half_dot_size, y + half_dot_size)
        
        gl.glVertex2f(x - half_dot_size, y + half_dot_size)
        gl.glVertex2f(x + half_dot_size, y + half_dot_size)

        gl.glVertex2f(x + half_dot_size, y + half_dot_size)
        gl.glVertex2f(x + half_dot_size, y - half_dot_size)

        gl.glVertex2f(x + half_dot_size, y - half_dot_size)
        gl.glVertex2f(x - half_dot_size, y - half_dot_size)
    
    def get_color():
        return (int(gui.get_value('color')[0]/2),int(gui.get_value('color')[1]/2),int(gui.get_value('color')[2]/2))

    
    def load_texture(image_path):
        
        img = Image.open(image_path)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  
        img_data = img.convert("RGBA").tobytes()

        
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)


        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

       
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        return texture_id, img.width, img.height
    
    gw.getWindowsWithTitle(title=title)[0].activate()
    
    while True:
        size = gui.get_value('size')
        gap = gui.get_value('gap')

        thickness = gui.get_value('thick')*2
        size = gui.get_value('size')
        gap = gui.get_value('gap')
        x = gui.get_value('posx')
        y = gui.get_value('posy')
        color1 = get_color()
           
        glfw.swap_buffers(window)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.poll_events()
        time.sleep(0.001)

        gl.glLineWidth(thickness)
        gl.glColor3b(*color1)
        

        if gui.get_value('t')=='+' and gui.get_value('rep')==False:
            
            gl.glBegin(gl.GL_LINES)
            
            
            if gui.get_value('dot')== True:
                dot(x,y,thickness)
 
            
            gl.glVertex2f(x - (size + gap), y)
            gl.glVertex2f(x - gap, y)

            gl.glVertex2f(x + (size + gap), y)
            gl.glVertex2f(x + gap, y)


            gl.glVertex2f(x, y - (size + gap))
            gl.glVertex2f(x, y - gap)

            gl.glVertex2f(x, y + (size + gap))
            gl.glVertex2f(x, y + gap)
            
            gl.glEnd()
        
        elif gui.get_value('t')=='x' and gui.get_value('rep')==False:
            
            gl.glBegin(gl.GL_LINES)
         
            if gui.get_value('dot')== True:
                dot(x,y,thickness)
            
            gl.glVertex2f(x+size,y+size)
            gl.glVertex2f(x-size,y-size)
            
            gl.glVertex2f(x-size,y+size)
            gl.glVertex2f(x+size,y-size)
            
            gl.glEnd()
       
        elif gui.get_value('t')=='o' and gui.get_value('rep')==False:
            
            gl.glBegin(gl.GL_LINE_LOOP)

            if size > 0:
                gl.GL_TRIANGLE_FAN
                num_segments = 10000
                for i in range(num_segments):
                    theta = 2.0 * math.pi * i / num_segments
                    dx = size * math.cos(theta)
                    dy = size * math.sin(theta)
                    gl.glVertex2f(x + dx, y + dy)
            if gui.get_value('dot')== True:
                dot(x,y,thickness)
            
            gl.glEnd()
       
        elif gui.get_value('rep')==True:

            texture_id, img_width, img_height = load_texture("customcross/"+gui.get_value('path'))
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, texture_id)
              
            gui.set_value('color',[255.0,255.0,255.0,255.0])


            half_width = img_width / 2
            half_height = img_height / 2

            glBegin(GL_QUADS)
            glTexCoord2f(0, 0)
            glVertex2f(x - half_width, y - half_height)  
            glTexCoord2f(1, 0)
            glVertex2f(x + half_width, y - half_height)  
            glTexCoord2f(1, 1)
            glVertex2f(x + half_width, y + half_height) 
            glTexCoord2f(0, 1)
            glVertex2f(x - half_width, y + half_height)  
            glEnd()

            glDisable(GL_TEXTURE_2D)


def threads():
    threading.Thread(target=corshair, daemon=True).start()




gui.create_context()
gui.create_viewport(title=title, width=400, height=400)
gui.setup_dearpygui()
gui.set_viewport_resizable(False)


with gui.window(label='CrosshairLab v2.3', width=385,height=400,no_title_bar=True,no_resize=True, no_move=True, show=True):
    with gui.tab_bar(label='cross'): 
        with gui.tab(label='crosshair'):
            gui.add_listbox(label='type',tag='t',items=modes, default_value='+')
            gui.add_slider_int(label='size', tag='size', min_value=1, max_value=50, default_value=6)
            gui.add_slider_int(label='gap', tag='gap', min_value=1, max_value=50, default_value=4)
            gui.add_slider_int(label='thick', tag='thick', min_value=1, max_value=10, default_value=2)
            gui.add_checkbox(label='dot',tag='dot')
            gui.add_button(label='reset',callback=reset,width=100)
        with gui.tab(label='color'):
            gui.add_color_picker(label='color:',tag='color', default_value=[255.0,255.0,255.0,255.0])
        with gui.tab(label='position'):
            gui.add_slider_int(label='posx', min_value=1,max_value=screenx,default_value=screenx/2, tag='posx',width=300)
            gui.add_slider_int(label='posy', min_value=1,max_value=screeny,default_value=screeny/2, tag='posy',width=300)
            gui.add_button(label='reset position',callback=reset_pos,width=150)
        with gui.tab(label='img to cross'):
            gui.add_checkbox(label='replace crosshair with image',tag='rep')
            gui.add_listbox(label='path',tag='path',items=pics)
            gui.add_button(label='open folder',callback=open_folder,width=100)
        with gui.tab(label='save/load'):
            gui.add_text(label='Load',default_value='Load')
            gui.add_listbox(label='',tag='file',items=saves)
            gui.add_button(label='load',callback=load,width=100)
            gui.add_text(label='Save',default_value='Save')
            gui.add_input_text(label='save name',tag='savename')
            gui.add_button(label='save',callback=save,width=100)
            



gui.show_viewport()
threads()
gui.start_dearpygui()
gui.destroy_context()