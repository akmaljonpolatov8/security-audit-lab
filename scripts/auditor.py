import socket
import os

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex(('127.0.0.1', port))
    s.close()
    return result == 0

print("--- ОТЧЕТ ПО БЕЗОПАСНОСТИ ---")
if check_port(8080):
    print("[!] ВНИМАНИЕ: Обнаружен подозрительный сервис на порту 8080!")
else:
    print("[+] Порт 8080 закрыт.")
nginx_version = os.popen('nginx -v 2>&1').read()
print(f"[*] Текущая версия сервера: {nginx_version.strip()}")
