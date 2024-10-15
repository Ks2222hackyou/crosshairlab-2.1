import dearpygui.dearpygui as gui
import glfw, threading
import win32gui
import OpenGL.GL as gl
import win32con, time
import math
import tkinter, os
import dearpygui.dearpygui as gui
from OpenGL.GL import *
from PIL import Image
import pygetwindow as gw
#https://www.rapidtables.com/web/color/RGB_Color.html


title = 'CrosshairLab v2.5'
screenx = tkinter.Tk().winfo_screenwidth()
screeny = tkinter.Tk().winfo_screenheight()





# ---------------------- Colors ----------------------

themes = {
    'default': {
        "window": (40, 40, 40, 255),
        "button": (60, 60, 60, 255),
        "text": (255, 255, 255, 255),
        "tab": (60, 60, 60, 255),
        "frame": (55, 55, 55, 255),
        "activate": (0, 150, 255, 255)
    },
    'white': {
        "window": (240, 240, 240, 255),
        "button": (220, 220, 220, 255),
        "text": (0, 0, 0, 255),
        "tab": (220, 220, 220, 255),
        "frame": (200, 200, 200, 255),
        "activate": (100, 100, 100, 255)
    },
    'orange_website': {
        "window": (0, 0, 0, 255),
        "button": (255, 120, 0, 255),
        "text": (255, 255, 255, 255),
        "tab": (255, 120, 0, 255),
        "frame": (255, 120, 0, 255),
        "activate": (0, 0, 0, 255)
    },
    'lime': {
        "window": (230, 255, 230, 255),
        "button": (180, 255, 180, 255),
        "text": (0, 0, 0, 255),
        "tab": (180, 255, 180, 255),
        "frame": (100, 200, 100, 255),
        "activate": (50, 205, 50, 255)
    },
    'night_sky': {
        "window": (0, 0, 30, 255),
        "button": (0, 0, 100, 255),
        "text": (255, 255, 255, 255),
        "tab": (0, 0, 50, 255),
        "frame": (30, 30, 70, 255),
        "activate": (25, 25, 112, 255)
    },
    'banana': {
        "window": (255, 255, 204, 255),
        "button": (255, 255, 0, 255),
        "text": (0, 0, 0, 255),
        "tab": (255, 215, 0, 255),
        "frame": (255, 165, 0, 255),
        "activate": (255, 215, 0, 255)
    }
}



def get_theme_list():
    t= []
    for i in themes.keys():
        t.append(i)
    return t

theme_list = get_theme_list()

def settheme(window,buttnon,text,tab,frame,activate):
    with gui.theme() as e:

        with gui.theme_component(gui.mvAll):
            gui.add_theme_color(gui.mvThemeCol_WindowBg, window)
            gui.add_theme_color(gui.mvThemeCol_Button, buttnon)
            gui.add_theme_color(gui.mvThemeCol_Text, text)
            gui.add_theme_color(gui.mvThemeCol_Tab, tab)
            gui.add_theme_color(gui.mvThemeCol_FrameBg, frame)
            gui.add_theme_color(gui.mvThemeCol_SliderGrab, activate)
                
            gui.add_theme_color(gui.mvThemeCol_FrameBgActive, activate)
            gui.add_theme_color(gui.mvThemeCol_TabActive, activate)
                
            gui.add_theme_color(gui.mvThemeCol_TabHovered, activate)
            gui.add_theme_color(gui.mvThemeCol_FrameBgHovered, activate)
            gui.add_theme_color(gui.mvThemeCol_ButtonHovered, activate)
            gui.add_theme_color(gui.mvThemeCol_SliderGrabActive, activate)
        
    gui.bind_theme(e)    
    try:  
        settheme(themes[gui.get_value('thm')]['window'],
            themes[gui.get_value('thm')]['button'],
            themes[gui.get_value('thm')]['text'],
            themes[gui.get_value('thm')]['tab'],
            themes[gui.get_value('thm')]['frame'],
            themes[gui.get_value('thm')]['activate'])
    except:None


