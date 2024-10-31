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
import ast, json, random, keyboard
#https://www.rapidtables.com/web/color/RGB_Color.html


title = 'CrosshairLab v2.7.1'
screenx = tkinter.Tk().winfo_screenwidth()
screeny = tkinter.Tk().winfo_screenheight()






# ---------------------- Colors ----------------------

def savelatesttheme():
    with open('themes/latest.clab', 'w') as x:

        x.write(gui.get_value('thm'))

def savethemes():
    with open('themes/themes.json', 'w') as file:
        json.dump(themes, file, indent=4)

def loadthemes():
    try:
        with open('themes/themes.json', 'r') as file:
            global themes
            return json.load(file)
    except:
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
                "activate": (255, 190, 0, 255)
            }
        }
        try:
            os.makedirs('themes')
        except:None
        savethemes()
        return themes

def removetheme():
    with open('themes/themes.json', 'r') as file:
        themes = json.load(file)
    if gui.get_value('thm') in themes and gui.get_value('thm') not in {'default', 'white', 'orange_website', 'lime', 'night_sky', 'banana', 'sunset'}:
        del themes[gui.get_value('thm')]
        with open('themes/themes.json', 'w') as file:
            json.dump(themes, file, indent=4)
    ref_themes()

def get_theme_list():
    t= []
    for i in themes.keys():
        t.append(i)
    return t

themes = loadthemes()

theme_list = get_theme_list()

def settheme(window,buttnon,text,tab,frame,activate):
    with gui.theme() as theme:

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

            gui.add_theme_color(gui.mvThemeCol_PopupBg, frame)

            


        
    gui.bind_theme(theme)    
    try:  
        settheme(themes[gui.get_value('thm')]['window'],
            themes[gui.get_value('thm')]['button'],
            themes[gui.get_value('thm')]['text'],
            themes[gui.get_value('thm')]['tab'],
            themes[gui.get_value('thm')]['frame'],
            themes[gui.get_value('thm')]['activate'])

        savelatesttheme()
            
    except:None

def loadlatesttheme():
    global lasttheme
    try:
        file1 = 'themes/latest.clab'
        file1 = open(file=file1)
        file1 = file1.readlines()

        modules1 = []
        for i in file1:
            modules1.append(i.replace('\n',''))
        lasttheme = modules1[0]
    except:
        lasttheme = 'default'
loadlatesttheme()


def makecustomtheme():
    themes[gui.get_value('themename')] = {
        "window": ast.literal_eval(gui.get_value('themewd')),
        "button": ast.literal_eval(gui.get_value('themebut')),
        "text": ast.literal_eval(gui.get_value('themetxt')),
        "tab": ast.literal_eval(gui.get_value('themetab')),
        "frame": ast.literal_eval(gui.get_value('themeframe')),
        "activate": ast.literal_eval(gui.get_value('themeact'))
    }
    savethemes()
    ref_themes()

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

def ref_themes():
    global themes,theme_list
    themes = loadthemes()
    theme_list = get_theme_list()
    gui.configure_item("thm", items=theme_list)









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
    try:
        gui.set_value('outline',bool(int(modules[13])))
        gui.set_value('outcolor',[float(modules[14]),float(modules[15]),float(modules[16]),255.0])
        gui.set_value('outthick',int(modules[17]))
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
        
        if gui.get_value('outline') == True:
            x.write('1'+'\n')
        else:
            x.write('0'+'\n')
        x.write(str(gui.get_value('outcolor')[0])+'\n')
        x.write(str(gui.get_value('outcolor')[1])+'\n')
        x.write(str(gui.get_value('outcolor')[2])+'\n')
        x.write(str(gui.get_value('outthick')))

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
    gui.set_value('outline',False)
    gui.set_value('outcolor',[0.0,0.0,0.0,0.0])
    gui.set_value('outthick',2)
    
def resetmainfunction():
    corshair()
