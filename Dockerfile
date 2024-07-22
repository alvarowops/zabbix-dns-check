FROM zabbix/zabbix-agent:alpine-6.0-latest

USER root

# Instalar Python y otras dependencias necesarias
RUN apk update && apk add --no-cache python3 py3-pip

# Crear un entorno virtual y activar
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar los módulos necesarios dentro del entorno virtual
RUN pip install python-whois dnspython

# Copiar los scripts y el archivo de configuración al contenedor
COPY whois_check.py /usr/local/bin/whois_check.py
COPY dns_check.py /usr/local/bin/dns_check.py
COPY zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf

# Establecer permisos ejecutables para los scripts
RUN chmod +x /usr/local/bin/whois_check.py
RUN chmod +x /usr/local/bin/dns_check.py

USER zabbix