def rgbeffect():
 
    def set_color(r,g,b):gui.set_value('color',[float(r),float(g),float(b),255.0])

    while True:       
        if gui.get_value('rgbef'):
            if gui.get_value('rgbef'):
                set_color(255.0, 0.0, 0.0) 

            for i in range(256):
                if gui.get_value('rgbef'):
                    set_color(255.0, i, 0.0)
                    time.sleep(0.01 / (gui.get_value('efspeed') / 2))

            for i in range(256):
                if gui.get_value('rgbef'):
                    set_color(255.0 - i, 255.0, 0.0)
                    time.sleep(0.01 / (gui.get_value('efspeed') / 2))

            for i in range(256):
                if gui.get_value('rgbef'):
                    set_color(0, 255.0 - i, i)
                    time.sleep(0.01 / (gui.get_value('efspeed') / 2))

            for i in range(256):
                if gui.get_value('rgbef'):
                    set_color(i, 0, 255.0)
                    time.sleep(0.01 / (gui.get_value('efspeed') / 2))

            for i in range(256):
                if gui.get_value('rgbef'):
                    set_color(255.0, 0, 255.0 - i)
                    time.sleep(0.01 / (gui.get_value('efspeed') / 2))       
            time.sleep(0.0001)
        else:time.sleep(0.5)











# ---------------------- Files ----------------------
def load_files():
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

pics,saves = load_files()

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
    try:
        gui.set_value('rgbef',bool(int(modules[11])))
        gui.set_value('efspeed',int(modules[12]))
    except:None

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
        if gui.get_value('rgbef')==True:
            x.write('1'+'\n')
        else:
            x.write('0'+'\n')
        x.write(str(gui.get_value('efspeed'))+'\n')

def open_folder():
    os.startfile('customcross')

def ref_files():
    global pics,saves
    pics,saves= load_files()
    gui.configure_item("path", items=pics)
    gui.configure_item("file", items=saves)










# ---------------------- other ----------------------
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










# ---------------------- Crosshair main ----------------------

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
            half_dot_size = dot_size / 2


            gl.glBegin(gl.GL_QUADS)
            gl.glVertex2f(x - half_dot_size, y - half_dot_size)
            gl.glVertex2f(x - half_dot_size, y + half_dot_size)
            gl.glVertex2f(x + half_dot_size, y + half_dot_size)
            gl.glVertex2f(x + half_dot_size, y - half_dot_size)
            gl.glEnd()

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
        
            gl.glVertex2f(x - (size + gap), y)
            gl.glVertex2f(x - gap, y)

            gl.glVertex2f(x + (size + gap), y)
            gl.glVertex2f(x + gap, y)


            gl.glVertex2f(x, y - (size + gap))
            gl.glVertex2f(x, y - gap)

            gl.glVertex2f(x, y + (size + gap))
            gl.glVertex2f(x, y + gap)
            
            gl.glEnd()
            
            if gui.get_value('dot')== True:
                dot(x,y,thickness)
        
        elif gui.get_value('t')=='x' and gui.get_value('rep')==False:
            
            gl.glBegin(gl.GL_LINES)
            
            gl.glVertex2f(x + gap, y + gap)
            gl.glVertex2f(x + size + gap, y + size + gap)

            gl.glVertex2f(x - gap, y - gap)
            gl.glVertex2f(x - size - gap, y - size - gap)

            gl.glVertex2f(x - gap, y + gap)
            gl.glVertex2f(x - size - gap, y + size + gap)

            gl.glVertex2f(x + gap, y - gap)
            gl.glVertex2f(x + size + gap, y - size - gap)
            
            gl.glEnd()

            if gui.get_value('dot')== True:
                dot(x,y,thickness)
       
        elif gui.get_value('t') == 'o' and gui.get_value('rep') == False:
            gl.glBegin(gl.GL_LINE_LOOP)

            if size > 0:
                num_segments = 10000
                for i in range(num_segments):
                    theta = 2.0 * math.pi * i / num_segments
                    dx = size * math.cos(theta)
                    dy = size * math.sin(theta)
                    gl.glVertex2f(x + dx, y + dy)        
            gl.glEnd()
            
            if gui.get_value('dot') == True:
                dot(x, y, thickness)
       
        elif gui.get_value('rep')==True:

            texture_id, img_width, img_height = load_texture("customcross/"+gui.get_value('path'))
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, texture_id)
              
            gui.set_value('color',[255.0,255.0,255.0,255.0])
            if gui.get_value('rgbef')==True:
                gui.set_value('rgbef',False)


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










