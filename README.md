# # Chatbot de WhatsApp con Flask, MySQL y RiveScript

Este proyecto es un **chatbot para WhatsApp** desarrollado con **Flask (Python)**, **MySQL** y **RiveScript**.  
Permite recibir mensajes de WhatsApp mediante la **API de Meta**, procesarlos con un motor de chatbot, guardar las interacciones en una base de datos y enviar respuestas automáticas al usuario.

---

## Funcionalidades

- Servidor Flask con un webhook para manejar mensajes de WhatsApp.
- Integración con la **API de WhatsApp Business de Meta**.
- Respuestas automáticas usando **RiveScript**.
- Registro de mensajes recibidos y enviados en **MySQL**.
- Evita insertar mensajes duplicados validando los IDs.
- Envía respuestas automáticas de vuelta al usuario vía WhatsApp.

---

## Tecnologías usadas

- **Python 3**
- **Flask**
- **RiveScript**
- **MySQL**
- **heyoo** (librería para la API de WhatsApp)

---

## Instalación

Cuenta en Meta Developers

source env/bin/activate
pip install rivescript
pip install mysql-connector-python
pip install heyoo