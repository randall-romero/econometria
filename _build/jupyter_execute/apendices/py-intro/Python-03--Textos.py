#!/usr/bin/env python
# coding: utf-8

# # Manipulando Textos

# ## Trabajando con mayúsculas y minúsculas

# In[1]:


personaje = "robin HOOD  "


# In[2]:


personaje.upper()


# In[3]:


personaje.lower()


# In[4]:


personaje.title()


# In[5]:


personaje.capitalize()


# ## Eliminando espacios

# In[6]:


personaje.strip()


# In[7]:


personaje = personaje.strip().title()
personaje


# ## Separando textos

# In[8]:


personaje.split(' ')


# In[9]:


nombre, apellido = personaje.split(' ')


# In[10]:


fibonacci_str = "1,1,2,3,5,8,13,21,34,55,89"
fibonacci_str.split(',')


# In[11]:


fibonacci_int = [int(x) for x in fibonacci_str.split(',')]
fibonacci_int


# ## Evaluando algunas condiciones

# In[12]:


dia, mes, año = "15 de septiembre de 1821".split(' de ')
print(f'{dia=}    {mes=}    {año=}')


# In[13]:


print(f"{año.startswith('18')=}")
print(f"{mes.endswith('embre')=}")


# In[14]:


print(f'{año.isnumeric()=}')
print(f'{mes.isnumeric()=}')


# In[15]:


len(mes)


# ## Operaciones con textos

# In[16]:


ladrido = "guau "


# In[17]:


ladrido * 3


# In[18]:


"balón"  + "pie"


# ## Contando palabras

# In[19]:


from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/nfWlot6h_JM?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>')


# In[20]:


shake_it_off = open("shake-it-off.txt", 'r', encoding='utf-8').read()

print(shake_it_off)


# In[21]:


shake_it_off.lower().count('shake')


# In[22]:


shake_it_off.lower().count('fake')


# In[23]:


shake_it_off.lower().count('hate')


# In[24]:


shake_it_off.lower().count('play')


# ## Uniendo textos

# In[25]:


separados = fibonacci_str.split(",")
separados


# In[26]:


' + '.join(separados) 


# ## Operación "slice" con textos

# In[27]:


libro = "El ingenioso hidalgo don Quijote de la Mancha"


# In[28]:


libro[:10]


# In[29]:


libro[-6:]


# In[30]:


'amor'[::-1]


# ## Acomodando texto en un formato

# In[31]:


ancho_línea = 54

print("=" * ancho_línea)
print("Título de mi libro".upper().center(ancho_línea))
print("Fulano de la O".center(ancho_línea))
print("\n")
print("EC4301".rjust(ancho_línea))
print("\n")
print("/°\\" * (ancho_línea//3))
print("\\_/" * (ancho_línea//3))


# ## Interpolando texto

# In[32]:


diasemana = 'lunes'
dia = 30
mes = 'Febrero'
año = 2020


# In[33]:


"Hoy es %s %d de %s de %d" % (diasemana, dia, mes, año)


# In[34]:


"Hoy es {0} {1} de {2} de {3}".format(diasemana, dia, mes, año)


# In[35]:


f"Hoy es {diasemana.upper()} {dia-1} de {mes.title()} de {año}"


# In[36]:


x = 1/7
x


# In[37]:


f"x es igual a {x:15.5f}"

