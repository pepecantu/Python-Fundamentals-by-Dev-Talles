
name = 'josé'
print(name)  # José

print(name[0])      # j
print(name[1])      # o
print(name[2])      # s
print(name[3])      # é

# ¿Como obtener la última letra
print(name[-1])     # é

# (Start:Stop)
print(name[0:1])    # j
print(name[0:2])    # jo
print(name[0:3])    # Jos
print(name[0:4])    # José

# [Start:Stop:stepover]
print(name[0:4:1])  # josé
print(name[0:4:2])  # js
print(name[0:4:3])  # jé
print(name[0:4:4])  # j

print(name[0:3:1])  # jos
print(name[0:3:2])  # js
print(name[0:3:3])  # j

print(name[0:2:1])  # jo

# Escribir el nombre alreves
print(name[::-1])