def set_overley_current():
    gw.getWindowsWithTitle(title='Crosshairlabrender')[0].activate()
    time.sleep(1)
    gw.getWindowsWithTitle(title=title)[0].activate()









# ---------------------- Crosshair main ----------------------

def corshair():
    glfw.init()
    glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, True)
    glfw.window_hint(glfw.FLOATING, True)
    glfw.window_hint(glfw.DECORATED, False)
    global window
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
    



    def outline():
        
        xb=gui.get_value('outthick')
        
        gl.glColor3b(*(int(gui.get_value('outcolor')[0]/2),int(gui.get_value('outcolor')[1]/2),int(gui.get_value('outcolor')[2]/2)))
        
        gl.glLineWidth(thickness+xb*2)
        
        if gui.get_value('t')=='+':
            
            gl.glBegin(gl.GL_LINES)
            gl.glVertex2f(x - (size + gap)-xb, y)
            gl.glVertex2f(x - gap+xb, y)

            gl.glVertex2f(x + (size + gap)+xb, y)
            gl.glVertex2f(x + gap-xb, y)


            gl.glVertex2f(x, y - (size + gap)-xb)
            gl.glVertex2f(x, y - gap+xb)

            gl.glVertex2f(x, y + (size + gap)+xb)
            gl.glVertex2f(x, y + gap-xb)
            gl.glEnd()
        
        elif gui.get_value('t')=='x':
            
            gl.glBegin(gl.GL_LINES)
            gl.glVertex2f(x + gap-xb, y + gap-xb)
            gl.glVertex2f(x + size + gap+xb, y + size + gap+xb)

            gl.glVertex2f(x - gap+xb, y - gap+xb)
            gl.glVertex2f(x - size - gap-xb, y - size - gap-xb)

            gl.glVertex2f(x - gap+xb, y + gap-xb)
            gl.glVertex2f(x - size - gap-xb, y + size + gap+xb)

            gl.glVertex2f(x + gap-xb, y - gap+xb)
            gl.glVertex2f(x + size + gap+xb, y - size - gap-xb)
            gl.glEnd()
        
        elif gui.get_value('t')=='o':
            gl.glEnable(gl.GL_BLEND)
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
            gl.glEnable(gl.GL_LINE_SMOOTH)

            gl.glBegin(gl.GL_LINE_LOOP)

            if size > 0:
                num_segments = 20000
                for i in range(num_segments):
                    theta = 2.0 * math.pi * i / num_segments
                    dx = size * math.cos(theta)
                    dy = size * math.sin(theta)
                    gl.glVertex2f(x + dx, y + dy)

            gl.glEnd()
        
        gl.glLineWidth(thickness)


    while True:
        size = gui.get_value('size')
        gap = gui.get_value('gap')

        thickness = gui.get_value('thick')*2
        size = gui.get_value('size')
        gap = gui.get_value('gap')
        x = gui.get_value('posx')
        y = gui.get_value('posy')

        
        glfw.swap_buffers(window)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.poll_events()
        time.sleep(0.01)

        gl.glLineWidth(thickness)

        

        if gui.get_value('t')=='+' and gui.get_value('rep')==False:
            
            if gui.get_value('outline'):
                outline()
            
            gl.glColor3b(*get_color())

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
            
            if gui.get_value('outline'):
                outline()

            gl.glColor3b(*get_color())
            
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
            
            if gui.get_value('outline'):
                outline()

            gl.glColor3b(*get_color())
            
            gl.glEnable(gl.GL_BLEND)
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
            gl.glEnable(gl.GL_LINE_SMOOTH)

            gl.glBegin(gl.GL_LINE_LOOP)

            if size > 0:
                num_segments = 20000
                for i in range(num_segments):
                    theta = 2.0 * math.pi * i / num_segments
                    dx = size * math.cos(theta)
                    dy = size * math.sin(theta)
                    gl.glVertex2f(x + dx, y + dy)

            gl.glEnd()

            if gui.get_value('dot') == True:
                dot(x, y, thickness)

            gl.glDisable(gl.GL_LINE_SMOOTH)
            gl.glDisable(gl.GL_BLEND)
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