# ---------------------- GUI ----------------------
modes = ['+','x','o']

def threads():
    threading.Thread(target=corshair, daemon=True).start()
    threading.Thread(target=rgbeffect, daemon=True).start()

gui.create_context()
gui.create_viewport(title=title, width=400, height=400)
gui.setup_dearpygui()
gui.set_viewport_resizable(False)


with gui.window(label='CrosshairLab v2.3', width=385,height=400,no_title_bar=True,no_resize=True, no_move=True, show=True):
    with gui.tab_bar(label='cross'): 
        with gui.tab(label='Crosshair'):
            with gui.tab_bar(label="Crosshair"):
                with gui.tab(label='crosshair'):
                    gui.add_listbox(label='type',tag='t',items=modes, default_value='+')
                    gui.add_slider_int(label='size', tag='size', min_value=1, max_value=50, default_value=6)
                    gui.add_slider_int(label='gap', tag='gap', min_value=0, max_value=50, default_value=4)
                    gui.add_slider_int(label='thick', tag='thick', min_value=1, max_value=10, default_value=2)
                    gui.add_checkbox(label='dot',tag='dot')
                    gui.add_button(label='reset',callback=reset,width=100)
                with gui.tab(label='color'):
                    gui.add_color_picker(label='color:',tag='color', default_value=[255.0,255.0,255.0,255.0],height=200,width=200)
                    gui.add_checkbox(label='rgb effect',tag='rgbef')
                    gui.add_slider_int(label='effect speed',tag='efspeed',min_value=1,max_value=20,default_value=5)
                with gui.tab(label='position'):
                    gui.add_slider_int(label='posx', min_value=1,max_value=screenx,default_value=screenx/2, tag='posx',width=300)
                    gui.add_slider_int(label='posy', min_value=1,max_value=screeny,default_value=screeny/2, tag='posy',width=300)
                    gui.add_button(label='reset position',callback=reset_pos,width=150)
                with gui.tab(label='img to cross'):
                    gui.add_checkbox(label='replace crosshair with image',tag='rep')
                    gui.add_listbox(label='path',tag='path',items=pics)
                    gui.add_button(label='refresh files',callback=ref_files,width=100)
                    gui.add_button(label='open folder',callback=open_folder,width=100)
                with gui.tab(label='save/load'):
                    gui.add_text(label='Load',default_value='Load')
                    gui.add_listbox(label='',tag='file',items=saves)
                    gui.add_button(label='load',callback=load,width=100)
                    gui.add_button(label='refresh files',callback=ref_files,width=100)
                    gui.add_text(label='Save',default_value='Save')
                    gui.add_input_text(label='save name',tag='savename')
                    gui.add_button(label='save',callback=save,width=100)
       
        with gui.tab(label='Settings'):
            with gui.tab_bar(label="themes"):
                with gui.tab(label='theme'):
                    gui.add_listbox(label='themes',tag='thm',items=theme_list, default_value='default', width=300,callback=settheme)







gui.show_viewport()
threads()
gui.start_dearpygui()
gui.destroy_context()