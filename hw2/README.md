# find_min_mtu

Утилита для поиска минимального значения MTU в канале между конечными хостами.

Пример работы:

```
$> sudo docker run --rm find_min_mtu --host vk.com
Minimal MTU between local_host and vk.com is 1500
```

```
$> sudo docker run --rm find_min_mtu --host ya.ru
Minimal MTU between local_host and ya.ru is 1500
```

Обработка ошибок и ситуаций, при которых icmp заблокирован:

```
$> sudo docker run --rm find_min_mtu --host string
Connection is unavailable, because of error:
ping: string: Name or service not known
```

```
$> sudo docker run --rm find_min_mtu --host microsoft.com
Connection is unavailable, because of error:
PING microsoft.com (20.84.181.62) 0(28) bytes of data.
--- microsoft.com ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
```