# ---------------------- tests ----------------------
b=[]
bindlist = {}
test_i = 0
def addtobindlist(pathname,bindname):
    global bindlist
    bindlist[gui.get_value(pathname)] = {"bind":gui.get_value(bindname)}
    print(bindlist)
    print(bindtag,pathname)


def addbind():
    global test_i, pics, saves

    refresh_binds()
    
    if test_i < len(saves):
        global bindtag,pathtag
        bindtag = 'bind'+str(test_i)
        pathtag = 'path'+str(test_i)
        try:
            gui.add_combo(label='Crosshair '+str(test_i+1), parent='bindparent',tag=pathtag,callback=refresh_binds, items=saves)
            gui.add_input_text(label='bind '+str(test_i+1), default_value=str(test_i), parent='bindparent', tag=bindtag,callback=refresh_binds)
            addtobindlist(pathtag,bindtag)
            b.append(test_i)
        except:None
        test_i=test_i+1


def bindloop():
    while True:
        time.sleep(0.01)
        
        for key, value in bindlist.items():
            try:
                if keyboard.is_pressed(value['bind']):
                
                    print(key,value)
                    file = f'saves/{key}'
                    file = open(file=file)
                    file = file.readlines()
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
                    try:
                        gui.set_value('outline',bool(int(modules[13])))
                        gui.set_value('outcolor',[float(modules[14]),float(modules[15]),float(modules[16]),255.0])
                        gui.set_value('outthick',int(modules[17]))
                    except:None
            except:None


    
def refresh_binds():
    global test_i, pics, saves

    pics,saves = load_files()
    try:
        for i in range(len(b)):
            addtobindlist('path'+str(i),'bind'+str(i))
            gui.configure_item('path'+str(i), items=saves)
    except:None


def delete_binds():
    try:
        for i in range(len(b)):
            gui.delete_item('path'+str(i))
            gui.delete_item('bind'+str(i))
        global test_i,bindlist
        test_i = 0
        bindlist.clear()
    except:None







# ---------------------- GUI ----------------------
modes = ['+','x','o']

def threads():
    settheme(themes[gui.get_value('thm')]['window'],
            themes[gui.get_value('thm')]['button'],
            themes[gui.get_value('thm')]['text'],
            themes[gui.get_value('thm')]['tab'],
            themes[gui.get_value('thm')]['frame'],
            themes[gui.get_value('thm')]['activate'])
    threading.Thread(target=corshair, daemon=True).start()
    threading.Thread(target=rgbeffect, daemon=True).start()
    threading.Thread(target=bindloop, daemon=True).start()

gui.create_context()
gui.create_viewport(title=title, width=400, height=400)
gui.setup_dearpygui()
gui.set_viewport_resizable(False)


