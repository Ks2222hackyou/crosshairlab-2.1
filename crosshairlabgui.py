import dearpygui.dearpygui as gui
import glfw
import win32gui
import OpenGL.GL as gl
import win32con, time
import math
import tkinter, os
import dearpygui.dearpygui as gui
from OpenGL.GL import *


from PIL import Image






color = (100,100,100) #https://www.rapidtables.com/web/color/RGB_Color.html
color1 = 'white'
if color1 == "black":
    color = (0,0,0)
else:
    None


modes = ['+','x','o']
try:
    pics = os.listdir('customcross')
except:os.makedirs('customcross');pics = os.listdir('customcross')

def open_folder():

    os.startfile('customcross')

    
def corshair():
    app = tkinter.Tk()

    screenx = app.winfo_screenwidth()
    screeny = app.winfo_screenheight()
    thickness = gui.get_value('thick')
    size = gui.get_value('size')
    gap = gui.get_value('gap')
    glfw.init()
    glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, True)
    glfw.window_hint(glfw.FLOATING, True)
    glfw.window_hint(glfw.DECORATED, False)

    window = glfw.create_window(screenx, screeny, 'tracers', None, None)
    glfw.make_context_current(window)
    gl.glOrtho(0, screenx, 0, screeny, -1, 1)

    handle = win32gui.FindWindow(0, 'tracers')

    exStyle = win32gui.GetWindowLong(handle, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(handle, win32con.GWL_EXSTYLE, exStyle | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

    color1 = color

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

    
    
    
    
    
    
    
    
    while True:
        
        color1 = (int(gui.get_value('r')/2), int(gui.get_value('g')/2), int(gui.get_value('b')/2))
        thickness = gui.get_value('thick')*2
        size = gui.get_value('size')
        gap = gui.get_value('gap')
        x = screenx / 2
        y = screeny / 2

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
            
            
            gui.set_value('r',255)
            gui.set_value('g',255)
            gui.set_value('b',255)


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
        
        
        
 






gui.create_context()
gui.create_viewport(title='cross', width=400, height=400)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)
gui.set_viewport_resizable(False)


with gui.window(label='cross', width=400,height=400,no_title_bar=True,no_resize=True, no_move=True, show=True):
    with gui.tab_bar(label='cross'):
        
        
        with gui.tab(label='default'):
            gui.add_listbox(label='type',tag='t',items=modes, default_value='+')
            gui.add_slider_int(label='size', tag='size', min_value=1, max_value=50, default_value=6)
            gui.add_slider_int(label='gap', tag='gap', min_value=1, max_value=50, default_value=4)
            gui.add_slider_int(label='thick', tag='thick', min_value=1, max_value=10, default_value=2)
            gui.add_text(label='Color')
            gui.add_slider_int(label='red', tag='r', min_value=0, max_value=255, default_value=255)
            gui.add_slider_int(label='green', tag='g', min_value=0, max_value=255, default_value=255)
            gui.add_slider_int(label='blue', tag='b', min_value=0, max_value=255, default_value=255)
            gui.add_checkbox(label='dot',tag='dot')
            gui.add_button(label='generate',callback=corshair)
        with gui.tab(label='image'):
            gui.add_checkbox(label='replace crosshair with image',tag='rep')
            gui.add_listbox(label='path',tag='path',items=pics)
            gui.add_button(label='open folder',callback=open_folder)
            gui.add_button(label='generate',callback=corshair)

            
        



gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()
