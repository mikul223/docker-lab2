## Команды запуска

Ручной запуск:
docker compose up -d

Запуск через Ansible:
ansible-playbook -i inventory.ini playbook.yml --ask-pass --ask-become-pass

## Адрес приложения

http://localhost:8080

## Схема

Ноутбук (Windows) → SSH-туннель → Хостовая Ubuntu VM (192.168.33.129) → KVM VM (192.168.122.178) → Контейнеры (frontend:80, backend:5000)

SSH-туннель с ноутбука:
ssh -L 8080:192.168.122.178:8080 -L 5000:192.168.122.178:5000 maria@192.168.33.129

## Проверка связи фронтенда с бэкендом

Внутри KVM VM:
curl http://localhost:5000/api/lemonades
Ожидается JSON-ответ со списком данных.

## Диагностика ограничения KVM

Проверка выполнена командой:
kvm-ok
Результат: KVM acceleration can be used 