with gui.window(label='CrosshairLab v2.3', width=385,height=400,no_title_bar=True,no_resize=True, no_move=True, show=True, tag='mainwindow'):
    with gui.tab_bar(label='cross'): 
        with gui.tab(label='Crosshair'):
            with gui.tab_bar(label="Crosshair"):
                with gui.tab(label='crosshair'):
                    gui.add_combo(label='type',tag='t',items=modes, default_value='+')
                    gui.add_slider_int(label='size', tag='size', min_value=1, max_value=50, default_value=6)
                    gui.add_slider_int(label='gap', tag='gap', min_value=0, max_value=50, default_value=4)
                    gui.add_slider_int(label='thick', tag='thick', min_value=1, max_value=5, default_value=2)
                    gui.add_checkbox(label='dot',tag='dot')
                    gui.add_checkbox(label='outline',tag='outline')
                    gui.add_slider_int(label='outline thick', tag='outthick', min_value=1, max_value=5, default_value=2)
                    gui.add_button(label='reset',callback=reset,width=100)
                with gui.tab(label='colors'):
                    with gui.tab_bar(label="color"):
                        with gui.tab(label='cross color'):
                            gui.add_color_picker(label='color:',tag='color', default_value=[255.0,255.0,255.0,255.0],height=180,width=180)
                            gui.add_checkbox(label='rgb effect',tag='rgbef')
                            gui.add_slider_int(label='effect speed',tag='efspeed',min_value=1,max_value=20,default_value=5)
                        with gui.tab(label='outline color'):
                            gui.add_color_picker(label='color:',tag='outcolor', default_value=[0.0,0.0,0.0,255.0],height=180,width=180)   
                with gui.tab(label='position'):
                    gui.add_slider_int(label='posx', min_value=1,max_value=screenx,default_value=screenx/2, tag='posx',width=300)
                    gui.add_slider_int(label='posy', min_value=1,max_value=screeny,default_value=screeny/2, tag='posy',width=300)
                    gui.add_button(label='reset position',callback=reset_pos,width=150)
                with gui.tab(label='save/load'):
                    gui.add_text(label='Load',default_value='Load')
                    gui.add_combo(label='',tag='file',items=saves)
                    with gui.group(horizontal=True):
                        gui.add_button(label='load',callback=load,width=100)
                        gui.add_button(label='refresh files',callback=ref_files,width=100)
                    gui.add_text(label='Save',default_value='Save')
                    gui.add_input_text(label='save name',tag='savename')
                    gui.add_button(label='save',callback=save,width=100)
       
        with gui.tab(label='theme'):
            with gui.tab_bar(label="themes"):
                with gui.tab(label='themes'):
                    gui.add_combo(label='themes',tag='thm',items=theme_list, default_value=lasttheme, width=300,callback=settheme)
                    gui.add_button(label='remove',callback=removetheme,width=100)
                with gui.tab(label='add custom theme'):
                    gui.add_input_text(label='name',tag='themename',default_value='name')
                    gui.add_input_text(label='window',tag='themewd',default_value=(f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"))
                    gui.add_input_text(label='button',tag='themebut',default_value=(f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"))
                    gui.add_input_text(label='text',tag='themetxt',default_value=(f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"))
                    gui.add_input_text(label='tab',tag='themetab',default_value=(f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"))
                    gui.add_input_text(label='frame',tag='themeframe',default_value=(f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"))
                    gui.add_input_text(label='activate',tag='themeact',default_value=(f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"+","+f"{random.randint(1,255)}"))
                    gui.add_button(label='add',callback=makecustomtheme,width=100)

        with gui.tab(label='Binds'):
             with gui.tab_bar(label='DevTests'):
                with gui.tab(label='Binds',tag='bindparent'):
                    with gui.group(horizontal=True):
                        gui.add_button(label='Add Bind',callback=addbind, width=100)
                        gui.add_button(label='Refresh Binds',callback=refresh_binds, width=100)
                        gui.add_button(label='Reset Binds',callback=delete_binds, width=100)
                    gui.add_text(label='',default_value='WARNING! Do Not Add 2 Binds For 1 Crosshair!')
        
        with gui.tab(label='img to cross'):
            with gui.tab_bar(label='img to cross'):
                with gui.tab(label='img to cross'):
                    gui.add_checkbox(label='replace crosshair with image',tag='rep')
                    gui.add_combo(label='path',tag='path',items=pics)
                    with gui.group(horizontal=True):
                        gui.add_button(label='refresh files',callback=ref_files,width=100)
                        gui.add_button(label='open folder',callback=open_folder,width=100)
        with gui.tab(label='fixes'):
            with gui.tab_bar(label='fixes'):
                with gui.tab(label='fixes'):            
                    gui.add_button(label='start main function',callback=resetmainfunction)
                    gui.add_button(label='set crosshair overley on top',callback=set_overley_current)







gui.show_viewport()
threads()
gui.start_dearpygui()
gui.destroy_context()