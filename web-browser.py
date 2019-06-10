import socket

mysoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysoc.connect(('dckira.org', 80))
cmd = 'GET http://dckira.org/sitedash/wp-content/uploads/elementor/thumbs/cru191-2-o73c4yq0wiaydty7gpavxu31e1zhzofnfx3tyyjqos.jpg HTTP/1.0\n\n'.encode()
mysoc.send(cmd)

while True:
    data = mysoc.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysoc.close()
